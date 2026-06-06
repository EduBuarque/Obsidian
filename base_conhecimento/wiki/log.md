# Registro Cronológico de Operações (GKE Log)

Histórico, tipo append-only, rastreando as ações do Gemini Knowledge Engine.

---

## [2026-05-26] Setup | Inicialização Estrutural
- Criação das pastas `/raw` e `/wiki` com separações entre `core-knowledge` e `logbook`.
- Elaboração do arquivo padrão `GKE_RULES.md`.
- Geração dos índices e logs vazios (`index.md` e `log.md`).

---

## [2026-05-27] Ingest | Processamento Inicial da Base de Conhecimento

### Fontes Processadas

**Clippings/ (Prioridade Alta) — 7 arquivos:**
| Arquivo | Tema | Destino na Wiki |
|---|---|---|
| A Gentle Introduction to Bayes Theorem for ML | Probabilidade e Bayes | `Teorema-de-Bayes.md` |
| Decision tree methods: applications for classification | Árvores de Decisão | `Arvores-de-Decisao.md` |
| Deep Learning Book-Cap 21 - Por Que a Regularização Ajuda | Regularização e Overfitting | `Regularizacao.md` |
| Kernel Trick Explained SVMs and Nonlinear Patterns | Kernel Trick e SVM | `Kernel-Trick-e-SVM.md` |
| The Kernel Trick in Machine Learning | Kernel Trick e SVM | `Kernel-Trick-e-SVM.md` (consolidado) |
| O que são classificadores Naïve Bayes? (IBM) | Naïve Bayes | `Teorema-de-Bayes.md` (seção) |
| O que é Regularização? (IBM) | Regularização | `Regularizacao.md` (seção) |

**raw/core-knowledge/ — 1 arquivo:**
| Arquivo | Tema | Destino na Wiki |
|---|---|---|
| Data Mining - Técnicas.md | Técnicas de DM + CRISP-DM | `Data-Mining-Tecnicas.md` |

### Artigos Criados em wiki/core-knowledge/
1. `Teorema-de-Bayes.md` — Síntese completa: probabilidade condicional, MAP, Naïve Bayes, Bayes Optimal Classifier, Otimização Bayesiana
2. `Arvores-de-Decisao.md` — Síntese: estrutura, algoritmos (CART/C4.5/CHAID/QUEST), splitting/pruning/stopping, exemplo MDD
3. `Regularizacao.md` — Síntese: L1/L2/Dropout, Bias-Variance Tradeoff, questão em aberto sobre generalização
4. `Kernel-Trick-e-SVM.md` — Síntese: princípio matemático, kernels (RBF/Polinomial/Sigmoid/Linear), SVM, extensões (GP, Kernel PCA)
5. `Data-Mining-Tecnicas.md` — Síntese completa: todas as categorias de técnicas + CRISP-DM + complementações modernas

### Links Cruzados Gerados
- `Teorema-de-Bayes` ↔ `Data-Mining-Tecnicas` (Naïve Bayes como técnica)
- `Arvores-de-Decisao` ↔ `Regularizacao` (poda ≈ regularização)
- `Arvores-de-Decisao` ↔ `Data-Mining-Tecnicas` (técnica de classificação)
- `Regularizacao` ↔ `Data-Mining-Tecnicas` (controle de overfitting em Gradient Boosting)
- `Kernel-Trick-e-SVM` ↔ `Data-Mining-Tecnicas` (SVM como técnica)
- `Kernel-Trick-e-SVM` ↔ `Regularizacao` (margem máxima SVM como regularização implícita)
- `Teorema-de-Bayes` ↔ `Kernel-Trick-e-SVM` (conexão probabilística)

### index.md
- Atualizado com todas as 5 entradas no Cofre Conceitual
- Grafo de conexões Mermaid adicionado

### Observações
- 2 clippings IBM (Naïve Bayes e Regularização) tinham conteúdo bloqueado por paywall/chatbot. O conteúdo foi sintetizado a partir das fontes complementares presentes nos outros Clippings.
- `raw/logbook/` está vazio — nenhum logbook gerado neste ciclo.
- `wiki/logbook/` permanece vazio aguardando projetos empíricos.

---

## [2026-05-28] Ingest | Processamento de Novo Clipping (KDD)

### Fontes Processadas

**Clippings/ (Prioridade Alta) — 1 arquivo:**
| Arquivo | Tema | Destino na Wiki | Hash SHA-256 |
|---|---|---|---|
| Knowledge Discovery in Databases 9 Steps to Success.md | Processo KDD de 9 etapas | `Processo-KDD.md` | f650829552921253bacf6c4113c9d3ab128b901168591944b55bed91d158246a |

### Artigos Criados em wiki/core-knowledge/
1. `Processo-KDD.md` — Síntese conceitual do processo KDD (9 passos), relações de trade-offs, pré-processamento e desafios em produção.

### Links Cruzados Gerados / Atualizados
- `Processo-KDD` ↔ `Data-Mining-Tecnicas` (CRISP-DM como metodologia relacionada; data mining como subfase do KDD)
- `Arvores-de-Decisao` ↔ `Processo-KDD` (interpretabilidade no passo 6 do KDD)
- `Regularizacao` ↔ `Processo-KDD` (ajuste de parâmetros no passo 7 do KDD)

### index.md
- Atualizado com a nova entrada no Cofre Conceitual (Metodologias)
- Grafo Mermaid de conexões atualizado com o nó KDD e novas ligações

### Observações / Auditoria de Integridade
- A auditoria de integridade varreu a base e confirmou que a nova nota está integrada de forma bidirecional. Não foram encontradas notas órfãs ou links quebrados.

---

## [2026-05-29] Upgrade | Reestruturação de Metadados e Rastreabilidade

### Atualizações de Diretrizes (GKE_RULES.md)
- **Seção 3.4 (Rastreabilidade de Procedência):** Atualizada para formalizar a exigência do link de retorno direto à fonte original via campo `original_source` nos metadados.
- **Seção 4.1 (Schema de Metadados):** Alteração do campo de `sources` para `original_source` para refletir um link estruturado, garantindo portabilidade e auditoria direta dos resumos sintetizados.

### Reprocessamento da Wiki
- Atualização em lote de todos os arquivos em `/wiki/core-knowledge/` (`Teorema-de-Bayes.md`, `Data-Mining-Tecnicas.md`, `Processo-KDD.md`, `Arvores-de-Decisao.md`, `Kernel-Trick-e-SVM.md`, `Regularizacao.md`) para substituir a tag `sources` por `original_source`, referenciando corretamente a contrapartida original na pasta `raw/`.

### Observações / Auditoria de Integridade
- Todas as páginas da wiki agora possuem links diretos de retorno funcionais para suas fontes originais em `raw/`, em conformidade total com as regras atualizadas.

---

## [2026-06-06] Ingest | Processamento de Clippings sobre Árvores de Decisão

### Checksum Protocol (Verificação de Duplicatas)

3 novos arquivos detectados em `Clippings/`. Nenhum constava no registro de hashes → processamento autorizado.

| Arquivo | Hash SHA-256 | Presente no Log? |
|---|---|---|
| Decision Trees.md | 13061C6599C3F984C8D48301B56994E906F5553337531E313DC28475013DBF0F | ❌ Novo |
| Árvores de decisão.md | 8CB9C63D96EDB7084C19B01A3968C78959EB9372EADA1E57227C16A7B7F86F4E | ❌ Novo |
| Tutorial sobre classificação por árvore de decisão em Python.md | A61C158B214220E846D746004CAC46A51FDD88224F743D9E364B29DC7ECC4945 | ❌ Novo |

### Fontes Processadas

**Clippings/ (Prioridade Alta) — 3 arquivos:**
| Arquivo | Tema | Destino na Wiki |
|---|---|---|
| Decision Trees.md | Documentação scikit-learn: implementação, classificação, regressão, valores ausentes, poda | `Arvores-de-Decisao.md` (atualizado) |
| Árvores de decisão.md | Panorama completo: AID, CHAID, CART, ID3, C4.5, QUEST, CRUISE, GUIDE, ensembles, ensembles | `Arvores-de-Decisao.md` (atualizado) |
| Tutorial sobre classificação por árvore de decisão em Python.md | Tutorial prático Python/scikit-learn: criação, otimização, visualização, decision stump | `Arvores-de-Decisao.md` (atualizado) |

### Atualização em wiki/core-knowledge/

1. `Arvores-de-Decisao.md` — Síntese expandida com:
   - Formalização matemática (critérios de divisão, Gini, Entropia, MSE, MAE)
   - Algoritmos single-tree completos (AID, CHAID, CART, ID3, C4.5, C5.0, QUEST, CRUISE, GUIDE)
   - Métodos de ensemble (AdaBoost, Random Forest, Gradient Boosting, XGBoost)
   - Árvores incrementais (VFDT, ITI) e ADTrees
   - Implementação no Scikit-Learn (classificação, regressão, visualização, valores ausentes, poda cost-complexity, decision stump)
   - Dicas de uso prático
   - Campo `aliases` adicionado ao YAML
   - Campo `updated` adicionado ao YAML

### Links Cruzados Verificados / Atualizados
- `Arvores-de-Decisao` ↔ `Data-Mining-Tecnicas` (ensemble como técnica) ✅
- `Arvores-de-Decisao` ↔ `Regularizacao` (overfitting/poda) ✅
- `Arvores-de-Decisao` ↔ `Teorema-de-Bayes` (entropia/informação) ✅
- `Arvores-de-Decisao` ↔ `Data-Mining-Tecnicas` (CRISP-DM) ✅
- `Arvores-de-Decisao` ↔ `Processo-KDD` (passo 6) ✅
- `Arvores-de-Decisao` ↔ `Kernel-Trick-e-SVM` (classificação) ✅
- Novo link adicional: `Arvores-de-Decisao` ↔ `Processo-KDD` (passo 7, ensembles)

### Movimentação de Arquivos (Obrigatória)
- `Clippings/Decision Trees.md` → `raw/core-knowledge/Decision Trees.md` ✅
- `Clippings/Árvores de decisão.md` → `raw/core-knowledge/Árvores de decisão.md` ✅
- `Clippings/Tutorial sobre classificação por árvore de decisão em Python.md` → `raw/core-knowledge/Tutorial sobre classificação por árvore de decisão em Python.md` ✅

### Auditoria de Integridade
- ✅ Nenhuma nota órfã detectada
- ✅ Todos os links `[[]]` apontam para arquivos existentes
- ✅ `original_source` atualizado com todas as 4 fontes (1 original + 3 novas)
- ✅ `Clippings/` agora está vazia (backlog limpo)
- ✅ `index.md` não requer atualização (árvore de decisão já catalogada)
