---
title: "1.10. Decision Trees"
source: "https://scikit-learn.org/stable/modules/tree.html"
author:
  - "scikit-learn.org"
published:
created: 2026-06-05
description: "Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning s..."
tags:
  - "clippings"
---
## 1.10. Árvores de Decisão

**Árvores de Decisão (ADs)** são um método de aprendizado supervisionado não paramétrico usado para e . O objetivo é criar um modelo que preveja o valor de uma variável alvo aprendendo regras de decisão simples inferidas a partir das características dos dados. Uma árvore pode ser vista como uma aproximação constante por partes.

Por exemplo, no exemplo abaixo, as árvores de decisão aprendem com os dados a aproximar uma curva senoidal com um conjunto de regras de decisão do tipo "se-então-senão". Quanto mais profunda a árvore, mais complexas as regras de decisão e mais preciso o modelo.

![../_images/sphx_glr_plot_tree_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)

Algumas vantagens das árvores de decisão são:

- Fácil de entender e interpretar. As árvores podem ser visualizadas.
- Requer pouco preparo de dados. Outras técnicas geralmente exigem normalização de dados, criação de variáveis fictícias e remoção de valores em branco. Algumas combinações de árvores e algoritmos suportam .
- O custo de utilização da árvore (ou seja, de previsão de dados) é logarítmico em relação ao número de pontos de dados utilizados para treinar a árvore.
- Capaz de lidar com dados numéricos e categóricos. No entanto, a implementação do scikit-learn não suporta variáveis categóricas por enquanto. Outras técnicas geralmente são especializadas na análise de conjuntos de dados que possuem apenas um tipo de variável. Consulte a seção para obter mais informações.
- Capaz de lidar com problemas de múltiplas saídas.
- Utiliza um modelo de caixa branca. Se uma determinada situação é observável em um modelo, a explicação para a condição é facilmente explicada pela lógica booleana. Por outro lado, em um modelo de caixa preta (por exemplo, em uma rede neural artificial), os resultados podem ser mais difíceis de interpretar.
- É possível validar um modelo usando testes estatísticos. Isso permite avaliar a confiabilidade do modelo.
- Apresenta bom desempenho mesmo que suas premissas sejam, de certa forma, violadas pelo modelo verdadeiro a partir do qual os dados foram gerados.

As desvantagens das árvores de decisão incluem:

- Os algoritmos de aprendizado por árvore de decisão podem criar árvores excessivamente complexas que não generalizam bem os dados. Isso é chamado de sobreajuste (overfitting). Mecanismos como poda, definição do número mínimo de amostras necessárias em um nó folha ou definição da profundidade máxima da árvore são necessários para evitar esse problema.
- Árvores de decisão podem ser instáveis porque pequenas variações nos dados podem resultar na geração de uma árvore completamente diferente. Esse problema é atenuado pelo uso de árvores de decisão dentro de um conjunto (ensemble).
- As previsões das árvores de decisão não são suaves nem contínuas, mas sim aproximações constantes por partes, como pode ser observado na figura acima. Portanto, elas não são boas para extrapolação.
- Sabe-se que o problema de aprender uma árvore de decisão ótima é NP-completo sob diversos aspectos de otimalidade, mesmo para conceitos simples. Consequentemente, os algoritmos práticos de aprendizado de árvores de decisão são baseados em algoritmos heurísticos, como o algoritmo guloso, no qual decisões localmente ótimas são tomadas em cada nó. Tais algoritmos não garantem o retorno da árvore de decisão globalmente ótima. Isso pode ser mitigado pelo treinamento de múltiplas árvores em um aprendizado conjunto, onde as características e amostras são selecionadas aleatoriamente com reposição.
- Existem conceitos difíceis de aprender porque as árvores de decisão não os expressam facilmente, como os problemas de XOR, paridade ou multiplexação.
- Os algoritmos de aprendizado por árvore de decisão criam árvores enviesadas se algumas classes predominarem. Portanto, recomenda-se balancear o conjunto de dados antes de treiná-lo com a árvore de decisão.

## 1.10.1. Classificação

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier") é uma classe capaz de realizar classificação multiclasse em um conjunto de dados.

Assim como outros classificadores, [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier") este recebe como entrada duas matrizes: uma matriz X, esparsa ou densa, de formato n, contendo as amostras de treinamento, e uma matriz Y de valores inteiros, de formato n , contendo os rótulos de classe para as amostras de treinamento:`(n_samples, n_features)` `(n_samples,)`

```
>>> from sklearn import tree
>>> X = [[0, 0], [1, 1]]
>>> Y = [0, 1]
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, Y)
```

Após o ajuste, o modelo pode então ser usado para prever a classe das amostras:

```
>>> clf.predict([[2., 2.]])
array([1])
```

Caso existam múltiplas classes com a mesma probabilidade máxima, o classificador irá prever a classe com o menor índice dentre essas classes.

Como alternativa à saída de uma classe específica, pode-se prever a probabilidade de cada classe, que é a fração de amostras de treinamento da classe em uma folha:

```
>>> clf.predict_proba([[2., 2.]])
array([[0., 1.]])
```

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier") é capaz de classificação binária (onde os rótulos são \[-1, 1\]) e classificação multiclasse (onde os rótulos são \[0, …, K-1\]).

Utilizando o conjunto de dados Iris, podemos construir uma árvore da seguinte forma:

```
>>> from sklearn.datasets import load_iris
>>> from sklearn import tree
>>> iris = load_iris()
>>> X, y = iris.data, iris.target
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, y)
```

Após o treinamento, você pode plotar a árvore com a [`plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree") função:

```
>>> tree.plot_tree(clf)
[...]
```

![../_images/sphx_glr_plot_iris_dtc_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_002.png)

Formas alternativas de exportar árvores [#](#alternative-ways-to-export-trees "Link para este menu suspenso")

```
>>> import graphviz
>>> dot_data = tree.export_graphviz(clf, out_file=None)
>>> graph = graphviz.Source(dot_data)
>>> graph.render("iris")
```

```
>>> dot_data = tree.export_graphviz(clf, out_file=None,
...                      feature_names=iris.feature_names,
...                      class_names=iris.target_names,
...                      filled=True, rounded=True,
...                      special_characters=True)
>>> graph = graphviz.Source(dot_data)
>>> graph
```

![../_images/iris.svg](https://scikit-learn.org/stable/_images/iris.svg)

![../_images/sphx_glr_plot_iris_dtc_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_001.png)

```
>>> from sklearn.datasets import load_iris
>>> from sklearn.tree import DecisionTreeClassifier
>>> from sklearn.tree import export_text
>>> iris = load_iris()
>>> decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
>>> decision_tree = decision_tree.fit(iris.data, iris.target)
>>> r = export_text(decision_tree, feature_names=iris['feature_names'])
>>> print(r)
|--- petal width (cm) <= 0.80
|   |--- class: 0
|--- petal width (cm) >  0.80
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2
```

Exemplos

- [Trace a superfície de decisão das árvores de decisão treinadas no conjunto de dados Iris.](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#sphx-glr-auto-examples-tree-plot-iris-dtc-py)
- [Entendendo a estrutura da árvore de decisão](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)

## 1.10.2. Regressão

![../_images/sphx_glr_plot_tree_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)

Árvores de decisão também podem ser aplicadas a problemas de regressão, usando a [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") classe.

Assim como na configuração de classificação, o método de ajuste receberá como argumentos as matrizes X e y, com a diferença de que, neste caso, espera-se que y tenha valores de ponto flutuante em vez de valores inteiros:

```
>>> from sklearn import tree
>>> X = [[0, 0], [2, 2]]
>>> y = [0.5, 2.5]
>>> clf = tree.DecisionTreeRegressor()
>>> clf = clf.fit(X, y)
>>> clf.predict([[1, 1]])
array([0.5])
```

Exemplos

- [Regressão por Árvore de Decisão](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py)

## 1.10.3. Problemas de múltiplas saídas

Um problema de múltiplas saídas é um problema de aprendizado supervisionado com várias saídas a serem previstas, ou seja, quando Y é uma matriz 2D de formato .`(n_samples, n_outputs)`

Quando não há correlação entre as saídas, uma maneira muito simples de resolver esse tipo de problema é construir n modelos independentes, ou seja, um para cada saída, e então usar esses modelos para prever independentemente cada uma das n saídas. No entanto, como é provável que os valores de saída relacionados à mesma entrada sejam correlacionados, uma maneira frequentemente melhor é construir um único modelo capaz de prever simultaneamente todas as n saídas. Primeiro, isso requer menos tempo de treinamento, já que apenas um único estimador é construído. Segundo, a precisão de generalização do estimador resultante pode ser aumentada.

No que diz respeito às árvores de decisão, essa estratégia pode ser facilmente utilizada para dar suporte a problemas com múltiplas saídas. Isso requer as seguintes alterações:

- Armazene n valores de saída nas folhas, em vez de 1;
- Utilize critérios de divisão que calculem a redução média em todas as n saídas.

Este módulo oferece suporte a problemas com múltiplas saídas, implementando essa estratégia em ambos [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier") os módulos [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor"). Se uma árvore de decisão for ajustada a uma matriz de saída Y de formato n , o estimador resultante será:`(n_samples, n_outputs)`

- Exibir valores n\_output ao `predict`;
- Gere uma lista de n\_output arrays de probabilidades de classe em `predict_proba`.

O uso de árvores de múltiplas saídas para regressão é demonstrado em [Regressão por Árvore de Decisão](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py). Neste exemplo, a entrada X é um único valor real e as saídas Y são o seno e o cosseno de X.

![../_images/sphx_glr_plot_tree_regression_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_002.png)

O uso de árvores de múltiplas saídas para classificação é demonstrado em " [Completamento de faces com estimadores de múltiplas saídas"](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-auto-examples-miscellaneous-plot-multioutput-face-completion-py). Neste exemplo, as entradas X são os pixels da metade superior dos rostos e as saídas Y são os pixels da metade inferior desses rostos.

![../_images/sphx_glr_plot_multioutput_face_completion_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_001.png)

Exemplos

- [Conclusão de faces com estimadores de múltiplas saídas](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-auto-examples-miscellaneous-plot-multioutput-face-completion-py)

Referências

- M. Dumont et al, [Anotação rápida de imagens multiclasse com subjanelas aleatórias e árvores de decisão randomizadas com múltiplas saídas](https://www.montefiore.ulg.ac.be/services/stochastic/pubs/2009/DMWG09/dumont-visapp09-shortpaper.pdf), Conferência Internacional sobre Teoria e Aplicações de Visão Computacional 2009

## 1.10.4. Complexidade

A tabela a seguir mostra as estimativas de complexidade no pior caso para uma árvore binária balanceada:

| Divisor | Custo total do treinamento | Custo total de inferência |
| --- | --- | --- |
| "melhor" | $\mathcal{O} \left(\right. n_{f e a t u r e s} n_{s a m p l e s}^{2} log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right)$ | $\mathcal{O} \left(\right. log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right)$ |
| "aleatório" | $\mathcal{O} \left(\right. n_{f e a t u r e s} n_{s a m p l e s}^{2} \left.\right)$ | $\mathcal{O} \left(\right. log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right)$ |

Em geral, o custo de treinamento para construir uma árvore binária balanceada **em cada nó** é

$$
\mathcal{O} \left(\right. n_{f e a t u r e s} n_{s a m p l e s} log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right) + \mathcal{O} \left(\right. n_{f e a t u r e s} n_{s a m p l e s} \left.\right)
$$

O primeiro termo é o custo da triagem. $n_{s a m p l e s}$ repetido para $n_{f e a t u r e s}$ O segundo termo é a varredura linear sobre os pontos de divisão candidatos para encontrar a característica que oferece a maior redução no critério de impureza. Este último é subprincipal para a estratégia de divisão gulosa "melhor" e, portanto, normalmente é descartado.

Independentemente da estratégia de divisão, após somar o custo em **todos os nós internos**, a complexidade total aumenta linearmente com $n_{n o d e s} = n_{l e a v e s} - 1$ , que é $\mathcal{O} \left(\right. n_{s a m p l e s} \left.\right)$ Na complexidade do pior caso, isto é, quando a árvore cresce até que cada amostra termine em sua própria folha.

Muitas implementações, como o scikit-learn, usam técnicas eficientes de cache para manter o controle da ordem geral dos índices em cada nó, de forma que os recursos não precisem ser reordenados em cada nó; portanto, a complexidade de tempo dessas implementações é apenas O(n log n). $\mathcal{O} \left(\right. n_{f e a t u r e s} n_{s a m p l e s} log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right)$ .

O custo da inferência é independente da estratégia de divisão. Ele depende apenas da profundidade da árvore. $\mathcal{O} \left(\right. \text{depth} \left.\right)$ Em uma árvore binária aproximadamente balanceada, cada divisão reduz os dados à metade, e o número dessas reduções aumenta com a profundidade como potências de dois. Se esse processo continuar até que cada amostra esteja isolada em sua própria folha, a profundidade resultante será $\mathcal{O} \left(\right. log ⁡ \left(\right. n_{s a m p l e s} \left.\right) \left.\right)$ .

Referências

## 1.10.5. Dicas de uso prático

- Árvores de decisão tendem a sofrer de sobreajuste em dados com um grande número de atributos. Obter a proporção correta entre amostras e número de atributos é importante, visto que uma árvore com poucas amostras em um espaço de alta dimensionalidade tem grande probabilidade de sofrer de sobreajuste.
- Considere realizar uma redução de dimensionalidade ( [PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca), [ICA](https://scikit-learn.org/stable/modules/decomposition.html#ica) ou [seleção de características](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection) ) previamente para dar à sua árvore uma chance melhor de encontrar características discriminativas.
- [Compreender a estrutura da árvore de decisão](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py) ajudará a obter mais informações sobre como ela faz previsões, o que é importante para entender as características relevantes nos dados.
- Visualize sua árvore durante o treinamento usando a `export` função. Use `max_depth=3` uma profundidade inicial para ter uma ideia de como a árvore se ajusta aos seus dados e, em seguida, aumente a profundidade.
- Lembre-se de que o número de amostras necessárias para preencher a árvore dobra a cada nível adicional que a árvore atinge. Use isso `max_depth` para controlar o tamanho da árvore e evitar sobreajuste.
- Use \` `min_samples_split` n\` ou \`max\` `min_samples_leaf` para garantir que múltiplas amostras influenciem cada decisão na árvore, controlando quais divisões serão consideradas. Um número muito pequeno geralmente significa que a árvore sofrerá sobreajuste (overfitting), enquanto um número grande impedirá que a árvore aprenda com os dados. Tente \`n\` `min_samples_leaf=5` como valor inicial. Se o tamanho da amostra variar muito, um número decimal pode ser usado como porcentagem nesses dois parâmetros. Embora \` `min_samples_split` n\` possa criar folhas arbitrariamente pequenas, \` `min_samples_leaf` max\` garante que cada folha tenha um tamanho mínimo, evitando nós folha com baixa variância e sobreajuste em problemas de regressão. Para classificação com poucas classes, \` `min_samples_leaf=1` n\` costuma ser a melhor escolha.
	Note que `min_samples_split` considera as amostras diretamente e independentemente de `sample_weight`, se fornecido (por exemplo, um nó com m amostras ponderadas ainda é tratado como tendo exatamente m amostras). Considere `min_weight_fraction_leaf` ou `min_impurity_decrease` se a contabilização dos pesos das amostras for necessária nas divisões.
- Equilibre seu conjunto de dados antes do treinamento para evitar que a árvore seja tendenciosa em relação às classes dominantes. O balanceamento de classes pode ser feito amostrando um número igual de amostras de cada classe ou, preferencialmente, normalizando a soma dos pesos das amostras ( `sample_weight`) para cada classe para o mesmo valor. Observe também que critérios de pré-poda baseados em pesos, como `min_weight_fraction_leaf`, serão menos tendenciosos em relação às classes dominantes do que critérios que não levam em consideração os pesos das amostras, como `min_samples_leaf`.
- Se as amostras forem ponderadas, será mais fácil otimizar a estrutura da árvore usando critérios de pré-poda baseados em peso, como o `min_weight_fraction_leaf`, que garante que os nós folha contenham pelo menos uma fração da soma total dos pesos das amostras.
- Todas as árvores de decisão usam `np.float32` matrizes internamente. Se os dados de treinamento não estiverem nesse formato, uma cópia do conjunto de dados será criada.
- Se a matriz de entrada X for muito esparsa, recomenda-se convertê-la para esparsa `csc_matrix` antes de chamar a função \`fit\` e novamente para esparsa `csr_matrix` antes de chamar a função \`predict\`. O tempo de treinamento pode ser ordens de magnitude mais rápido para uma matriz de entrada esparsa em comparação com uma matriz densa quando as características têm valores zero na maioria das amostras.

## 1.10.6. Algoritmos de árvore: ID3, C4.5, C5.0 e CART

Quais são os vários algoritmos de árvore de decisão e como eles diferem entre si? Qual deles está implementado no scikit-learn?

scikit-learn uses an optimized version of the CART algorithm; however, the scikit-learn implementation does not support categorical variables for now.

## 1.10.7. Mathematical formulation

Given training vectors $x_{i} \in R^{n}$, i=1,…, l and a label vector $y \in R^{l}$, a decision tree recursively partitions the feature space such that the samples with the same labels or similar target values are grouped together.

Let the data at node $m$ be represented by $Q_{m}$ with $n_{m}$ samples. For each candidate split $\theta = \left(\right. j , t_{m} \left.\right)$ consisting of a feature $j$ and threshold $t_{m}$, partition the data into $Q_{m}^{l e f t} \left(\right. \theta \left.\right)$ and $Q_{m}^{r i g h t} \left(\right. \theta \left.\right)$ subsets

$$
\begin{matrix}Q_{m}^{l e f t} \left(\right. \theta \left.\right) = \left{\right. \left(\right. x , y \left.\right) \left|\right. x_{j} \leq t_{m} \left.\right} \\ Q_{m}^{r i g h t} \left(\right. \theta \left.\right) = Q_{m} \backslash Q_{m}^{l e f t} \left(\right. \theta \left.\right)\end{matrix}
$$

The quality of a candidate split of node $m$ is then computed using an impurity function or loss function $H \left(\right. \left.\right)$, the choice of which depends on the task being solved (classification or regression)

$$
G \left(\right. Q_{m} , \theta \left.\right) = \frac{n_{m}^{l e f t}}{n_{m}} H \left(\right. Q_{m}^{l e f t} \left(\right. \theta \left.\right) \left.\right) + \frac{n_{m}^{r i g h t}}{n_{m}} H \left(\right. Q_{m}^{r i g h t} \left(\right. \theta \left.\right) \left.\right)
$$

Select the parameters that minimises the impurity

$$
\theta^{*} = argmin_{\theta} G \left(\right. Q_{m} , \theta \left.\right)
$$

The strategy to choose the split at each node is controlled by the `splitter` parameter:

- With the **best splitter** (default, `splitter='best'`), $\theta^{*}$ is found by performing a **greedy exhaustive search** over all available features and all possible thresholds $t_{m}$ (i.e. midpoints between sorted, distinct feature values), selecting the pair that exactly minimizes $G \left(\right. Q_{m} , \theta \left.\right)$.
- With the **random splitter** (`splitter='random'`), $\theta^{*}$ is found by sampling a **single random candidate threshold** for each available feature. This performs a stochastic approximation of the greedy search, effectively reducing computation time (see ).

After choosing the optimal split $\theta^{*}$ at node $m$, the same splitting procedure is then applied recursively to each partition $Q_{m}^{l e f t} \left(\right. \theta^{*} \left.\right)$ and $Q_{m}^{r i g h t} \left(\right. \theta^{*} \left.\right)$ until a stopping condition is reached, such as:

- the maximum allowable depth is reached (`max_depth`);
- $n_{m}$ is smaller than `min_samples_split`;
- the impurity decrease for this split is smaller than `min_impurity_decrease`.

See the respective estimator docstring for other stopping conditions.

### 1.10.7.1. Classification criteria

If a target is a classification outcome taking on values 0,1,…,K-1, for node $m$, let

$$
p_{m k} = \frac{1}{n_{m}} \underset{y \in Q_{m}}{\sum} I \left(\right. y = k \left.\right)
$$

be the proportion of class k observations in node $m$. If $m$ is a terminal node, `predict_proba` for this region is set to $p_{m k}$. Common measures of impurity are the following.

Gini:

$$
H \left(\right. Q_{m} \left.\right) = \underset{k}{\sum} p_{m k} \left(\right. 1 - p_{m k} \left.\right)
$$

Log Loss or Entropy:

$$
H \left(\right. Q_{m} \left.\right) = - \underset{k}{\sum} p_{m k} log ⁡ \left(\right. p_{m k} \left.\right)
$$

### 1.10.7.2. Regression criteria

If the target is a continuous value, then for node $m$, common criteria to minimize as for determining locations for future splits are Mean Squared Error (MSE or L2 error), Poisson deviance as well as Mean Absolute Error (MAE or L1 error). MSE and Poisson deviance both set the predicted value of terminal nodes to the learned mean value $\bar{y}_{m}$ of the node whereas the MAE sets the predicted value of terminal nodes to the median $m e d i a n \left(\right. y \left.\right)_{m}$.

Mean Squared Error:

$$
\begin{matrix}\bar{y}_{m} = \frac{1}{n_{m}} \underset{y \in Q_{m}}{\sum} y \\ H \left(\right. Q_{m} \left.\right) = \frac{1}{n_{m}} \underset{y \in Q_{m}}{\sum} \left(\right. y - \bar{y}_{m} \left.\right)^{2}\end{matrix}
$$

Mean Poisson deviance:

$$
H \left(\right. Q_{m} \left.\right) = \frac{2}{n_{m}} \underset{y \in Q_{m}}{\sum} \left(\right. y log ⁡ \frac{y}{\bar{y}_{m}} - y + \bar{y}_{m} \left.\right)
$$

Setting `criterion="poisson"` might be a good choice if your target is a count or a frequency (count per some unit). In any case, $y >= 0$ is a necessary condition to use this criterion. For performance reasons the actual implementation minimizes the half mean poisson deviance, i.e. the mean poisson deviance divided by 2.

Mean Absolute Error:

$$
\begin{matrix}m e d i a n \left(\right. y \left.\right)_{m} = \underset{y \in Q_{m}}{median} \left(\right. y \left.\right) \\ H \left(\right. Q_{m} \left.\right) = \frac{1}{n_{m}} \underset{y \in Q_{m}}{\sum} \left|\right. y - m e d i a n \left(\right. y \left.\right)_{m} \left|\right.\end{matrix}
$$

Note that it is 3–6× slower to fit than the MSE criterion as of version 1.8.

## 1.10.8. Missing Values Support

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier"), [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") have built-in support for missing values using `splitter='best'`, where the splits are determined in a greedy fashion. [`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier"), and [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor") have built-in support for missing values for `splitter='random'`, where the splits are determined randomly. For more details on how the splitter differs on non-missing values, see the [Forest section](https://scikit-learn.org/stable/modules/ensemble.html#forest).

First we will describe how [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier"), [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") handle missing-values in the data.

For each potential threshold on the non-missing data, the splitter will evaluate the split with all the missing values going to the left node or the right node.

Decisions are made as follows:

- By default when predicting, the samples with missing values are classified with the class used in the split found during training:
	```
	>>> from sklearn.tree import DecisionTreeClassifier
	>>> import numpy as np
	>>> X = np.array([0, 1, 6, np.nan]).reshape(-1, 1)
	>>> y = [0, 0, 1, 1]
	>>> tree = DecisionTreeClassifier(random_state=0).fit(X, y)
	>>> tree.predict(X)
	array([0, 0, 1, 1])
	```
- If the criterion evaluation is the same for both nodes, then the tie for missing value at predict time is broken by going to the right node. The splitter also checks the split where all the missing values go to one child and non-missing values go to the other:
	```
	>>> from sklearn.tree import DecisionTreeClassifier
	>>> import numpy as np
	>>> X = np.array([np.nan, -1, np.nan, 1]).reshape(-1, 1)
	>>> y = [0, 0, 1, 1]
	>>> tree = DecisionTreeClassifier(random_state=0, max_depth=1).fit(X, y)
	>>> X_test = np.array([np.nan]).reshape(-1, 1)
	>>> tree.predict(X_test)
	array([1])
	```
- If no missing values are seen during training for a given feature, then during prediction missing values are mapped to the child with the most samples:
	```
	>>> from sklearn.tree import DecisionTreeClassifier
	>>> import numpy as np
	>>> X = np.array([0, 1, 2, 3]).reshape(-1, 1)
	>>> y = [0, 1, 1, 1]
	>>> tree = DecisionTreeClassifier(random_state=0).fit(X, y)
	>>> X_test = np.array([np.nan]).reshape(-1, 1)
	>>> tree.predict(X_test)
	array([1])
	```

[`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier"), and [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor") handle missing values in a slightly different way. When splitting a node, a random threshold will be chosen to split the non-missing values on. Then the non-missing values will be sent to the left and right child based on the randomly selected threshold, while the missing values will also be randomly sent to the left or right child. This is repeated for every feature considered at each split. The best split among these is chosen.

Durante a previsão, o tratamento de valores ausentes é o mesmo que o da árvore de decisão:

- Por padrão, ao realizar previsões, as amostras com valores ausentes são classificadas com a classe usada na divisão encontrada durante o treinamento.
- Se nenhum valor ausente for observado durante o treinamento para uma determinada característica, então, durante a predição, os valores ausentes serão mapeados para o filho com o maior número de amostras.

## 1.10.9. Poda de Complexidade de Custo Mínimo

A poda de custo-complexidade mínimo é um algoritmo usado para podar uma árvore a fim de evitar sobreajuste, descrito no Capítulo 3 de . Este algoritmo é parametrizado por $\alpha \geq 0$ conhecido como parâmetro de complexidade. O parâmetro de complexidade é usado para definir a medida de custo-complexidade. $R_{\alpha} \left(\right. T \left.\right)$ de uma determinada árvore $T$ :

$$
R_{\alpha} \left(\right. T \left.\right) = R \left(\right. T \left.\right) + \alpha \left|\right. \overset{\sim}{T} \left|\right.
$$

onde $\left|\right. \overset{\sim}{T} \left|\right.$ é o número de nós terminais em $T$ e $R \left(\right. T \left.\right)$ é tradicionalmente definida como a taxa total de classificação incorreta dos nós terminais. Alternativamente, o scikit-learn usa a impureza ponderada total da amostra dos nós terminais para $R \left(\right. T \left.\right)$ Como mostrado acima, a impureza de um nó depende do critério. A poda de custo-complexidade mínimo encontra a subárvore de $T$ que minimiza $R_{\alpha} \left(\right. T \left.\right)$ .

A medida de complexidade de custo de um único nó é $R_{\alpha} \left(\right. t \left.\right) = R \left(\right. t \left.\right) + \alpha$ O ramo, $T_{t}$ , é definida como uma árvore onde o nó $t$ é a sua raiz. Em geral, a impureza de um nó é maior que a soma das impurezas de seus nós terminais. $R \left(\right. T_{t} \left.\right) < R \left(\right. t \left.\right)$ No entanto, a medida de complexidade de custo de um nó, $t$ , e sua filial, $T_{t}$ , pode ser igual dependendo de $\alpha$ Definimos o efetivo $\alpha$ de um nó ser o valor onde eles são iguais, $R_{\alpha} \left(\right. T_{t} \left.\right) = R_{\alpha} \left(\right. t \left.\right)$ ou $\alpha_{e f f} \left(\right. t \left.\right) = \frac{R \left(\right. t \left.\right) - R \left(\right. T_{t} \left.\right)}{\left|\right. T \left|\right. - 1}$ Um nó não terminal com o menor valor de $\alpha_{e f f}$ é o elo mais fraco e será podado. Esse processo termina quando a árvore podada atingir o mínimo necessário. $\alpha_{e f f}$ é maior que o `ccp_alpha` parâmetro.

Exemplos

- [Árvores de decisão pós-poda com poda de complexidade de custo](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)

Referências

- [https://en.wikipedia.org/wiki/Decision\_tree\_learning](https://en.wikipedia.org/wiki/Decision_tree_learning)
- [https://en.wikipedia.org/wiki/Predictive\_analytics](https://en.wikipedia.org/wiki/Predictive_analytics)
- JR Quinlan. C4. 5: programas para aprendizado de máquina. Morgan Kaufmann, 1993.
- T. Hastie, R. Tibshirani e J. Friedman. Elementos de Aprendizagem Estatística, Springer, 2009.