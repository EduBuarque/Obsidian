import os
import re
import sys
import json
import math
import sqlite3
import argparse
import yaml
import requests

# Configurações Padrão
OLLAMA_URL = "http://localhost:11434"
DEFAULT_EMBED_MODEL = "nomic-embed-text"
DB_NAME = "wiki_search_index.db"

STOPWORDS = {
    # Português
    "a", "o", "ao", "aos", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "um", "uma", "uns", "umas", "com", "por", "para", "que", "se", "como", "e", "ou", "mas",
    "por", "este", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas",
    # Inglês
    "the", "a", "an", "and", "or", "but", "if", "then", "else", "of", "at", "by", "from",
    "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when", "where", "why",
    "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
    "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can",
    "will", "just", "should", "now"
}

def tokenize(text):
    text = text.lower()
    # Remove acentos básicos de forma simplificada
    replacements = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c'
    }
    for orig, rep in replacements.items():
        text = text.replace(orig, rep)
    tokens = re.findall(r'\b\w+\b', text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]

# Classe para fallback semântico offline baseada em TF-IDF
class TFIDFVectorizer:
    def __init__(self, idf=None):
        self.idf = idf or {}
        
    def fit(self, all_docs_tokens):
        doc_count = len(all_docs_tokens)
        df = {}
        for doc in all_docs_tokens:
            for token in set(doc):
                df[token] = df.get(token, 0) + 1
        
        self.idf = {}
        for token, count in df.items():
            self.idf[token] = math.log(1 + doc_count / (1 + count))
            
    def transform(self, doc_tokens):
        tf = {}
        for token in doc_tokens:
            tf[token] = tf.get(token, 0) + 1
            
        vector = {}
        for token, count in tf.items():
            if token in self.idf:
                vector[token] = count * self.idf[token]
        return vector

    @staticmethod
    def cosine_similarity(vec1, vec2):
        dot = 0.0
        for k, v1 in vec1.items():
            if k in vec2:
                dot += v1 * vec2[k]
        norm1 = math.sqrt(sum(v*v for v in vec1.values()))
        norm2 = math.sqrt(sum(v*v for v in vec2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

# Classe para gerenciar banco de dados SQLite
class SearchIndexDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        # Tabela de arquivos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                relative_path TEXT UNIQUE,
                tags TEXT,
                frontmatter TEXT
            )
        """)
        # Tabela de chunks
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER,
                header TEXT,
                content TEXT,
                dense_vector TEXT,  -- JSON string de floats
                tfidf_vector TEXT,  -- JSON string de dict {token: tfidf}
                tokens TEXT,        -- Lista de tokens separados por espaço
                FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
            )
        """)
        # Tabela de metadados gerais
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS metadata (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        self.conn.commit()
        
    def clear_index(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM chunks")
        cursor.execute("DELETE FROM files")
        cursor.execute("DELETE FROM metadata")
        self.conn.commit()
        
    def save_file(self, relative_path, tags, frontmatter):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO files (relative_path, tags, frontmatter) VALUES (?, ?, ?)",
            (relative_path, json.dumps(tags), json.dumps(frontmatter, default=str))
        )
        return cursor.lastrowid
        
    def save_chunk(self, file_id, header, content, dense_vector, tfidf_vector, tokens):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO chunks (file_id, header, content, dense_vector, tfidf_vector, tokens)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                file_id, 
                header, 
                content, 
                json.dumps(dense_vector) if dense_vector else None,
                json.dumps(tfidf_vector) if tfidf_vector else None,
                " ".join(tokens)
            )
        )
        
    def save_metadata(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()
        
    def get_metadata(self, key):
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM metadata WHERE key = ?", (key,))
        row = cursor.fetchone()
        return row[0] if row else None
        
    def get_all_chunks(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT c.id, c.header, c.content, c.dense_vector, c.tfidf_vector, c.tokens, f.relative_path, f.tags
            FROM chunks c
            JOIN files f ON c.file_id = f.id
        """)
        return cursor.fetchall()

# Função para testar se o Ollama está online
def check_ollama_online():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Função para gerar embedding usando o Ollama
def get_ollama_embedding(text, model_name=DEFAULT_EMBED_MODEL):
    try:
        # Tenta primeiro a API /api/embed (mais recente)
        response = requests.post(
            f"{OLLAMA_URL}/api/embed",
            json={"model": model_name, "input": text},
            timeout=5
        )
        if response.status_code == 200:
            return response.json().get("embeddings", [[]])[0]
            
        # Fallback para a antiga /api/embeddings
        response = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={"model": model_name, "prompt": text},
            timeout=5
        )
        if response.status_code == 200:
            return response.json().get("embedding", [])
    except Exception as e:
        print(f"[Ollama Error] Não foi possível obter embedding para o texto: {e}", file=sys.stderr)
    return None

# Função para extrair chunks de um markdown com base nos cabeçalhos
def extract_chunks_from_markdown(content):
    # Separar Frontmatter
    frontmatter = {}
    remaining_content = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except Exception as e:
                print(f"[YAML Warning] Erro ao analisar frontmatter: {e}", file=sys.stderr)
            remaining_content = parts[2]
            
    # Regex para cabeçalhos Markdown (# a ####)
    header_pattern = re.compile(r'^(#{1,4})\s+(.+)$', re.MULTILINE)
    
    chunks = []
    lines = remaining_content.splitlines()
    
    current_header_stack = []
    current_chunk_lines = []
    
    def get_header_path():
        if not current_header_stack:
            return "Geral"
        return " > ".join(current_header_stack)
        
    for line in lines:
        match = header_pattern.match(line)
        if match:
            # Salvar chunk acumulado se houver
            if current_chunk_lines:
                chunk_text = "\n".join(current_chunk_lines).strip()
                if chunk_text:
                    chunks.append((get_header_path(), chunk_text))
                current_chunk_lines = []
                
            level = len(match.group(1))  # número de #
            header_title = match.group(2).strip()
            
            # Ajustar a pilha de cabeçalhos baseado no nível
            if len(current_header_stack) >= level:
                current_header_stack = current_header_stack[:level-1]
            current_header_stack.append(header_title)
        else:
            current_chunk_lines.append(line)
            
    # Salvar o último chunk
    if current_chunk_lines:
        chunk_text = "\n".join(current_chunk_lines).strip()
        if chunk_text:
            chunks.append((get_header_path(), chunk_text))
            
    return frontmatter, chunks

# Executa a indexação
def run_indexing(model_name=DEFAULT_EMBED_MODEL):
    print("=== Iniciando Indexação ===")
    
    # 1. Verificar Ollama
    ollama_online = check_ollama_online()
    if ollama_online:
        print(f"[Embedding Mode] Ollama ONLINE. Usando modelo: '{model_name}'")
    else:
        print("[Embedding Mode] Ollama OFFLINE. Usando fallback de TF-IDF local.")
        
    db = SearchIndexDB(DB_NAME)
    db.clear_index()
    
    wiki_dirs = ["wiki/core-knowledge", "wiki/logbook"]
    all_chunks_raw = []  # List of tuples: (file_path, frontmatter, header, text, tokens)
    
    # 2. Ler arquivos e extrair chunks
    for w_dir in wiki_dirs:
        if not os.path.exists(w_dir):
            continue
        for root, _, files in os.walk(w_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, start=".")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        frontmatter, chunks = extract_chunks_from_markdown(content)
                        tags = frontmatter.get("tags", [])
                        
                        file_id = db.save_file(rel_path, tags, frontmatter)
                        
                        for header, text in chunks:
                            tokens = tokenize(text)
                            all_chunks_raw.append({
                                "file_id": file_id,
                                "header": header,
                                "content": text,
                                "tokens": tokens,
                                "rel_path": rel_path
                            })
                    except Exception as e:
                        print(f"[File Error] Erro ao ler {rel_path}: {e}", file=sys.stderr)
                        
    if not all_chunks_raw:
        print("Nenhum documento markdown encontrado nas pastas da wiki para indexar.")
        return
        
    print(f"Total de {len(all_chunks_raw)} seções (chunks) encontradas.")
    
    # 3. Construir e treinar TF-IDF local para fallback semântico
    print("Construindo vetorizador TF-IDF local...")
    tfidf_vectorizer = TFIDFVectorizer()
    tfidf_vectorizer.fit([c["tokens"] for c in all_chunks_raw])
    
    # Salvar vocabulário/IDF no banco
    db.save_metadata("tfidf_idf", json.dumps(tfidf_vectorizer.idf))
    db.save_metadata("embedding_mode", "ollama" if ollama_online else "tfidf")
    db.save_metadata("ollama_model", model_name if ollama_online else "")
    
    # 4. Processar e salvar cada chunk no banco
    for idx, c in enumerate(all_chunks_raw):
        # Gerar representação TF-IDF
        tfidf_vec = tfidf_vectorizer.transform(c["tokens"])
        
        # Gerar dense embedding se Ollama estiver online
        dense_vec = None
        if ollama_online:
            print(f"[{idx+1}/{len(all_chunks_raw)}] Gerando embedding Ollama para: {c['rel_path']} > {c['header']}")
            # Concatenar cabeçalho + conteúdo para melhor busca semântica
            full_text_to_embed = f"{c['header']}\n{c['content']}"
            dense_vec = get_ollama_embedding(full_text_to_embed, model_name)
            
        db.save_chunk(
            file_id=c["file_id"],
            header=c["header"],
            content=c["content"],
            dense_vector=dense_vec,
            tfidf_vector=tfidf_vec,
            tokens=c["tokens"]
        )
        
    db.conn.commit()
    print("=== Indexação Concluída com Sucesso! ===")

# Executa a busca híbrida (BM25 + Semantic via Reciprocal Rank Fusion)
def run_search(query, model_name=DEFAULT_EMBED_MODEL, top_n=5, verbose=False, synthesize=False, gen_model="llama3"):
    db = SearchIndexDB(DB_NAME)
    
    # Obter configuração de indexação
    db_mode = db.get_metadata("embedding_mode")
    if not db_mode:
        print("Erro: O índice está vazio. Execute a indexação primeiro usando '--index'.", file=sys.stderr)
        return
        
    ollama_model_indexed = db.get_metadata("ollama_model")
    
    chunks = db.get_all_chunks()
    if not chunks:
        print("A base de conhecimento indexada está vazia.", file=sys.stderr)
        return
        
    query_tokens = tokenize(query)
    
    # === 1. BUSCA LEXICAL (BM25) ===
    # Usamos o rank-bm25
    from rank_bm25 import BM25Okapi
    
    corpus_tokens = [c["tokens"].split() for c in chunks]
    bm25 = BM25Okapi(corpus_tokens)
    
    bm25_scores = bm25.get_scores(query_tokens)
    
    # Rankear BM25
    bm25_ranked = sorted(enumerate(bm25_scores), key=lambda x: x[1], reverse=True)
    bm25_rank_map = {idx: rank for rank, (idx, _) in enumerate(bm25_ranked)}
    
    # === 2. BUSCA SEMÂNTICA (Dense Vector ou Fallback TF-IDF) ===
    semantic_scores = [0.0] * len(chunks)
    
    # Tenta rodar Ollama se foi indexado em modo ollama
    run_semantic_ollama = (db_mode == "ollama" and check_ollama_online())
    
    if run_semantic_ollama:
        # Usa o modelo do banco ou o provido por CLI
        use_model = model_name if model_name != DEFAULT_EMBED_MODEL else ollama_model_indexed
        query_embed = get_ollama_embedding(query, use_model)
        
        if query_embed:
            for idx, c in enumerate(chunks):
                if c["dense_vector"]:
                    doc_embed = json.loads(c["dense_vector"])
                    # Cosseno
                    dot = sum(a * b for a, b in zip(query_embed, doc_embed))
                    norm_q = math.sqrt(sum(a * a for a in query_embed))
                    norm_d = math.sqrt(sum(b * b for b in doc_embed))
                    semantic_scores[idx] = dot / (norm_q * norm_d) if norm_q and norm_d else 0.0
        else:
            print("[Warning] Falha ao obter embedding da query no Ollama. Usando fallback de TF-IDF local.", file=sys.stderr)
            run_semantic_ollama = False
            
    if not run_semantic_ollama:
        # Fallback local TF-IDF
        idf_data = json.loads(db.get_metadata("tfidf_idf") or "{}")
        tfidf_vectorizer = TFIDFVectorizer(idf_data)
        query_tfidf = tfidf_vectorizer.transform(query_tokens)
        
        for idx, c in enumerate(chunks):
            if c["tfidf_vector"]:
                doc_tfidf = json.loads(c["tfidf_vector"])
                semantic_scores[idx] = TFIDFVectorizer.cosine_similarity(query_tfidf, doc_tfidf)
                
    # Rankear Semântica
    semantic_ranked = sorted(enumerate(semantic_scores), key=lambda x: x[1], reverse=True)
    semantic_rank_map = {idx: rank for rank, (idx, _) in enumerate(semantic_ranked)}
    
    # === 3. FUSÃO DE POSTOS (Reciprocal Rank Fusion - RRF) ===
    # RRF(d) = sum( 1 / (k + rank_i(d)) )
    k = 60
    rrf_scores = []
    
    for idx in range(len(chunks)):
        rank_bm25_val = bm25_rank_map.get(idx, len(chunks))
        rank_sem_val = semantic_rank_map.get(idx, len(chunks))
        
        score_rrf = (1.0 / (k + rank_bm25_val)) + (1.0 / (k + rank_sem_val))
        rrf_scores.append((idx, score_rrf, rank_bm25_val, rank_sem_val, bm25_scores[idx], semantic_scores[idx]))
        
    # Ordenar por pontuação RRF descendente
    rrf_ranked = sorted(rrf_scores, key=lambda x: x[1], reverse=True)
    
    # === Exibir Resultados ===
    mode_str = "Ollama (Dense)" if run_semantic_ollama else "Local TF-IDF (Sparse)"
    print(f"\nResultados da pesquisa por: \"{query}\"")
    print(f"Modo Semântico ativo: {mode_str}\n")
    
    for i in range(min(top_n, len(rrf_ranked))):
        idx, rrf_score, rank_bm25_val, rank_sem_val, raw_bm25, raw_sem = rrf_ranked[i]
        c = chunks[idx]
        tags = json.loads(c["tags"])
        
        print(f"{i+1}. [{c['relative_path']}] > {c['header']}")
        print(f"   Tags: {', '.join(tags) if tags else 'Nenhuma'}")
        
        if verbose:
            print(f"   Scores detalhados:")
            print(f"     - RRF Score: {rrf_score:.5f}")
            print(f"     - Posto BM25: #{rank_bm25_val+1} (Score: {raw_bm25:.3f})")
            print(f"     - Posto Semântico: #{rank_sem_val+1} (Similaridade Cosseno: {raw_sem:.3f})")
            
        print("   Conteúdo:")
        # Indenta o texto para exibição
        indented_content = "\n".join("      " + line for line in c["content"].splitlines()[:8])
        print(indented_content)
        if len(c["content"].splitlines()) > 8:
            print("      ...")
        print("-" * 50)

    # === SÍNTESE GERATIVA DE RESPOSTA ===
    if synthesize:
        print("\n=== Sintetizando Resposta com Ollama ===")
        if not check_ollama_online():
            print("Erro: O Ollama está offline. A síntese requer o Ollama ativo localmente.", file=sys.stderr)
            return

        # Construir o contexto a partir das top_n seções recuperadas
        context_parts = []
        for i in range(min(top_n, len(rrf_ranked))):
            idx = rrf_ranked[i][0]
            c = chunks[idx]
            tags = json.loads(c["tags"])
            context_parts.append(
                f"Documento: {c['relative_path']}\n"
                f"Seção: {c['header']}\n"
                f"Tags: {', '.join(tags) if tags else 'Nenhuma'}\n"
                f"Conteúdo:\n{c['content']}\n"
                f"---"
            )
        
        context_str = "\n".join(context_parts)
        
        # Montar o prompt estruturado
        prompt = (
            "Você é um assistente especialista e co-piloto encarregado de responder à pergunta do usuário "
            "com base EXCLUSIVAMENTE nos trechos fornecidos da nossa base de conhecimento (wiki).\n"
            "Sua resposta deve ser estruturada, direta, objetiva e inteiramente em Português do Brasil (pt-BR).\n"
            "Não invente fatos fora do contexto fornecido. Se os trechos fornecidos não contiverem a informação "
            "necessária para responder à pergunta, diga claramente que a informação não foi encontrada na base de conhecimento.\n\n"
            "Trechos de Contexto:\n"
            f"{context_str}\n\n"
            f"Pergunta do Usuário: {query}\n\n"
            "Resposta Sintetizada:\n"
        )
        
        print(f"Usando modelo gerador: '{gen_model}'")
        print("Resposta:\n")
        
        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": gen_model,
                    "prompt": prompt,
                    "stream": True
                },
                stream=True,
                timeout=30
            )
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        chunk_data = json.loads(line.decode('utf-8'))
                        text = chunk_data.get("response", "")
                        sys.stdout.write(text)
                        sys.stdout.flush()
                print("\n")
            else:
                print(f"\nErro da API Ollama: Status Code {response.status_code}", file=sys.stderr)
        except Exception as e:
            print(f"\nErro ao chamar o modelo gerador Ollama: {e}", file=sys.stderr)

# Bloco Principal da CLI
if __name__ == "__main__":
    if sys.platform.startswith('win'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    parser = argparse.ArgumentParser(description="CLI de Busca Híbrida para Gemini Knowledge Engine (GKE)")
    parser.add_argument("--index", action="store_true", help="Reconstruir o índice de busca com base nos arquivos atuais na wiki")
    parser.add_argument("--query", type=str, help="Executar uma busca por texto na wiki usando BM25 + Semântica")
    parser.add_argument("--model", type=str, default=DEFAULT_EMBED_MODEL, help=f"Modelo do Ollama para embeddings (padrão: {DEFAULT_EMBED_MODEL})")
    parser.add_argument("--top", type=int, default=5, help="Número de resultados a retornar (padrão: 5)")
    parser.add_argument("--verbose", action="store_true", help="Exibir detalhes de pontuação e postos individuais")
    parser.add_argument("--synthesize", action="store_true", help="Sintetizar uma resposta em linguagem natural usando o Ollama")
    parser.add_argument("--gen-model", type=str, default="llama3", help="Modelo gerador do Ollama para síntese (padrão: llama3)")
    
    args = parser.parse_args()
    
    # Se nenhum argumento for fornecido, exibir help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    if args.index:
        run_indexing(args.model)
        
    if args.query:
        run_search(args.query, args.model, args.top, args.verbose, args.synthesize, args.gen_model)
