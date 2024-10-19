#!/usr/bin/env python3 

# Script para analisar os processos ativos e monitorar quando os navegadores estiverem abertos ou fechados
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando as bibliotecas necessárias
import psutil
from time import sleep, strftime, localtime
import os
from colorama import init, Fore, Back

# Iniciando o colorama automaticamente
init(autoreset=True) 

# Lista de navegadores
navegadores = ("firefox chrome brave").split() # Colocando os nomes sem ser como é executado pelo terminal funciona OK


h = localtime() # Hora atual da máquina
fd = "%d-%m-%Y %H:%M:%S" # Formato da hora desejado
hf = strftime(fd, h) # Hora Formatada

# Abrindo um documento para DEBUG
g = open("status_navegador.log", "a") 
g.write(f"\n\nCOMECEI A EXECUÇÃO DO SCRIPT EM ==> {hf}\n")
print(f"{Back.RED}{'COMECEI A EXECUÇÃO DO SCRIPT EM ==>':>70} {hf}{' '*45}{Back.RESET}\n")
g.close() #fechando o arquivo


# Criando um loop infinito para monitorar o acesso aos navegadores
while True:
    # Bloco: Hora dentro do loop para ser atualizado a cada vez que rodar
    hora_atual = localtime() 
    formato_desejado = "%d-%m-%Y %H:%M:%S"
    hora_formatada = strftime(formato_desejado, hora_atual)
    
    # Criando um loop para interagir com cada processo ativo e verificar se os navegadores estão rodando
    for navegador in navegadores:    
        with open("status_navegador.log", "a") as f:  
            if any(p.info["name"] == navegador for p in psutil.process_iter(attrs=["name"])):
                print(f"O navegador {Back.GREEN}{navegador}{Back.RESET} {Back.YELLOW}está aberto{Back.RESET} ==> Data {hora_formatada}")
                f.write(f"O navegador {navegador} está aberto ==> Data {hora_formatada}\n")
                
            else:
                print(f"O navegador {Back.BLUE}{navegador}{Back.RESET} {Back.RED}está fechado{Back.RESET} ==> Data {hora_formatada}") 
                f.write(f"O navegador {navegador} não está em execução ==> Data {hora_formatada}\n")
                
    sleep(60) # atualizar a cada 1 minuto
    os.system("clear")  # Limpando a tela a cada ciclo 
