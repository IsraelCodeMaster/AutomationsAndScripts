# Automação de Comentários no Instagram

Este repositório contém um projeto de automação que faz comentários em publicações do Instagram utilizando Python. É ideal para participar de sorteios e aumentar a interação no seu perfil.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `pyautogui`
- `pyperclip`

### Instalação das Bibliotecas

Para instalar as bibliotecas necessárias, execute os seguintes comandos:

```sh
pip install pyautogui
pip install pyperclip
```
## On Linux, additionally you need to install the scrot application, as well as Tkinter:
```
sudo apt-get install scrot

sudo apt-get install python3-tk

sudo apt-get install python3-dev
```
## Configuração
### Clone este repositório:
```
git clone https://github.com/IsraelCodeMaster/AutomationsAndScripts.git

```
### Navegue até o diretório do projeto
```
cd AutomationsAndScripts/Automacao_Instagram

```
### Atualize o link da publicação do Instagram no script para o link desejado:
```
link = 'https://www.instagram.com/p/SEU_LINK_AQUI/'

```
## Como Usar
### Execute o script:
```
python3 automacao_instagram.py

```
O script abrirá uma nova aba no navegador, acessará o link da publicação e começará a fazer comentários automaticamente, escolhendo aleatoriamente os usuários da lista fornecida.

## Comentários Importantes

- ` O script realiza um loop de comentários a cada 60 segundos, escolhendo um intervalo de tempo aleatório para os comentários. `
- ` Certifique-se de ajustar as coordenadas do clique (x, y) no script para corresponder à posição do botão de comentário na tela do seu computador. `

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Para mais conteúdos, visite meu Canal do Youtube: https://www.youtube.com/@israelalvespro


