# Projeto PIBIC-CNPq
Pesquisador: Clemilton Barroso de Souza Furtado

# Reconstrucao de Imagem utilizando Deep Learning
Hoje em dia, as imagens hiper espectrais tem se ganhado destaque na sociedade por está presente em diversas áreas (militar, industrial e científica), uma vez que a mesma tem capacidade de capturar e processar uma imagem em um grande número de comprimento de ondas, até mesmo os que estão invisíveis a olho nu. Todavia, a reconstrução de imagens hiper espectrais acaba sendo apenas aplicada em empresas e não se tem um fácil acesso à tal reconstrução pelo fato dos aparelhos possuírem um alto valor no mercado. 
Nesse viés, pode-se tornar viável desenvolver um sistema de baixo custo de imagem hiper espectral utilizando reconstrução espectral baseada em deep learnig. Sendo assim, o projeto consiste em desenvolver um protótipo que fará a integração lógica entre um anel de led, juntamente com uma câmera multicanal e um raspberry pi 4 para a criação de um dataset que posteriormente será utilizado em uma rede neural para realizar a reconstrução das imagens.

# 1-Conceitos Iniciais
Para entender um pouco sobre a temática do projeto, temos que entender alguns termos que serão utilizados no decorrer dos textos:
  - Imagem: Reprodução da figura de um objeto pela combinação dos raios de luz provenientes da mesma. 
  - Espectro: Distribuição da intensidade de uma radiação em função de uma grandeza característica, como o comprimento de onda, energia, a frequência ou a massa.
  - Bandas: Segmento do espectro eletromagnético.
    ![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/1b5f7034-d878-4a47-8a27-4e9b7e5e472d)
  - Imagem espectral – conjunto de imagens dentro do mesmo objeto representadas cada uma delas com diferentes comprimentos de onda.
  - Resolução Espectral – número e largura das porções do espectro eletromagnético medido pelo sensor.
  - Resolução Espacial – Nível de detalhe espacial representado em uma imagem. 
  - Imagem Multiespectral x imagem hiper espectral.
    ![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/1b425ae1-61fc-444c-bcdb-7173f5f82a15)

# 2-Imagem Multiespectral x Imagem Hiperespectral
## 2.1 Imagem Multiespectral
O seu termo em inglês é Multispectral Imaging (MSI).
São formadas por bandas discretizadas e variam entre 3-20 bandas. 
Resolução espectral limitada
Processamento mais simples
São frequentemente utilizsadas no sensoriamento remoto

## 2.2 Imagem Hiperespectral
O seu termo em inglês é Hyperspectral Imaging (HSI).
São formadas por bandas contíguas, possuindo centenas ou até mesmo milhares de bandas. 
Captura e processamento de uma imagem em um grande número de comprimentos de onda.
Capacidade de discriminação espectral
Aplicações avançadas: detecção de minerais, identificação de poluentes, análise de solos, monitoramento da saúde das plantas e muito mais.
Processamento complexo

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/29689da1-1bf1-4d07-be49-7191fdafeec7)

# 3-Objetivos do projeto
1) Desenvolver o protótipo de um sistema integrado de câmera multicanal e minicomputador que seja rápido, portátil e de baixo custo para análise de imagens.
2) Efetuar a integração lógica e eletrônica das partes do protótipo.
3) Desenvolvimento do Dataset.
4) Desenvolvimento do algoritmo de Deep learning.
5) Reconstruir imagens hiper espectrais a partir de imagens RGB.

# 4-Protótipo
Para realizar esse projeto, montei um protótipo utilizando um Raspberry pi4, anel de leds e uma câmera multicanal.
Esses itens são necessários, pois iremos fazer a captura de imagens 150x150 em RGB para realizar testes e posteriormente montar um datastet.

![Imagem do WhatsApp de 2023-09-07 à(s) 18 14 39](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/2411dd1b-9a8b-454a-b064-5ab1da39d192)

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/1a06b60f-48b8-4fc7-ae7f-4379595539e2)

# 5-Imagens Capturadas
Depois de montar o protótipo e desenvolver a biblioteca dos componentes, decidi fazer a captura de algumas imagens para teste
OBS: As imagens das figuras estão na dimensão 1920 x 1080
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/0e6e7472-8f14-408a-bade-a656093614c2)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/e539489f-64bf-4a0b-a93e-0e4997366155)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/b67ec94a-13d0-460b-b490-e6df86825f72)

# 6- Diagrama de Blocos 
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/4ed18333-fc42-40e2-8137-5017787a2330)

# 7-Dataset
Levando em consideração o pouco tempo de duração do projeto, eu optei por utilizar um dataset da plataforma Kaggle com imagens de paisagens com dimensões de 150x150.
![0](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/8cf4a226-ff22-4dd3-87a8-304cd7ac2635)
![2](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/daa7200a-83ec-4aa2-890e-88d39252091c)

# 8-Pré-processamento
Na parte de pré-processamento, eu apliquei filtros variando o comprimento de onda em 400-700nm e posteriormente apliquei a normalização MinMax para transformar os valores de [0-255] a [0-1].

# 9-Deep Learning
## 9.1 Autoencoder 
Um autoencoder é um tipo de rede neural artificial usada para aprender codificações eficientes de dados não rotulados. Um autoencoder aprende duas funções: uma função de codificação que transforma os dados de entrada e uma função de decodificação que recria os dados de entrada da representação codificada.
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/88fe5e5f-a16a-49b8-8c22-50abdc5f6ebe)

## 9.2 Autoencoder Convolucional
Um autoencoder convolucional é um tipo de rede neural que combina os conceitos de autoencoder e camadas convolucionais.
A adição de camadas convolucionais ao autoencoder convencional permite lidar com dados de entrada que possuem uma estrutura espacial, como imagens. As camadas convolucionais são projetadas para extrair características locais dos dados de entrada usando filtros convolucionais. Essas camadas ajudam a capturar informações importantes, como bordas, texturas e padrões, preservando a relação espacial dos dados.

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/80e2bbbb-c40f-4d6b-b361-1c23ec36665b)

# 10-Testes iniciais utilizando a biblioteca Cifar10
Para teste iniciais, eu primeiramente trabalhei com reconstrução de imagens utilizando datasets do Cifar10
## Teste Piloto
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/434d52bd-6178-4c0e-b751-8c8ebbe9ab1c)
## Testte Piloto 2.0
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/b9bed09c-f025-461c-bffc-634d2a5320aa)
## Testte 01
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/967a3b85-c07e-43cb-8ce9-fdd39dc86909)
## Teste 02
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/9eab433f-cd3d-4fb4-acff-f88991253522)
## Teste 03
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/eaaeff06-2c56-4d69-915c-43dfc73041e5)

## 10.1 Resultados dos testes iniciais
RESULTADOS
- Teste 01- MSE: 0.017352
- Teste 02 - MSE: 0.01398
- Teste 03 - MSE: 0.00978

# 11- Testes Utilizando imagens com apenas 3 comprimentos de onda (RGB)
Após realizar os testes iniciais com o dataset do Cifar10, utilizei o dataset do Kaggle com imagens filtradas em 3 comprimentos de ondas (RGB) e fiz a reconstrução de uma imagem de uma maçã.
OBS: Na época em que essa reconstrução foi feita, eu não tinha em mão os protótipo montado, então não realizei testes com imagens capturadas pelo protótipo
Imagem Original
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/a9785a36-4655-4ad8-9967-3acf7d960390)

Imagem Reconstruidas
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/505436c9-24a3-48eb-a207-83ea6c9a660e)

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/133ef034-fcbc-499a-9f3d-381446bf6cf1)

# 12-Teste final utilizando imagens com 7 comprimentos de onda
Com posse das imagens filtradas em 7 cores diferentes, eu criei um novo algoritmo de autoencoder que se adaptasse aos novos comprimentos de onda. Ademais, eu adicionei uma segunda rede neural que deixasse mais nítida a reconstrução feita pelo Autoencoder.

Gráfico da Acurácia e Perda do Autoencoder
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/ba89773b-5fe3-47a8-a223-597f02e2cd25)

Obtendo uma métrica de RMSE igual 0.0685, foram realizadas as reconstruções de imagens capturas pelo protótipo com dimensões de 150x150 e 1920x1080.
![Teste_01](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/fd13f6ce-ab89-41d8-b8a2-801c7ea432e9)

![Teste_02](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/4aa52338-658e-495f-ac5a-dec84b44b493)

![Teste_05](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/81753ab5-0348-459c-84b8-34891bb09b4f)


