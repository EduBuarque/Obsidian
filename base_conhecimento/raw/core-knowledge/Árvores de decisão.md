---
title: "árvores de decisão"
source: "https://vinizinho.net/temp/dt"
author:
  - "Vinícius"
published:
created: 2026-06-05
description:
tags:
  - "clippings"
---
## Árvores de decisão: um apanhado geral

## Objetivo

Um apanhado geral do uso de árvores de decisão no campo de aprendizado de máquina. Quais são os modelos que existem, como eles se diferenciam, vantagens e desvantagens de cada um deles, quais os mais populares.

## Introdução

Uma árvore de decisão é uma estrutura muito similar a um fluxograma no qual você entra com um dado e sai com alguma predição do mesmo. Por exemplo, se quisermos decidir o meio de transporte para chegar no trabalho (a pé ou de ônibus), podemos utilizar a seguinte árvore de decisão:

{ width=400px }

Em aprendizado de máquina, estamos interessados em **como construir boas árvores de decisão**. Uma árvore de decisão *boa* é uma que toma decisões corretamente: ela ao mesmo tempo se aproxima corretamente dos dados que viu, quanto generaliza bem o que aprendeu para acertar dados que não viu.

Existem muitos tipos de árvores de decisão, e não é óbvio o que isso significa. Quando falamos de "tipos diferentes de árvores de decisão", em geral estamos falando de:

- Algoritmos diferentes para construir árvores a partir de um conjunto de dados;
- Modelos cujas árvores apresentam estruturas internas distintas;
	- Por exemplo, certos algoritmos constróem apenas árvores binárias, enquanto outros não possuem essa limitação;
- Modelos que juntam diversas árvores de uma vez só;
	- Pode-se argumentar que isso não entra no campo de *decision tree learning*, mas sim no campo de *ensemble learning*.

Observação importante: o problema de construir a árvore de decisão que melhor particiona um conjunto de dados é um problema de otimização. Porém, esse problema é NP-completo, então em geral esses algoritmos de construção de árvores são heurísticas gulosas que tentam tomar decisões localmente ótimas (ao invés de globalmente ótimas).

## Lista de modelos

Segue uma lista não-exaustiva dos modelos mais populares de aprendizado de máquina que constroem árvores de decisão únicas:

- AID (*Automatic Interaction Detection*)
	- O primeiro algoritmo de construção de árvores, proposto por Sonquist et al. em 1971.
		- Era bastante suscetível a *overfitting*, e funcionava apenas pra regressão. O algoritmo THAID (*THeta Automatic Interaction Detection*) foi proposto por Messenger & Mandell em 1972 e estende essas ideias pra classificação.
		- Não recebeu muita atenção na época.
- CHAID (*CHi-squared Automatic Interaction Detection*)
	- Proposto por Gordon Kass em 1980. Originalmente era apenas de classificação mas depois foi estendido pra regressão.
		- Dava uma atenção especial a dados faltantes. Por exemplo, se a variável for categórica, é criado um filho apenas pra possibilidade dela estar faltando. Se ela for numérica, são criados 10 filhos (um para cada intervalo), e um 11º pra possibilidade dela estar faltando.
		- Após a construção inicial da árvore, conjuntos de nós irmãos são considerados para mesclagem de acordo com testes de significância estatística (com correção de Bonferroni). Depois, eles são considerados para separação de novo utilizando um método similar.
- CART (*Classification and Regression Trees*)
	- O nome é confuso porque parece que é o nome da área (árvores de decisão para classificação e regressão), mas na verdade também é usado pra se referir a um algoritmo específico proposto por Breiman et al. em 1984.
		- Foi o primeiro algoritmo de árvores de decisão a realmente ganhar atenção. Ele introduziu o uso de *pruning* e splits multivariados. Pra lidar com dados faltantes, utiliza *surrogate splits* (preenche o dado faltante utilizando a média dos dados presentes).
- ID3 (*Iterative Dichotomiser 3*)
	- Algoritmo simples para construção de árvores proposto por Quinlan em 1986.
		- Constrói rapidamente árvores curtas, mas não lida bem com variáveis numéricas e valores faltantes, e também não faz nenhum *pruning*.
- C4.5:
	- Algoritmo de construção de árvores proposto por Quinlan em 1993, para ser o sucessor direto do ID3, corrigindo algumas de suas falhas.
		- Apresenta tratamento de dados faltantes e *pruning*. O critério de divisão em cada nó utiliza uma métrica chamada *gain ratio* que é baseada em entropia.
		- O algoritmo se tornou bem popular por apresentar boa acurácia e rapidez na maior parte dos casos.
- FACT (*Fast and Accurate Classification Tree*)
	- Proposto por Loh & Vanichsetakul em 1988.
		- Não apresenta *variable selection bias* (ver subseção seguinte) para variáveis categóricas, mas apresenta pra numéricas.
- QUEST (*Quick, Unbiased and Efficient Statistical Tree*)
	- Proposto por Loh & Shih em 1997.
		- Não apresenta *variable selection bias* pra nenhum tipo de variável. Apresenta *pruning* e é mais rápido do que o CART quando as variáveis categóricas apresentam muitos valores distintos.
		- Só gera árvores binárias.
- CRUISE (*Classification Rule with Unbiased Interaction Selection and Estimation*)
	- Proposto por Kim & Loh em 2001.
		- Sucessor ao QUEST, corrigindo algumas de suas falhas. A árvore não precisa ser necessariamente binária, de modo que um nó correspondente a uma variável categórica possui um filho para cada valor possível dessa variável. Isso reduz o tamanho da árvore e torna ela mais interpretável.
		- O algoritmo também elimina um viés que o CART apresenta: a tendência a selecionar variáveis com mais dados faltantes e variáveis *surrogate* com menos valores faltantes. Em particular, o CRUISE utiliza a média/moda para imputar os valores faltantes.
- GUIDE (*Generalized, Unbiased, Interaction Detection and Estimation*)
	- Proposto por Loh em 2009.
		- Sucessor do QUEST e do CRUISE. O CRUISE possui certo viés na forma de escolher variáveis usando testes de interação (Loh, 2014), e o GUIDE corrige isso, fazendo também um teste de interação mais elaborado.
		- O GUIDE também faz *splits* bivariados, atribui dados faltantes a uma categoria " *missing* ", produz um ranking de importância pras variáveis, e pode produzir ensembles usando *bagging* e *random forest*.

Em seguida, os algoritmos mais populares para construção de *ensembles* de árvores, ao invés de árvores únicas:

- AdaBoost (*Adaptive Boosting*)
	- Introduzido por Freund e Schapire em 1996/7.
		- É um modelo de *ensemble* que pode ser usado com qualquer classificador, mas frequentemente é usado com árvores de decisão.
		- A ideia básica é: treinamos uma árvore de decisão num conjunto de dados, e observamos quais erros ela cometeu. Em seguida, treinamos outra árvore, mas damos maior peso aos dados mal-classificados pela árvore anterior. No fim das contas, isso produz uma floresta em que nenhuma árvore é boa em tudo, mas elas são boas em coisas diferentes. A predição é feita através de uma votação ponderada, em que o peso de uma árvore é dado pela sua acurácia no conjunto de validação.
		- Uma questão importante envolve a capacidade de *boosting* dar *overfit*.
		- Em (Dietterich, 2000), é apresentado que o AdaBoost normalmente produz os melhores resultados quando não há muito ruído, mas apresenta grande capacidade para *overfit* quando o ruído é alto. A explicação é que o AdaBoost atribui maior peso aos erros de classificação, e esses erros podem ser simplesmente *outliers* causados por ruído. De certa forma, o modelo está explicitamente tentando se ajustar ao ruído.
				- Contudo, na prática esse *overfit* raramente ocorre. Diversas respostas são dadas mas nenhuma definitiva, até onde pude entender não é algo muito bem compreendido na literatura. Essa robustez observada empiricamente é um dos motivos pelos quais métodos de *boosting* são tão populares.
- RF (*Random Forest*)
	- Proposto por Breiman em 2001.
		- É um modelo de *ensemble* que usa árvores de decisão pra fazer predições mais acuradas. A ideia é que uma árvore isolada possui alta taxa de overfit (isto é, pouco viés mas altíssima variância), mas diversas árvores juntas podem acabar reduzindo essa variância se forem independentes (da forma como entendo, em um esquema próximo a aproximações de Monte Carlo).
		- O treinamento de uma RF envolve duas aleatoriedades: (1) cada árvore é treinada num conjunto de dados diferente (*bagging*), e (2) cada árvore tem acesso a um subconjunto aleatório das variáveis disponíveis no problema.
		- Por ser uma *ensemble*, há uma perda inerente de interpretabilidade no uso de RF quando comparado a árvores isoladas. Porém, ainda é possível ter uma noção da importância de cada uma das variáveis: pra cada dado no conjunto de validação, mudamos o valor da $i$-ésima variável e vemos que resposta a RF dá para essa versão modificada. Se a resposta for idêntica à do dado original, então a $i$-ésima variável aparentemente não teve impacto algum! Fazemos isso para todos os dados e com isso temos uma noção da importância da $i$-ésima variável.
		- É um modelo de aprendizado de máquina muito popular. Pode ser facilmente paralelizado (porque as árvores são independentes), o que o torna bem rápido.
- *Gradient Boosting*
	- Introduzido por Friedman em 2000/1, como uma generalização do AdaBoost.
		- A ideia é muito similar ao AdaBoost: a $m$-ésima árvore tenta focar nos erros da $(m-1)$-ésima árvore. A diferença está em *como* este enfoque é feito. Ao invés de aplicarmos pesos às amostras, fazemos a $m$-ésima árvore dar *fit* na diferença entre a resposta desejada e a resposta da *ensemble* até então.
		- Por exemplo, se para o conjunto de dados $(x\_1, x\_2, x\_3)$ temos as respostas $(y\_1 = 0.1, y\_2=2.3, y\_3=4)$, e o modelo produziu $(\\hat{y\_1} = 0.2, \\hat{y\_2} = 0.7, \\hat{y\_3} = 2.1)$, então a nova árvore tentará se ajustar a distribuição $(0.1, -1.6, -1.9)$. É daí que vem o nome *Gradient Boosting*: as árvores miram no residual/diferença/gradiente do modelo.
		- O *Gradient Boosting* é uma generalização do AdaBoost e pode ser usado com qualquer função de perda que seja diferenciável. Por conta disso ele é bem poderoso, pois podemos escolher uma função de perda que seja mais robusta a *outliers* por exemplo, e assim reduzimos as chances de *overfit*.
- XGBoost (*eXtreme Gradient Boosting*)
- Outras menções: LightGBM, pGBRT

Alguns paradigmas alternativos:

- Incremental Decision Trees
	- Todos os algoritmos discutidos anteriormente apresentam treinamento *offline*, ou seja, eles constroem árvores com base num conjunto de dados estático que não é passível de alteração; caso um novo dado seja obtido, será necessário re-treinar todas as árvores para atualizá-las. Em certos contextos isso é indesejado, e portanto há necessidade de algoritmos *online*, que sejam capazes de lidar com chegadas constantes de novas observações.
		- A classe de algoritmos que cria árvores de decisão *online* é normalmente chamada de ODTs (*Online Decision Trees*) ou de *Incremental Decision Trees*. Existem diversos algoritmos nessa classe, mas dentre os mais utilizados, destacam-se o VFDT (*Very Fast Decision Trees*) (Domingos & Hulten, 2000) e o ITI (*Incremental Tree Induction*, (Utgoff et al., 1997))
- ADTrees (*Alternating Decision Trees*)
	- O conceito de ADTrees foi proposto por Freund e Mason em 1999. O propósito seria combinar árvores de decisão e *boosting* de uma forma a reproduzir o sucesso do AdaBoost, porém construindo uma única árvore (e portanto, mantendo a interpretabilidade). Para isso, foi desenvolvido um novo tipo de árvore de decisão (chamada de *alternating*) que acaba visitando diversas folhas durante a predição, e soma o resultado de cada uma delas.
		- Os resultados do paper original indicam que ADTrees são tão boas quanto outros algoritmos de *boosting* com árvores de decisão, ao mesmo tempo sendo mais interpretáveis do que métodos de *ensemble*.

## Comparações

Em que dimensões os algoritmos variam entre si?

### Regras de avaliação de variáveis

Grande parte das árvores são construídas de forma gulosa: ao criar um novo nó (um novo *split*), todas as variáveis são consideradas e escolhe-se aquela que melhor divide os dados observados de acordo com alguma métrica. Essa métrica usualmente varia de algoritmo pra algoritmo.

- AID: somatório dos desvios quadrados
- CHAID: seleciona a variável com maior estatística de teste $\\chi^2$.
- CART: *Gini impurity*
- ID3: *information gain* (também chamado de *mutual information*)
- C4.5: *gain ratio*
	- Tenta resolver o *variable selection bias* do *information gain*. Depois foram publicados estudos que mostram que ele também é similarmente enviesado, de uma forma mais sutil.
- FACT: usa testes ANOVA e aplica LDA na variável mais significativa
- QUEST: teste $\\chi^2$ pra variáveis categóricas e ANOVA pra numéricas
- CRUISE: teste $\\chi^2$

### Pruning

Árvores isoladas sempre tiveram um problema com *overfitting*: quanto maior a árvore, maior a possibilidade de cada folha representar um único dado do conjunto de treinamento. Uma das técnicas utilizadas pra impedir que isso ocorra é o *pruning*, ou poda: basicamente, reduzir o tamanho da árvore.

*Pruning* é dividido em dois tipos: *pre-pruning* e *post-pruning* (também chamados de *no pruning* e *pruning*. Eu sei, é complicado). O *pre-pruning* tenta estabelecer algumas regras pra delimitar o tamanho da árvore: não cresça a árvore além de uma determinada altura, por exemplo. Já o *post-pruning* envolve deixar a árvore ficar bem grande, e depois aplicar algum algoritmo pra cortar sub-árvores que não contribuem significativamente pra acurácia de generalização.

A ideia é que o *post-pruning* é melhor do que o *pre-pruning* porque ele compensa a suboptimalidade da indução gulosa: é melhor deixar a árvore ser construída completamente e depois a gente corta ela do que tentar fazer isso de forma prematura. O *pruning* funciona, de certa forma, como um *lookahead*.

- AID: sem *pruning*
- CHAID: sem *pruning*
- CART: *cost-complexity pruning*
	- Foi o primeiro algoritmo a apresentar *pruning*, em especial o que se chamou de *cost-complexity pruning*. Uma sequência de árvores é construída a partir da árvore inicial e escolhe-se a árvore que apresenta maior métrica *cost-complexity* (basicamente, testa as árvores num conjunto de validação e pega as com melhor acurácia, mas penalizando árvores maiores).
- ID3: sem *pruning*
- C4.5: *pruning* baseado em significância estatística
- FACT: *cost-complexity pruning*
- QUEST: *cost-complexity pruning*
- CRUISE: *cost-complexity pruning*

### Variable selection bias

Diversos dos algoritmos de construção de árvores apresentados acima são enviesados em relação a seleção de variáveis. Em particular, na hora de escolher qual variável será empregada em um certo nó da árvore, elas tendem a escolher variáveis que apresentam muitas categorias diferentes (tanto variáveis categóricas quanto variáveis numéricas que possuem muitas possibilidades de *cutoff*). Isso é chamado de *variable selection bias* e é impactante devido à forma sequencial com a qual as decisões gulosas são tomadas.

Esse viés é problemático porque afeta não só a capacidade preditiva do modelo como também a interpretabilidade que podemos retirar dele: será que a árvore foi construída dessa forma porque ela enxergou algo nos dados, ou é apenas fruto dos tipos das variáveis? Esse viés se apresenta mesmo quando todas as variáveis são irrelevantes.

Na prática, isso pode não ser um problema. O viés de seleção pode aumentar a chance de divisões serem feitas em variáveis irrelevantes com maior quantidade de *cutoffs*, mas se o número de amostras for grande o suficiente isso não deve afetar muito o impacto do modelo - basta permitir que a árvore seja grande o suficiente a ponto de contar também com os *splits* importantes (Loh, 2014).

Certos algoritmos de construção de árvore são não-enviesados nesse aspecto, como por exemplo a família do FACT (GUIDE, QUEST, CRUISE). O C4.5, o CART e o CHAID são enviesados.

### Árvores Binárias vs. Multiway

Imaginemos uma variável categórica "clima" que pode admitir os valores "ensolarado", "nublado" e "chuvoso". Em uma árvore de decisão, existem duas formas interessantes de criar um nó para essa variável:

1. Um nó que checa se o dado possui um determinado valor pra variável (ex.: "clima == ensolarado?"), e apresenta dois filhos ("sim" e "não")
2. Um nó que checa o valor da variável no dado, e possui um filho para cada um dos possíveis valores (como na figura da Introdução).

Essas não são as duas únicas formas (por exemplo, a primeira opção poderia ter "sim", "não" e "faltante"), mas são duas bastante intuitivas e comuns. O primeiro esquema cria apenas árvores binárias, e o segundo esquema cria árvores *multiway* (notavelmente mais largas).

Toda árvore *multiway* pode ser escrita como uma árvore binária, pois basta criar mais camadas pra representar o mesmo modelo. Portanto, elas não variam na questão de representabilidade. Contudo, elas variam na questão de interpretabilidade: por serem mais compactas, as árvores *multiway* são mais fáceis de serem compreendidas visualmente por um ser humano (Kim & Loh, 2001).

Segue uma relação de quais algoritmos produzem árvores binárias e quais produzem árvores *multiway*.

- AID: binárias
- CHAID: multiway
- CART: binárias
- ID3: depende da implementação
- C4.5: multiway (apenas para variáveis categóricas)
- FACT: multiway
- QUEST: binárias
- CRUISE: multiway

É intuitivo visualizar uma divisão *multiway* pra variáveis categóricas, mas alguns algoritmos também as apresentam pra variáveis contínuas (separando em diversos intervalos). O CHAID, por exemplo, separa toda variável contínua em 10 intervalos distintos.

### Univariate vs. Multivariate

A maior parte das árvores de decisão fazem *splits* em apenas uma variável (*univariate*), no formato $X \\geq c$. Essa abordagem é simples, mas incapaz de representar *cutoffs* que não sejam ortogonais ao eixo da variável. Basta pensar numa linha diagonal: para aproximá-la usando árvores *univariate*, precisamos de um número potencialmente infinito de nós.

Podemos imaginar um outro esquema no qual os *splits* consideram múltiplas variáveis (*multivariate*), como por exemplo em uma combinação linear $a X\_1 + b X\_2 \\geq c$. Isso aumenta o espaço de hipóteses buscado pelo modelo, ao mesmo tempo que potencialmente gera árvores mais compactas (pois os nós são mais poderosos). Porém, há um custo associado: os nós em si podem ficar mais difíceis de serem interpretados.

Muitos métodos foram utilizados como testes lineares nos nós de árvores: LDA (*linear discriminant analysis*), programação linear, perceptrons, redes neurais, *hill climbing*, etc.

- CHAID: *univariate*
- CART: *univariate* e linear
- ID3: *univariate*
- C4.5: *univariate*
- QUEST: *univariate* e linear
- CRUISE: *univariate* e linear
- GUIDE: *univariate* e linear

### Ranqueamentos de importância

Uma das vantagens das árvores de decisão é a sua interpretabilidade: por conta da natureza de *white box* das árvores, um desses modelos pode fornecer intuições sobre o domínio no qual os dados foram retirados. Essa vantagem pode ser adicionalmente observada através do uso de *importance scores*, ou ranqueamentos de importância.

Basicamente, as variáveis são ranqueadas de acordo com o quanto elas contribuem pra tarefa de predição. Essa noção de "importância" é certamente não muito bem-definida (Loh, 2014), e por conta disso cada algoritmo inventa um jeito diferente.

Os únicos algoritmos de árvores de decisão *single-tree* que fornecem ranqueamento das variáveis são o CART (que usa *surrogate splits* pra isso) e o GUIDE (por meio de estatísticas $\\chi^2$). Dentre os métodos de *ensemble*, pode-se utilizar o ranqueamento empregado pelo *random forests* (importância via permutação).

Vale observar que, independente de como a árvore foi construída, sempre podemos calcular a importância com base na "fração de amostras que ela afeta". Por exemplo, a variável no nó raiz afeta 100% das amostras vistas: se o seu filho a esquerda afetar apenas 5% das amostras vistas, é de se esperar que ele seja menos importante do que o filho à direita (que afeta 95% das amostras vistas). Portanto, essa noção de "fração de amostras" pode ser combinada com o decréscimo na impureza pra obter uma métrica de importância. O problema dessa abordagem é duplo: (1) não necessariamente diz algo sobre o ranqueamento das variáveis *out-of-sample*, e (2) está sujeito aos vieses de seleção de variáveis (ver seção *Variable selection bias*). Portanto, outras abordagens (como as que usam permutação) são preferíveis (scikit-learn, 1.11.2.5).

### Tratamento de valores faltantes

No mundo real, frequentemente os dados que temos estão longe do ideal. Além deles terem algum ruído inerente ao processo de coleta, não é nada raro que certas amostras simplesmente não tenham certas *features* - isto é, elas possuem "valores faltantes" (*missing values*). Uma das abordagens mais diretas é simplesmente eliminar os dados que estão incompletos, mas dependendo do seu domínio (e do tamanho do seu conjunto de dados), isso não é uma opção.

Diversos algoritmos de árvore de decisão apresentam soluções pra esse problema (nem todos, contudo).

- CHAID: é criado um ramo na árvore pra caso o valor esteja faltante.
- CART: há diversas alternativas, que normalmente variam de uma implementação pra outra:
	- *surrogate split*: no treinamento, cada nó construído se associa não apenas a uma variável única, mas a uma variável *surrogate* (qual a variável que melhor "simula" a variável principal?)
		- joga pro nó com mais amostras
		- distribui aleatoriamente de forma proporcional às amostras
- ID3: ignora os valores faltantes.
- C4.5: envia o dado com valor faltante pra todos os ramos do nó atual, e depois avalia qual predição foi mais frequente (ponderando pela quantidade de amostras que cada ramo viu durante o treinamento).
- QUEST: imputação de valores
- CRUISE: imputação, *surrogate split*
- GUIDE: trata valores faltantes como uma categoria diferente.

### Árvores vs. Ensembles

Quando utilizamos árvores de decisão para solucionar um problema, existem dois objetivos que não são mutuamente excludentes: (1) produzir uma árvore que seja capaz de gerar boas previsões, e (2) inferir informações qualitativas sobre os dados de treinamento. O primeiro objetivo é compartilhado com diversos outros métodos de aprendizado de máquina, contudo o segundo objetivo é possível apenas para um conjunto restrito de modelos denominados *interpretáveis*, dentre os quais as árvores de decisão se destacam.

Nos últimos anos, árvores de decisão têm sido empregadas cada vez mais no contexto de *ensemble learning* (ou "aprendizados por comitê"). Nestes comitês, treinam-se dezenas ou centenas de classificadores de uma vez só, de forma que a resposta final do modelo é uma votação na qual todos os classificadores participam. Métodos de *ensemble* podem ser utilizados com quaisquer classificadores, mas suas versões mais populares frequentemente usam árvores de decisão: destacam-se o *Random Forest* e o *XGBoost*. Comparações baseadas em dados reais e simulados indicam que a acurácia do melhor algoritmo *single-tree* é em média 10% menor do que a de um *ensemble* de árvores (Loh, 2009).

Porém, o que se ganha em acurácia se perde em interpretabilidade. É difícil, senão impossível, extrair alguma interpretação de um conjunto de 500 árvores. Árvores de decisão isoladas continuam sendo um dos modelos mais interpretáveis, apesar de suas formas de ensemble terem se tornado mais populares. Para capitalizar em cima dessa vantagem, é essencial o uso de algoritmos que sejam não-enviesados e que produzam árvores compactas.

## Perguntas em aberto

- Se o GUIDE é tão bom assim, por que ele não está implementado nas bibliotecas mais famosas (scipy, WEKA)?
	- Como ele realmente se compara com o C4.5?
- Quais as condições pra uma árvore ser interpretável?
- ADTrees realmente são tão boas assim?

{ width=400px }