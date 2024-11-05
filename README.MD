#YouTube Video Downloader Script
Este é um simples script em Python para baixar vídeos do YouTube. Ele utiliza a biblioteca pytubefix para facilitar o processo de download, proporcionando uma forma rápida e eficiente de salvar vídeos diretamente para o seu computador.

#Pré-requisitos
- Python 3.x instalado em seu computador.
- A biblioteca pytubefix, que pode ser instalada facilmente via pip.

#Instalação
1. Instalar o Python:
Caso ainda não tenha o Python instalado, você pode baixá-lo aqui.

2. Instalar a Biblioteca pytubefix:
Abra o terminal e execute o seguinte comando para instalar a biblioteca necessária:
pip install pytubefix

#Como Usar
1. Execute o script:
Após garantir que o Python e a biblioteca pytubefix estão corretamente instalados, você pode executar o script com o seguinte comando:
python baixar_video.py

2. Digite o URL do vídeo:
O script solicitará que você insira o URL do vídeo do YouTube que deseja baixar.

4. Aguarde o download:
O script irá buscar o vídeo, verificar se está disponível e proceder com o download do vídeo na melhor resolução possível. Ao final, será exibida uma mensagem indicando que o download foi concluído com sucesso.

##Exemplo de execução:
Video URL: https://youtu.be/fAXpNW5fuC4?si=AVG9EvyOe93BIu9b
Title: Never Gonna Give You Up
Thumbnail URL: https://i.ytimg.com/vi/fAXpNW5fuC4/sddefault.jpg
Download completed successfully.

#Como Funciona
O script realiza os seguintes passos:

1. Recebe o URL do vídeo: O script solicita que o usuário insira o URL do vídeo desejado.
2. Verifica a disponibilidade do vídeo: Usando a biblioteca pytubefix, o script verifica se o vídeo está disponível para download.
3. Obtém a melhor resolução do vídeo: O script seleciona automaticamente a melhor resolução disponível para o download.
4. Realiza o download: O vídeo é baixado diretamente para o diretório em que o script foi executado.

#Tratamento de Erros
O script conta com um tratamento de erros simples, que exibe uma mensagem caso algo dê errado durante o processo, como problemas com a URL do vídeo ou falhas na conexão.

##Exemplos de erros:
- URL inválida: Se você inserir um link que não seja um vídeo válido do YouTube.
- Problemas de conexão: Se houver algum problema ao tentar baixar o vídeo.

#Considerações Finais
O script foi desenvolvido para ser simples e direto ao ponto, com o objetivo de baixar vídeos do YouTube com a mínima quantidade de código e sem complicações.
É recomendado que você tenha algum conhecimento básico em Python para poder executar e modificar o script caso necessário.
O código pode ser facilmente adaptado para suportar mais funcionalidades, como download de playlists ou vídeos em diferentes resoluções.

#Contribuições
Contribuições são bem-vindas! Se você encontrar bugs ou quiser adicionar novos recursos ao script, sinta-se à vontade para criar um fork do projeto.

Licença
Este projeto está licenciado sob a MIT License.

---

#YouTube Video Downloader Script
This is a simple Python script to download YouTube videos. It uses the pytubefix library to make the download process easier, providing a quick and efficient way to save videos directly to your computer.

#Prerequisites
Python 3.x installed on your computer.
The pytubefix library, which can be easily installed via pip.

#Installation
1. Install Python:
If you don't have Python installed yet, you can download it from here.

2. Install the pytubefix Library:
Open the terminal and run the following command to install the required library:
pip install pytubefix

#How to Use
1. Run the script:
After ensuring Python and the pytubefix library are properly installed, you can run the script with the following command:
python download_video.py

2. Enter the video URL:
The script will prompt you to enter the YouTube video URL you want to download.

3. Wait for the download:
The script will fetch the video, check its availability, and proceed with downloading the video in the best available resolution. Once completed, a success message will be displayed.

##Example of execution:
Video URL: https://youtu.be/fAXpNW5fuC4?si=AVG9EvyOe93BIu9b
Title: Never Gonna Give You Up
Thumbnail URL: https://i.ytimg.com/vi/fAXpNW5fuC4/sddefault.jpg
Download completed successfully.

#How It Works
The script performs the following steps:

1. Receives the video URL: The script prompts the user to input the desired YouTube video URL.
2. Checks video availability: Using the pytubefix library, the script checks whether the video is available for download.
3. Gets the best video resolution: The script automatically selects the highest resolution available for the download.
4. Downloads the video: The video is downloaded directly to the directory where the script is executed.

#Error Handling
The script includes basic error handling that displays an error message if something goes wrong during the process, such as issues with the video URL or connection problems.

##Example errors:
Invalid URL: If you input a link that is not a valid YouTube video.
Connection issues: If there is a problem while attempting to download the video.

#Final Considerations
- The script was designed to be simple and straightforward, with the goal of downloading YouTube videos using the minimal amount of code and without complications.
- It is recommended to have basic Python knowledge to run and modify the script if needed.
- The code can be easily adapted to support additional features, such as downloading playlists or videos in different resolutions.

#Contributing
Contributions are welcome! If you find bugs or want to add new features to the script, feel free to fork the project and submit a pull request.

#License
This project is licensed under the MIT License.