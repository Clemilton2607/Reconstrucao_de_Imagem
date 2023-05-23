# Reconstrucao de Imagem utilizando Deep Learning
Hodiernamente, as imagens hiper espectrais tem se ganhado destaque na sociedade por está presente em diversas áreas (militar, industrial e científica), uma vez que a mesma tem capacidade de capturar e processar uma imagem em um grande número de comprimento de ondas, até mesmo os que estão invisíveis a olho nu. Todavia, a reconstrução de imagens hiper espectrais acaba sendo apenas aplicada em empresas e não se tem um fácil acesso à tal reconstrução pelo fato dos aparelhos possuírem um alto valor no mercado. 
Nesse viés, pode-se tornar viável desenvolver um sistema de baixo custo de imagem hiper espectral utilizando reconstrução espectral baseada em deep learnig. Sendo assim, o projeto consiste em desenvolver um protótipo que fará a integração lógica entre um anel de led, juntamente com uma câmera multicanal e um raspberry pi 4 para a criação de um dataset que posteriormente será utilizado em uma rede neural para realizar a reconstrução das imagens.

# 1-Protótipo
Para realizar esse projeto, montei um protótipo utilizando um raspberry pi4, anel de leds e uma câmera multicanal.
Esses itens são necessários, pois iremos fazer a captura de imagens RGB para compor o nosso dataset.

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/1a06b60f-48b8-4fc7-ae7f-4379595539e2)


# 2-Imagens Capturadas
Depois de montar o protótipo e desenvolver a biblioteca dos componentes, decidi fazer a captura de algumas imagens para teste

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/0e6e7472-8f14-408a-bade-a656093614c2)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/e539489f-64bf-4a0b-a93e-0e4997366155)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/b67ec94a-13d0-460b-b490-e6df86825f72)

# 3-Deep Learning
## 3.1 Autoencoder 
Um autoencoder é um tipo de rede neural artificial usada para aprender codificações eficientes de dados não rotulados. Um autoencoder aprende duas funções: uma função de codificação que transforma os dados de entrada e uma função de decodificação que recria os dados de entrada da representação codificada.
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/88fe5e5f-a16a-49b8-8c22-50abdc5f6ebe)

## 3.2 Autoencoder Convolucional
Um autoencoder convolucional é um tipo de rede neural que combina os conceitos de autoencoder e camadas convolucionais.
A adição de camadas convolucionais ao autoencoder convencional permite lidar com dados de entrada que possuem uma estrutura espacial, como imagens. As camadas convolucionais são projetadas para extrair características locais dos dados de entrada usando filtros convolucionais. Essas camadas ajudam a capturar informações importantes, como bordas, texturas e padrões, preservando a relação espacial dos dados.

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/80e2bbbb-c40f-4d6b-b361-1c23ec36665b)

# 4-Testes iniciais
Para teste iniciais, eu primeiramente trabalhei com reconstrução de imagens utilizando datasets encontrados na internet
## Testte Piloto
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/434d52bd-6178-4c0e-b751-8c8ebbe9ab1c)
## Testte Piloto 2.0
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/b9bed09c-f025-461c-bffc-634d2a5320aa)
## Testte 01
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/967a3b85-c07e-43cb-8ce9-fdd39dc86909)
## Teste 02
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/9eab433f-cd3d-4fb4-acff-f88991253522)
## Teste 03
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem/assets/79425563/eaaeff06-2c56-4d69-915c-43dfc73041e5)

## Resultados dos testes iniciais
RESULTADOS
- Teste 01- MMSE: 0.017352
- Teste 02 - MSE: 0.01398
- Teste 03 - MSE: 0.00978
