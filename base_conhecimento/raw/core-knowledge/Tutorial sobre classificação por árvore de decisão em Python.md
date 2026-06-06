---
title: "Tutorial sobre classificação por árvore de decisão em Python"
source: "https://www.datacamp.com/pt/tutorial/decision-tree-classification-python"
author:
  - "[[Avinash Navlani]]"
published: 2026-01-14
created: 2026-06-05
description: "Aprenda a classificação de árvores de decisão em Python com o Scikit-Learn. Crie, visualize e otimize modelos para marketing, finanças e outras aplicações."
tags:
  - "clippings"
---
## Criação de classificador de árvore de decisão no Scikit-learn

### Importando as bibliotecas necessárias

Vamos primeiro carregar as bibliotecas necessárias.

```python
# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
Executar código Powered By Esse assistente de IA foi útil?
```

### Carregando dados

Vamos primeiro carregar o conjunto de dados necessário sobre diabetes entre os índios Pima usando a função de leitura de CSV do pandas. Você pode baixar o [conjunto de dados do Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database) para acompanhar.

```python
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("diabetes.csv", header=None, names=col_names)
Executar código Powered By Esse assistente de IA foi útil?
```
```python
pima.head()
Executar código Powered By Esse assistente de IA foi útil?
```

|  | grávida | glucose | bp | pele | insulina | bmi | linhagem | idade | rótulo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 6 | 148 | 72 | 35 | 0 | 33,6 | 0,627 | 50 | 1 |
| 1 | 1 | 85 | 66 | 29 | 0 | 26,6 | 0,351 | 31 | 0 |
| 2 | 8 | 183 | 64 | 0 | 0 | 23,3 | 0,672 | 32 | 1 |
| 3 | 1 | 89 | 66 | 23 | 94 | 28,1 | 0,167 | 21 | 0 |
| 4 | 0 | 137 | 40 | 35 | 168 | 43,1 | 2.288 | 33 | 1 |

### Seleção de recursos

Aqui, você precisa dividir as colunas fornecidas em dois tipos de variáveis: variáveis dependentes (ou variáveis-alvo) e variáveis independentes (ou variáveis características).

```python
#split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] # Features
y = pima.label # Target variable
Executar código Powered By Esse assistente de IA foi útil?
```

### Dividindo dados

Pra entender o desempenho do modelo, uma boa estratégia é dividir o conjunto de dados em um conjunto de treinamento e um conjunto de teste.

Vamos dividir o conjunto de dados usando a função \` `train_test_split()` \`. Você precisa passar três parâmetros: características, tamanho do conjunto de dados de destino e tamanho do conjunto de dados de teste.

```python
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
Executar código Powered By Esse assistente de IA foi útil?
```

### Criando um modelo de árvore de decisão

Vamos criar um modelo de árvore de decisão usando o Scikit-learn.

```python
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
Executar código Powered By Esse assistente de IA foi útil?
```

### Avaliando o modelo

Vamos ver com que precisão o classificador ou modelo consegue prever o tipo de cultivares.

A precisão pode ser calculada comparando os valores reais do conjunto de testes com os valores previstos.

```python
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
Executar código Powered By Esse assistente de IA foi útil?
```
```javascript
Accuracy: 0.6753246753246753
Executar código Powered By Esse assistente de IA foi útil?
```

Conseguimos uma taxa de classificação de 67,53%, o que é considerado uma boa precisão. Você pode melhorar essa precisão ajustando os parâmetros no algoritmo da árvore de decisão.

## Visualizando árvores de decisão

Você pode usar a função \` `export_graphviz()` \` do Scikit-learn para mostrar a árvore dentro de um notebook Jupyter. Para desenhar a árvore, você também precisa instalar `graphviz` e `pydotplus`.

```python
pip install graphviz
pip install pydotplusPowered By
```

A função `export_graphviz()` transforma o classificador da árvore de decisão em um arquivo dot, e o pydotplus transforma esse arquivo dot em PNG ou em um formato que dá pra ver no Jupyter.

```python
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())Powered By
```

![Visualizando árvores de decisão](https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1545933329/output_57_0_livyu1.png)

No gráfico da árvore de decisão, cada nó interno tem uma regra de decisão que divide os dados. O Gini, também chamado de índice de Gini, mede a impureza do nó. Dá pra dizer que um nó é puro quando todos os seus registros são da mesma classe. Esses nós são conhecidos como nós folha.

Aqui, a árvore resultante não foi podada. Essa árvore sem poda é inexplicável e difícil de entender. Na próxima seção, vamos otimizar isso com a poda.

## Otimizando o desempenho da árvore de decisão

- **critério: opcional (padrão = “gini”) ou Escolha a medida de seleção de atributos.** Esse parâmetro permite usar a medida de seleção de atributos diferentes-diferentes. Os critérios suportados são “gini” para o índice de Gini e “entropia” para o ganho de informação.
- **divisor: string, opcional (padrão = “melhor”) ou Estratégia de Divisão.** Esse parâmetro permite escolher a estratégia de divisão. As estratégias suportadas são “melhor” para escolher a melhor divisão e “aleatória” para escolher a melhor divisão aleatória.
- **max\_depth: int ou None, opcional (padrão=None) ou Profundidade máxima de uma árvore.** A profundidade máxima da árvore. Se for None, os nós são expandidos até que todas as folhas tenham menos que min\_samples\_split amostras. Um valor mais alto de profundidade máxima faz com que o modelo se ajuste demais, e um valor mais baixo faz com que ele se ajuste de menos ([Fonte](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)).

No Scikit-learn, a otimização do classificador de árvore de decisão é feita só com pré-poda. A profundidade máxima da árvore pode ser usada como uma variável de controle para o pré-podar. No exemplo a seguir, você pode traçar uma árvore de decisão com os mesmos dados usando max\_depth=3. Além dos parâmetros de pré-poda, você também pode tentar outras medidas de seleção de atributos, como a entropia.

```python
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
Accuracy: 0.7705627705627706Powered By
```

Bem, a taxa de classificação aumentou para 77,05%, o que é uma precisão melhor do que o modelo anterior.

Vamos deixar nossa árvore de decisão um pouco mais fácil de entender usando o seguinte código:

```python
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, 
                filled=True, 
                rounded=True, 
                special_characters=True, 
                feature_names=feature_cols,
                class_names=['0','1'])

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())Powered By
```

Aqui, fizemos o seguinte:

- Importou as bibliotecas necessárias.
- Criei um objeto `StringIO` chamado `dot_data` para guardar a representação textual da árvore de decisão.
- Exportou a árvore de decisão para o formato `dot` usando a função `export_graphviz` e gravou a saída no buffer `dot_data`.
- Criou um objeto gráfico `pydotplus` a partir da representação no formato `dot` da árvore de decisão armazenada no buffer `dot_data`.
- Escreva o gráfico gerado em um arquivo PNG chamado “diabetes.png”.
- Mostrou a imagem PNG gerada da árvore de decisão usando o objeto `Image` do módulo `IPython.display`.

Como você pode ver, esse modelo simplificado é menos complicado, mais fácil de explicar e entender do que o gráfico anterior da árvore de decisão.

## Prós e contras da árvore de decisão

Agora que você criou e otimizou um classificador de árvore de decisão, vamos dar uma pausa para avaliar alguns dos pontos fortes e limitações do algoritmo de forma mais geral. Entender as vantagens e desvantagens ajuda você a decidir quando as árvores de decisão são a escolha certa.

| Vantagens | Desvantagens |
| --- | --- |
| Fácil de entender e visualizar | Sensível a dados ruidosos e pode sobreajustar |
| Pode capturar facilmente padrões não lineares | Pequenas variações nos dados podem resultar em árvores muito diferentes. |
| Precisa de um pré-processamento mínimo dos dados (não precisa normalizar as colunas) | Viciado com conjuntos de dados desequilibrados (recomenda-se o equilíbrio) |
| Útil para engenharia de recursos (previsão de valores ausentes, seleção de variáveis) |  |
| Sem suposições sobre a distribuição dos dados (não paramétrica) |  |

Vale lembrar que algumas desvantagens, como a instabilidade da variância, podem ser amenizadas com métodos de conjunto, como algoritmos [de bagging](https://www.datacamp.com/pt/tutorial/what-bagging-in-machine-learning-a-guide-with-examples) e [boosting](https://www.datacamp.com/pt/tutorial/what-is-boosting).

## Árvore de decisão vs. Decisão difícil

Embora tenhamos trabalhado com árvores de decisão completas ao longo deste tutorial, vale a pena entender uma variante mais simples chamada tronco de decisão. Um tronco de decisão é basicamente uma árvore de decisão com profundidade máxima de um, ou seja, tem só uma divisão no nó raiz e dois nós folha.

| Aspecto | Árvore de decisão | Decisão difícil |
| --- | --- | --- |
| **Profundidade** | Pode ter qualquer profundidade (controlada por `max_depth` parâmetro) | Sempre profundidade de 1 (apenas uma divisão) |
| **Complexidade** | Pode modelar relações complexas e não lineares | Modelos apenas com limites de decisão simples e lineares |
| **Caso de uso** | Classificador independente para problemas complexos | Usado principalmente como um aluno fraco em métodos de conjunto |
| **Precisão** | Geralmente maior precisão como modelo independente | Precisão menor, mas eficaz quando combinado |
| **Interpretabilidade** | Diminui com a profundidade (como vimos com nossa árvore não podada) | Super simples e fácil de entender |

Os troncos de decisão raramente são usados como classificadores independentes por causa da sua simplicidade. Mas eles podem ter um papel nos métodos de conjunto, especialmente [o AdaBoost](https://www.datacamp.com/pt/tutorial/adaboost-classifier-python) usa stumps de decisão como aprendizes fracos que são combinados para criar um classificador forte, ou [reforço de gradiente](https://www.datacamp.com/pt/tutorial/guide-to-the-gradient-boosting-algorithm), porque os stumps podem ser usados como aprendizes básicos no processo de reforço.

Você pode criar um stump de decisão no Scikit-learn simplesmente definindo um `max_depth=1`:

```python
# Create a Decision Stump
stump = DecisionTreeClassifier(max_depth=1)
stump = stump.fit(X_train, y_train)Powered By
```

## Conclusão

Neste tutorial, você aprendeu vários detalhes sobre árvores de decisão: como elas funcionam, medidas de seleção de atributos como ganho de informação, taxa de ganho e índice de Gini, construção de modelos de árvores de decisão, visualização e avaliação de um conjunto de dados sobre diabetes usando o pacote Scikit-learn do Python. Também falamos sobre os prós, contras e como melhorar o desempenho da árvore de decisão usando o ajuste de parâmetros.
