# Reconstrucao de Imagem utilizando Deep Learning

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
## 4.1 Testte 01
