# Automação Web para Coleta de Informações do YouTube

Este script utiliza Selenium para automatizar a coleta de informações de vídeos de um canal do YouTube. Ele navega até a página de vídeos do canal e extrai os títulos e links de todos os vídeos carregados.

## Descrição

- **Nome do Script:** `automacao_web_youtube.py`
- **Propósito:** Automatizar a coleta de títulos e links de vídeos de um canal do YouTube.
- **Funcionalidade:**
  - Acessa a página de vídeos de um canal específico do YouTube.
  - Rola a página para carregar mais vídeos.
  - Extrai e exibe os títulos e links dos vídeos.
  - Salva as informações em um arquivo de texto.

## Requisitos

- Python 3
- Selenium
- WebDriver do Chrome

### Instalando o WebDriver do Chrome

1. Baixe o WebDriver do Chrome na [página de downloads do ChromeDriver](https://sites.google.com/chromium.org/driver/downloads).
2. Extraia o arquivo baixado:
   ```bash
   unzip chromedriver_linux64.zip

### Mova o WebDriver para um diretório no PATH do seu sistema:
  ```bash
      sudo mv chromedriver /usr/local/bin/
  ```                    

### Verifique a instalação do WebDriver:
  ```bash
    chromedriver --version
  ```  

### Uso

1. Clone o repositório para sua máquina local.
    ```bash
   git clone https://github.com/IsraelCodeMaster/AutomationsAndScripts.git

2. Navegue até o diretório do script.
   ```bash
   cd AutomationsAndScripts/Automacao_Web/Automacao_Web_Selenium


3. Instale as dependências necessárias.
   ```bash
   pip install selenium

4. Execute o script.
   ```python3
   python3 automacao_web_youtube.py

## Para mais projetos como esse acesse meu canal no Youtube: https://www.youtube.com/@israelalvespro
