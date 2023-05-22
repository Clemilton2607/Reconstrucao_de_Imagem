# Reconstrucao de Imagem utilizando Deep Learning

# 1-Protótipo
Para realizar esse projeto, montei um protótipo utilizando um raspberry pi4, anel de leds e uma câmera multicanal.
Esses itens são necessários, pois iremos fazer a captura de imagens RGB para compor o nosso dataset.

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/737e1ff8-026e-4890-8d72-3659878eb74a)

# 2-Imagens Capturadas
Depois de montar o protótipo e desenvolver a biblioteca dos componentes, decidi fazer a captura de algumas imagens para teste

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/c032fb3a-5544-4c70-8e4d-5ba75b44c371)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/711df434-f545-4dec-851e-b503c9aaab6f)
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/e98a63fa-5d99-4eba-88cf-43d94e67067c)

# 3-Deep Learning
## 3.1 Autoencoder 
Um autoencoder é um tipo de rede neural artificial usada para aprender codificações eficientes de dados não rotulados. Um autoencoder aprende duas funções: uma função de codificação que transforma os dados de entrada e uma função de decodificação que recria os dados de entrada da representação codificada.
![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/feaed1f3-153b-4607-9a82-77cd6cfdcaf3)

## 3.2 Autoencoder Convolucional
Um autoencoder convolucional é um tipo de rede neural que combina os conceitos de autoencoder e camadas convolucionais.
A adição de camadas convolucionais ao autoencoder convencional permite lidar com dados de entrada que possuem uma estrutura espacial, como imagens. As camadas convolucionais são projetadas para extrair características locais dos dados de entrada usando filtros convolucionais. Essas camadas ajudam a capturar informações importantes, como bordas, texturas e padrões, preservando a relação espacial dos dados.

![image](https://github.com/Clemilton2607/Reconstrucao_de_Imagem-/assets/79425563/0068b3fc-595c-4bd2-b3e9-eea4def5b934)

# 4-Testes iniciais
## 4.1 Testte 01
