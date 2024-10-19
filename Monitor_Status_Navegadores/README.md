# Monitoramento de Navegadores

![Captura da Tela](https://github.com/IsraelCodeMaster/AutomationsAndScripts/blob/82be6a57c1cdfdce6ca29f3285901f535cfec334/Monitor_Status_Navegadores/Screenshot%20from%202024-10-18%2021-41-32.png)

## Descrição
Este script Python monitora os navegadores Firefox, Chrome e Brave, verificando se estão
em execução e registrando o status em um arquivo de log. A cada minuto, ele verifica o
status dos navegadores e atualiza o log com a data e hora atuais.

## Requisitos
- `Python3`
- `Biblioteca psutil`
- `Biblioteca colorama`

## Instalação

1. Clone este repositório:
`git clone https://github.com/IsraelCodeMaster/AutomationsAndScripts.git`

2. Instale as dependências:
   `pip install psutil colorama`

## Uso
Execute o script com o seguinte comando:
`python3 script_status_navegadores.py`

O script começará a monitorar os navegadores Firefox, Chrome e Brave, registrando o status em `status_navegador.log`.

## Estrutura do Código
- `navegadores = ("firefox chrome brave").split()`: Define a lista de navegadores a serem monitorados.
- `hora_formatada`: Obtém a data e hora atuais.
- Loop infinito: Verifica o status dos navegadores a cada minuto e atualiza o log.

## Contribuição
Sinta-se à vontade para abrir um pull request ou relatar um problema. Adoramos contribuições!

## Licença
Este projeto está licenciado sob os termos da licença MIT.

## Para mais conteúdos, visite meu Canal do YouTube.
https://www.youtube.com/@israelalvespro

