# YouTube Video Downloader

Script para baixar vídeos do YouTube utilizando `yt-dlp`.

## Visão Geral

Este script permite que você baixe vídeos do YouTube selecionando a melhor qualidade disponível ou escolhendo um formato específico. Ele utiliza a biblioteca `yt-dlp` para realizar o download e permite entrada de dados com timeout automático.

## Requisitos

- Python 3.x
- `yt-dlp` 
- `threading` (biblioteca padrão do Python)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/IsraelCodeMaster/AutomationsAndScripts.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd /AutomationsAndScripts/Youtube_Downloader
    ```
3. Instale a biblioteca `yt-dlp`:
    ```bash
    pip install yt-dlp
    ```

## Uso

Execute o script e insira a URL do vídeo do YouTube quando solicitado:
  ```bash
  python3 youtube_downloader.py
  ```

O script solicitará que você escolha se deseja selecionar o formato do vídeo. Caso contrário, o formato de maior resolução disponível será selecionado automaticamente.

- Enter the URL: https://www.youtube.com/watch?v=seu-video
- Do you want to select from the available options? (y/n): y
- Enter the format id of the video: 137

Após a conclusão do download, será exibida uma mensagem de sucesso:

Download completo usando yt-dlp.
- Não se esqueça de se inscrever no canal: https://www.youtube.com/@israelalvespro/videos?sub_confirmation=1

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Agradecimentos
yt-dlp - Biblioteca utilizada para download de vídeos.

Canal do YouTube: @israelalvespro

