#!/usr/bin/env python3   
#shebang or hashbeng 

# Script para iniciar máquinas virtuais
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando as bibliotecas que serão usadas no código
import re
import subprocess
import  os
import colorama
from colorama import Fore, Back 

# Iniciando o colorama
colorama.init(autoreset=True)

# Lista vazia para receber os nomes das VMS
vms_list = []
# Dicionário para armazenar as máquinas virtuais
dic_maquinas = {}

def list_vms():
    try:
        # Executa o comando `VBoxManage list vms` e captura a saída
        result = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True, check=True)
        # Usa expressão regular para extrair os nomes entre aspas
        vm_names = re.findall(r'"([^"]+)"', result.stdout)
        # Adiciona os nomes à lista
        for name in vm_names:
            vms_list.append(name)          
        # Adicionando valores ao dicionário   
        for i, vm in enumerate(vms_list, 1): # começando do indice 01
            dic_maquinas[f"maquina_{i:02d}"] = vm
            
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar VMs: {e}")

# Função para iniciar a maquina virtual
def iniciar_maquina(options): #criando uma função
    command = 'virtualboxvm --startvm'
    machine = dic_maquinas.get(options) 
    if machine: # Verifica se a opção que o usuario digitou esta no dicionario
        os.system(f"{command} '{machine}'") # Aspas simples em caso do nome da maquina ser separado
    else:
        print(f"{Fore.RED}Opção inválida: {options}")

if __name__ == "__main__":
    # Chamando a funcção
    list_vms()
    
    #Centralizando MÁQUINAS com o parâmetro  : ^90
    print(f"\n{Back.RED}{'MÁQUINAS' : ^90}")  
    print('-'*90)
    
    #Criando loop para printar cada item do dicionário
    for maquina, item in dic_maquinas.items(): 
        print(f'{Fore.GREEN}{maquina: >40} ==> {item: <20}', ' '*23,'|')

    # Solicitando a opção ao usuário
    options = input('Qual maquina deseja inicar Israel?\n') # Atribuindo um valor a variavel options

    # Iniciando a maquina escolhida
    iniciar_maquina(options) 
