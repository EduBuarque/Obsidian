## Introdução

A Mineração de Dados (_Data Mining_) reúne técnicas estatísticas, matemáticas e computacionais voltadas à **descoberta de padrões, relações, comportamentos e conhecimento útil** a partir de grandes volumes de dados. Essas técnicas podem ter objetivos **preditivos** — antecipando eventos ou estimando valores — ou **descritivos**, buscando compreender estruturas, agrupamentos, associações e desvios existentes nos dados.

 A técnica se situa na **interseção entre estatística, inteligência artificial e aprendizado de máquina** , e faz parte de um processo mais amplo chamado **KDD** (_Knowledge Discovery in Databases_). O fluxo típico do KDD é:
```
Seleção → Pré-processamento → Transformação → Data Mining → Interpretação/Avaliação
```

Na prática, a **escolha da técnica** depende menos do algoritmo em si e mais das características do problema, da **natureza dos dados disponíveis, do objetivo analítico, da interpretabilidade desejada, da disponibilidade de rótulos e das restrições computacionais**. Por isso, organizar essas abordagens por cenário de utilização, pré-requisitos, forças e limitações ajuda a construir uma visão estratégica e aplicada da disciplina.

---
# Coletânea Inicial de Técnicas de Data Mining

# 1. Tarefas Preditivas: Classificação e Regressão

O objetivo das tarefas preditivas é estimar um valor futuro ou desconhecido a partir de padrões aprendidos em dados históricos.  
Quando o alvo é categórico, trata-se de **classificação**; quando é numérico contínuo, trata-se de **regressão**.
## Características Gerais

- **Tipo de aprendizado:** Supervisionado
- **Necessidade de rótulos:** Sim
- **Objetivo:** Predizer classes, probabilidades ou valores
- **Principais desafios:** _Overfitting_, qualidade dos dados, desbalanceamento e generalização
## Cenários de Utilização

- Análise de risco de crédito
- Diagnóstico médico
- Predição de churn
- Forecast de demanda
- Detecção de spam
- Precificação
- Marketing direcionado
- Previsão de séries temporais
- Score de propensão
## Pré-requisitos

- Dados históricos rotulados
- Variáveis representativas do fenômeno
- Processo de preparação de dados
- Tratamento de valores ausentes e ruídos
- Separação entre treino, validação e teste

---
## Técnicas Comuns, Forças e Fraquezas

### Árvores de Decisão (CART, C4.5, CHAID)

#### Características

Modelos baseados em regras hierárquicas de decisão.
#### Forças
- Alta interpretabilidade
- Fácil visualização
- Pouco pré-processamento
- Aceitam variáveis numéricas e categóricas
- Boa explicabilidade para negócio
#### Fraquezas
- Instabilidade estrutural
- Sensíveis a pequenas alterações nos dados
- Tendência ao _overfitting_
- Baixa capacidade de extrapolação
#### Cenários Indicados
- Crédito
- Saúde
- Compliance
- Sistemas explicáveis
- Modelos para usuários de negócio

---
### Random Forest

#### Características
Conjunto (_ensemble_) de múltiplas árvores de decisão.
#### Forças
- Excelente capacidade preditiva
- Redução de _overfitting_
- Robusto a ruído
- Lida bem com alta dimensionalidade
- Mede importância das variáveis
#### Fraquezas
- Menor interpretabilidade
- Custo computacional maior
- Pode gerar modelos muito grandes
#### Cenários Indicados
- Score de risco
- Predição tabular
- Dados heterogêneos
- Problemas com muitas variáveis

**Obs**.: Enquanto uma **Arvore de Decisão** constrói uma estrutura hierárquica de perguntas e respostas para chegar a uma previsão, **Random Forest** é uma técnica de ensemble que cria centenas ou milhares de árvores de decisão e combina seus resultados.

---
### Gradient Boosting (XGBoost, LightGBM, CatBoost)

#### Características
Modelos sequenciais que corrigem iterativamente erros anteriores.
#### Forças
- Altíssima performance preditiva
- Excelente para dados tabulares
- Lida bem com relações complexas
- Muito utilizado em competições e produção
#### Fraquezas
- Sensível a hiperparâmetros
- Maior complexidade de ajuste
- Menor interpretabilidade
- Pode sofrer *overfitting* sem **regularização**
#### Cenários Indicados
- Finanças
- Marketing Analytics
- Sistemas de score
- Predição de churn
- Detecção de fraude

---
### Naïve Bayes

#### Características
Modelo probabilístico baseado no _Teorema de Bayes_.
#### Forças
- Muito rápido
- Simples
- Funciona bem com texto
- Pouca necessidade computacional
#### Fraquezas
- Suposição forte de independência
- Sensível a atributos correlacionados
- Limitações em relações complexas
#### Cenários Indicados
- Classificação de texto
- Spam
- NLP inicial
- Sistemas simples de categorização

---
### Redes Neurais Artificiais (ANN / Deep Learning)

#### Características

Modelos inspirados em redes neurais biológicas.
#### Forças
- Capturam relações altamente não lineares
- Excelente performance em imagens, áudio e texto
- Alta capacidade de generalização
#### Fraquezas
- Baixa interpretabilidade
- Alto custo computacional
- Necessitam grande volume de dados
- Processo de treinamento complexo
#### Cenários Indicados
- Visão computacional
- NLP
- Séries temporais complexas
- Sistemas de recomendação

---
### Support Vector Machines (SVM)

#### Características
Buscam hiperplanos ótimos de separação.
#### Forças
- Muito eficientes em alta dimensionalidade
- Bons resultados com poucas amostras
- Kernel trick para relações não lineares

#### Fraquezas
- Escalabilidade limitada
- Ajuste complexo
- Difícil interpretação
#### Cenários Indicados
- Bioinformática 
- Texto
- Classificação com muitas variáveis

---
### k-Nearest Neighbors (k-NN)

#### Características
Classifica observações pela proximidade entre exemplos.
#### Forças
- Simples
- Sem fase explícita de treinamento
- Flexível para fronteiras complexas

#### Fraquezas
- Predição lenta
- Sensível à escala
- Sofre com alta dimensionalidade

#### Cenários Indicados
- Sistemas pequenos
- Reconhecimento de padrões
- Problemas exploratórios

---
### Regressão Linear e Logística
#### Características
Modelos estatísticos clássicos amplamente utilizados.

#### Forças
- Altamente interpretáveis
- Simples implementação
- Excelente baseline
- Fácil explicação estatística

#### Fraquezas
- Limitados para relações complexas
- Sensíveis à multicolinearidade
- Dependem de premissas estatísticas

#### Cenários Indicados
- Modelos regulatórios
- Estudos estatísticos
- Saúde
- Finanças
- Modelos explicáveis

---
# 2. Tarefas Descritivas: Agrupamento de Dados (Clustering)

O agrupamento busca identificar subconjuntos naturais nos dados sem conhecimento prévio das classes, de modo que objetos dentro de uma mesma classe sejam mais similares entre si do que em relação a objetos de outras classes.
## Características Gerais
- **Tipo de aprendizado:** Não supervisionado
- **Necessidade de rótulos:** Não
- **Objetivo:** Descobrir estruturas ocultas
- **Principal dependência:** Métrica de similaridade/distância
## Cenários de Utilização
- Segmentação de clientes
- Agrupamento comportamental
- Bioinformática
- **Compressão de dados**
- Organização documental
- Recomendação
- Descoberta de perfis
## Pré-requisitos
- Padronização de variáveis
- Escolha adequada de distância
- Avaliação da dimensionalidade
- Tratamento de _outliers_

---
## Técnicas Comuns

### K-Means
#### Forças
- Simples
- Escalável
- Muito rápido
#### Fraquezas
- Necessita definir K
- Sensível a outliers
- Supõe clusters esféricos

#### Cenários Indicados
- Segmentação de clientes
- Dados numéricos bem comportados

---

### Clustering Hierárquico
#### Forças

- Excelente visualização
- Não exige K inicial
- Produz dendrogramas interpretáveis

#### Fraquezas
- Alto custo computacional
- Pouco escalável
- Sensível a ruídos

#### Cenários Indicados
- Estudos exploratórios
- Taxonomias
- Análises acadêmicas

---
### DBSCAN / HDBSCAN / OPTICS

#### Forças
- Detectam** formas arbitrárias**
- Identificam **ruído automaticamente**
- Muito fortes para **detecção de densidade**

#### Fraquezas
- Ajuste de parâmetros complexo
- Sensíveis à dimensionalidade
- Dificuldade com densidades heterogêneas

#### Cenários Indicados
- Geolocalização
- Fraudes
- Análise espacial
- IoT

---
### Gaussian Mixture Models (GMM)

#### Forças
- Clustering probabilístico
- Flexibilidade geométrica
- Modela incerteza

#### Fraquezas
- Sensível à inicialização
- Convergência em máximos locais
- Maior custo computacional

#### Cenários Indicados
- Segmentação probabilística
- Sistemas fuzzy
- Bioestatística

---

# 3. Mineração de Associações e Correlações

Busca descobrir padrões de coocorrência e relações frequentes entre eventos ou atributos.
## Características Gerais

- **Tipo de aprendizado:** Não supervisionado
- **Objetivo:** Descoberta de **relações frequentes**
- **Saída típica:** Regras de associação

## Cenários de Utilização

- Market Basket Analysis
- Cross-selling
- Recomendação
- Layout de lojas
- Diagnóstico de eventos simultâneos
- Navegação web

## Pré-requisitos
- Dados transacionais
- Definição de suporte e confiança
- Boa modelagem dos eventos

---
## Técnicas Comuns

### Apriori

#### Forças
- Fácil entendimento
- Forte fundamentação teórica
- Excelente para ensino

#### Fraquezas
- Muito custoso computacionalmente
- Muitas varreduras no banco
- Explosão combinatória

#### Cenários Indicados
- Bases pequenas e médias
- Estudos exploratórios

---
### FP-Growth

#### Forças
- Muito mais eficiente
- Evita geração massiva de candidatos
- Melhor escalabilidade

#### Fraquezas
- Estruturas complexas
- Alto consumo de memória em alguns cenários

#### Cenários Indicados

- Grandes varejistas
- E-commerce
- Logs massivos

---

# 4. Detecção de Anomalias (Outlier Detection)

O objetivo é identificar padrões raros, incomuns ou discrepantes em relação ao comportamento esperado.

## Características Gerais
- Pode ser supervisionado, semi-supervisionado ou não supervisionado
- Forte dependência do conceito de “normalidade”
- Muito utilizado em monitoramento contínuo

## Cenários de Utilização
- Fraudes financeiras
- Intrusão em redes
- Equipamentos industriais
- Monitoramento hospitalar
- IoT
- Cybersecurity

## Pré-requisitos
- Entendimento do comportamento normal
- Estratégia de tolerância a falso positivo
- Tratamento de desbalanceamento extremo

---

## Técnicas Comuns

### Métodos Estatísticos
#### Forças

- Forte interpretabilidade
- Base matemática sólida
#### Fraquezas
- Dependência de distribuições
- Sofrem em alta dimensionalidade

#### Cenários Indicados
- Controle estatístico
- Qualidade industrial

---
### LOF (Local Outlier Factor)

#### Forças
- Detecta anomalias locais
- Funciona bem em densidades variadas

#### Fraquezas
- Alto custo computacional
- Ajuste difícil de parâmetros

#### Cenários Indicados
- Fraudes
- Redes
- Dados espaciais

---
### Isolation Forest

#### Forças
- Muito escalável
- Excelente para grandes volumes
- Pouca necessidade de premissas estatísticas
#### Fraquezas
- Menor interpretabilidade
- Sensível à parametrização

#### Cenários Indicados
- Big Data
- Logs
- Observabilidade
- Monitoramento operacional

---
### Autoencoders

#### Forças
- Muito eficientes para padrões complexos
- Capturam estruturas não lineares

#### Fraquezas
- Exigem grande volume de dados
- Baixa interpretabilidade

#### Cenários Indicados
- Deep Learning
- Imagens
- Cybersecurity
- IoT

---
# 5. Redução de Dimensionalidade e Extração de Características

Visa reduzir a quantidade de variáveis preservando o máximo possível da informação relevante.

## Características Gerais
- Pode ser supervisionada ou não supervisionada
- Muito utilizada como pré-processamento
- Combate a maldição da dimensionalidade

## Cenários de Utilização
- Visualização de dados
- Compressão
- NLP
- Bioinformática
- Feature Engineering

## Pré-requisitos
- Correlação entre variáveis
- Necessidade de compactação
- Avaliação de perda de informação

---
## Técnicas Comuns

### PCA (Principal Component Analysis)

#### Forças
- Simples
- Muito eficiente
- Forte base estatística

#### Fraquezas
- Linear
- Baixa interpretabilidade semântica

#### Cenários Indicados
- Dados tabulares
- Pré-processamento

---
### t-SNE

#### Forças
- Excelente visualização
- Preserva vizinhanças locais

#### Fraquezas
- Alto custo computacional
- Não escalável
- Difícil reprodução

#### Cenários Indicados
- Exploração visual
- Embeddings

---
### UMAP

#### Forças
- Mais rápido que t-SNE
- Melhor preservação estrutural global

#### Fraquezas
- Sensível a hiperparâmetros

#### Cenários Indicados
- Visualização moderna
- Grandes datasets

---
# 6. Séries Temporais e Sequências

Focadas em dados dependentes do tempo e padrões sequenciais.
## Cenários de Utilização

- Forecast financeiro
- Demanda hospitalar
- IoT
- Energia
- Supply Chain

## Técnicas Comuns

### ARIMA / SARIMA

- Fortes para padrões lineares e sazonais
- Exigem estacionariedade

### Prophet

- Fácil uso
- Forte para sazonalidade de negócio
- Menos robusto em relações complexas

### LSTM / Transformers Temporais

- Capturam dependências longas
- Muito poderosos
- Alto custo computacional e baixa interpretabilidade

---
# 7. Regras Gerais para Escolha de Técnicas

## Quando priorizar interpretabilidade

- Árvores
- Regressões
- Regras de associação

## Quando priorizar performance preditiva

- Gradient Boosting
- Random Forest
- Deep Learning

## Quando os dados não possuem rótulos

- Clustering
- Associação
- Redução de dimensionalidade

## Quando há alta dimensionalidade

- SVM
- PCA
- Autoencoders

## Quando há necessidade de escalabilidade

- K-Means
- Isolation Forest
- LightGBM

## Quando existem poucos dados

- Regressões
- Árvores
- SVM

---

# Possíveis Expansões Futuras do Material

## Aspectos Teóricos

- Bias-Variance Tradeoff
- Overfitting vs Underfitting
- Maldição da dimensionalidade
- Métricas de distância
- Entropia e ganho de informação
- Regularização
- Validação cruzada

## Aspectos Práticos

- Pipeline de Machine Learning
- Engenharia de atributos
- Balanceamento de classes
- Explainable AI (XAI)
- Drift de modelos
- MLOps
- Monitoramento de performance

## Aplicações por Domínio

- Saúde
- Bancos
- Varejo
- Telecom
- Marketing Science
- Indústria
- Auditoria hospitalar
- Detecção de fraude
- Observabilidade operacional

---
# Metodologia de Projetos em Data Mining: CRISP-DM

O **CRISP-DM (Cross Industry Standard Process for Data Mining)** é uma metodologia amplamente utilizada para estruturar projetos de mineração de dados e analytics.  
Seu objetivo é organizar o ciclo analítico desde o entendimento do problema de negócio até a implantação e monitoramento das soluções analíticas.

O modelo é iterativo e incremental, permitindo revisões contínuas entre as etapas conforme novos aprendizados surgem durante o projeto.
---

# Estrutura do CRISP-DM

## 1. Business Understanding (Entendimento do Negócio)

Objetivo:
- compreender o problema organizacional;
- definir objetivos analíticos;
- estabelecer critérios de sucesso.

### Atividades comuns
- entrevistas com stakeholders;
- definição de KPIs;
- avaliação de viabilidade;
- tradução do problema de negócio em problema analítico.

### Exemplos
- reduzir churn;
- detectar fraude;
- prever ocupação hospitalar;
- segmentar clientes.

---
## 2. Data Understanding (Entendimento dos Dados)

Objetivo:
- conhecer profundamente os dados disponíveis.

### Atividades comuns
- análise exploratória;
- identificação de inconsistências;
- análise de distribuição;
- detecção de outliers;
- avaliação de qualidade.

### Técnicas frequentemente utilizadas
- estatística descritiva;
- visualização;
- clustering exploratório;
- análise de correlação.

---

## 3. Data Preparation (Preparação dos Dados)

Frequentemente a etapa mais custosa do projeto.

Objetivo:

- transformar dados brutos em dados utilizáveis.

### Atividades comuns

- limpeza;
- tratamento de missing;
- encoding;
- normalização;
- feature engineering;
- seleção de variáveis.

### Conceitos importantes

- pipeline de dados;
- redução de dimensionalidade;
- balanceamento de classes.

---

## 4. Modeling (Modelagem)

Objetivo:

- construir modelos analíticos e preditivos.

### Atividades comuns

- seleção de algoritmos;
- treinamento;
- tuning;
- validação cruzada;
- comparação de modelos.

### Técnicas típicas

- regressão;
- árvores;
- random forest;
- gradient boosting;
- clustering;
- redes neurais.

---

## 5. Evaluation (Avaliação)

Objetivo:

- verificar se o modelo realmente resolve o problema de negócio.

### Avaliações técnicas

- acurácia;
- recall;
- precisão;
- ROC-AUC;
- RMSE;
- silhouette score.

### Avaliações de negócio

- impacto operacional;
- retorno financeiro;
- interpretabilidade;
- risco.

---

## 6. Deployment (Implantação)

Objetivo:

- operacionalizar o modelo no ambiente real.

### Atividades comuns

- APIs;
- dashboards;
- automações;
- monitoramento;
- retreinamento.

### Conceitos modernos relacionados

- MLOps;
- monitoramento de drift;
- observabilidade de modelos;
- governança de IA.

---

# Características Importantes do CRISP-DM

## Processo Iterativo

Não é linear.

Frequentemente:

- problemas encontrados na modelagem exigem nova preparação;
- problemas nos dados exigem redefinição do negócio.

---

## Forte Orientação ao Negócio

O foco principal não é:

- “construir modelos sofisticados”,

mas:

- resolver problemas organizacionais reais.

---
## Independente de Tecnologia

O CRISP-DM:

- não depende de linguagem,
- ferramenta,
- framework,
- banco de dados,
- plataforma de IA.

---
# Relação do CRISP-DM com as Técnicas de Data Mining

Essa conexão é extremamente importante no seu material.

|Etapa CRISP-DM|Técnicas frequentemente associadas|
|---|---|
|Data Understanding|Estatística descritiva, visualização, clustering exploratório|
|Data Preparation|PCA, feature engineering, normalização|
|Modeling|Classificação, regressão, clustering, associação|
|Evaluation|Métricas estatísticas e validação|
|Deployment|MLOps, monitoramento, inferência|

---
# Sugestão Estratégica para o Seu Material

Seu material pode ficar ainda mais forte se dividido em:
## Parte 1 — Fundamentos e Processo

- O que é Data Mining
- CRISP-DM
- Tipos de aprendizado
- Tipos de problemas analíticos
- Pipeline analítico

---
## Parte 2 — Técnicas de Data Mining

- Classificação
- Regressão
- Clustering
- Associação
- Anomalias
- Redução de dimensionalidade
- Séries temporais

---
## Parte 3 — Aspectos Avançados

- Explainable AI
- Drift
- Ensemble Learning
- Feature Engineering
- Validação
- MLOps
- Governança

---
# Observação importante

Embora o CRISP-DM seja extremamente relevante, hoje existem complementações modernas importantes, especialmente em ambientes corporativos com IA operacionalizada:

- MLOps
- Data-Centric AI
- Model Governance
- Responsible AI
- Continuous Learning Pipelines
