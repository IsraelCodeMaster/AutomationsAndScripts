# Agendar Desligamento da Máquina

Este script permite que você agende o desligamento da sua máquina em um horário específico. Ele verifica a hora atual em um loop e, quando chega o horário programado, envia uma notificação e agenda o desligamento da máquina.

## Descrição

- **Nome do Script:** `agendar_desligamento.sh`
- **Propósito:** Agendar o desligamento da máquina em um horário específico.
- **Funcionalidade:**
  - Solicita ao usuário um horário de desligamento no formato HH:MM:SS.
  - Verifica a entrada para garantir que está no formato correto.
  - Verifica a hora atual em um loop.
  - Envia uma notificação e agenda o desligamento quando o horário especificado é alcançado.

## Uso

1. Clone o repositório para sua máquina local.
   ```bash
   git clone https://github.com/seu-usuario/Scripts_Bash_Linux.git
2. Navegue até o diretório do script.

    ```bash
   cd Scripts_Bash_Linux/Automacoes_Sistema

3. Dê permissão de execução ao script.
    ```bash
   chmod +x agendar_desligamento.sh

4. Execute o script.
    ```bash
   bash angendar_desligamento   

# Exemplo de uso
Ao executar o script, perguntará:  
  `Qual hora deseja desligar o notebook Israel? (HH:MM:SS):`
  
Você pode digitar, por exemplo, `23:30:00`. Quando a hora atual atingir 23:30:00, o script  enviará uma notificação e angendará o desligamento da máquina.

# Autor
- `Israel Alves`

# Licença
Este projeto está licenciado sob a `Liceça MIT`.




