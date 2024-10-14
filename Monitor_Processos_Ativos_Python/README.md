# Monitor de Processos Ativos no Linux

Este script monitora processos ativos no sistema Linux e cria um log com as informações dos processos, incluindo saída colorida no terminal para melhor visualização. Útil para análises e monitoramento.

### Imagem do Terminal
![Saída Terminal Claro](https://github.com/IsraelCodeMaster/AutomationsAndScripts/blob/8554868393641a4e029478140c5ecdb2256e7e76/Monitor_Processos_Ativos_Python/Screenshot%20from%202024-10-13%2022-03-34.png)


### Imagem do Terminal
![Saída Terminal Escuro](https://github.com/IsraelCodeMaster/AutomationsAndScripts/blob/8554868393641a4e029478140c5ecdb2256e7e76/Monitor_Processos_Ativos_Python/Screenshot%20from%202024-10-13%2022-01-54.png)

## Descrição

- **Nome do Script:** `monitor_processos.py`
- **Propósito:** Monitorar processos ativos e registrar informações em um log.
- **Funcionalidades:**
  - Mostra informações dos processos ativos no terminal com cores.
  - Salva um log detalhado dos processos com informações como PID, nome do usuário e status.

## Requisitos

- Python 3
- Bibliotecas: `psutil`, `colorama`

## Instalação

1. Clone o repositório para sua máquina local.
   ```bash
   git clone https://github.com/IsraelCodeMaster/AutomationsAndScripts.git

2. Navegue até o diretório do script.
    ```bash
    cd Monitor_Processos_Ativos_Python
3. Instale as dependências necessárias
    ```bash
    pip install psutil colorama

## Uso

1. Execute o script.
   ```python3
   python3 monitor_processos.py

2. O script atualizará as informações dos processos a cada minuto e limpará a tela a cada atualização.

## Exemplo de Saída no Terminal

  ```bash
    [1] Process: python3 (PID: 1234) ==> User: seu_usuario || Status: running ==> 12/12/2023 12:12:12
    [2] Process: bash (PID: 5678) ==> User: seu_usuario || Status: sleeping ==> 12/12/2023 12:12:12
  ```
## Link do Video [Como Criar Monitor de Processos] no Youtube:  
    ```bash
   https://youtu.be/vC7fNyahUQo?si=JHlrh3xvhNO2QHOM

## Contribuição
- Sinta-se à vontade para abrir pull requests e sugerir melhorias!
- Para relatar problemas, abra uma issue no GitHub.

  ##

    
