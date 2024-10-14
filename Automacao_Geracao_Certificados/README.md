# Sobrescrever Certificados Automático

Este projeto automatiza a tarefa de gerar e sobrescrever certificados personalizados para vários clientes com base em uma planilha de dados.

## Imagem do Certificado
![Imagem do Certificado](https://github.com/IsraelCodeMaster/AutomationsAndScripts/blob/de0ba8acdb9f4e87a68918bf29da44be1309e616/Automacao_Geracao_Certificados/(1)%20Israel%20Siqueira%20Alves%20certificado.png)

## Descrição

O script lê os dados de uma planilha do Excel e preenche os campos mutáveis em um certificado padrão. Os campos incluem:
- Nome do curso
- Nome do participante
- Tipo de participação
- Data de início e fim
- Carga horária
- Data de emissão do certificado

## Requisitos

Para executar o script, você precisará das seguintes bibliotecas Python:
- `pandas`
- `openpyxl`
- `Pillow`

Você pode instalar todas as dependências executando:
 `pip install -r requirements.txt`

## Arquivos Necessários
Certifique-se de que os seguintes arquivos estão no diretório do projeto:
- `AnnapurnaSIL-Bold.ttf`
- `AnnapurnaSIL-Regular.ttf`
- `certificado_padrao.jpg`
- `planilha_alunos.xlsx`


## Uso

 1. **Clone o repositório**:
    ```bash
    https://github.com/IsraelCodeMaster/AutomationsAndScripts.git

2. **Navegue até o diretório do projeto**:
   ```bash
   cd Automacao_Geracao_Certificados

3. **Certifique-se de que os arquivos `planilha_alunos.xlsx` e `certificado_padrao.jpg` estão no diretório do projeto.**

4. **Execute o script**
   ```bash
   python sobrescrever_certificados.py


## Estrutura dos Arquivos
- `sobrescrever_certificados.py`: Script principal para gerar os certificados.
- `planilha_alunos.xlsx`: Planilha do Excel com os dados dos participantes.
- `certificado_padrao.jpg`: Imagem do certificado padrão.
- `requirements.txt`: Lista de dependências do projeto.

## Contribuição
Sinta-se à vontade para abrir issues e pull requests. Qualquer contribuição é bem-vinda!

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Para mais projetos como esse, acesse meu Canal no Youtube.
https://www.youtube.com/@israelalvespro

## Autor 
Israel Alves




