#!/usr/bin/env python3

# Monitor de processos, com criação de LOG para analises.
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando as bibliotecas necessárias
import psutil
from time import sleep 
import os
from time import strftime
import colorama
from colorama import Fore, Back

# Iniciando o colorama
colorama.init(autoreset=True)

# Função para pegar todos os processos ativos
def log_activity():
    data_atual = strftime('%d/%m/%y %H:%M:%S')
    rep = 0
    active_processes = psutil.process_iter(attrs=['pid', 'name', 'status', 'username'])
    for process in active_processes: 
        rep += 1
        print(f"[{rep}] {Fore.RED}Process:{Fore.RESET} {process.info['name']} (PID: {Fore.YELLOW}{process.info['pid']}{Fore.RESET}) {Fore.GREEN} ==> {Fore.RESET} User: {Fore.BLUE}{process.info['username']} {Fore.RESET} || status: {Back.YELLOW}({process.info['status']}{Back.RESET}) ==> {data_atual}")
        
        # Salvar sem edição de cores
        #save_activity(f"[{rep}] Process: {process.info['name']} (PID: {process.info['pid']}) ==> User: {process.info['username']} ==> {data_atual}")

        # Salvar com edição de cores
        save_activity(f"[{rep}] {Fore.RED}Process:{Fore.RESET} {process.info['name']} (PID: {Fore.YELLOW}{process.info['pid']}{Fore.RESET}) {Fore.GREEN} ==> {Fore.RESET} User: {Fore.BLUE}{process.info['username']} {Fore.RESET} || status: {Back.YELLOW}({process.info['status']}{Back.RESET}) ==> {data_atual}")
        
# Função para anotar as informações em um documento        
def save_activity(activity):
    with open('log_atividades.log', 'a') as file: 
        file.write(f"{activity}\n")

# Loop para atualizar os processos ativos a cada 1 minuto
while True:
    log_activity()
    sleep(60) # Registra a cada minuto
    os.system("clear") # Limpando a tela
