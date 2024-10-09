#!/usr/bin/env python3   
#shebang or hashbeng 

# Script para iniciar máquinas virtuais
# Canal do Youtube: https://www.youtube.com/@israelalvespro

#importando as bibliotecas que serão usadas no código
import  os
import colorama
from colorama import init,Fore,Back 

#Iniciando o colorama
colorama.init(autoreset=True)

# Função para imprimir as maquinas
def imprimir_maquinas(dic_maquinas):
    print(f"\n{Back.RED}{'MAQUINAS' : ^100}") #Centralizando MÁQUINAS com o parâmetro  : ^100 
    print('-'*105)
    repeticoes = 0
    
    for maquina, item in dic_maquinas.items(): #criando loop para printar cada item do dicionario
        repeticoes+=1
        if repeticoes == 1:
            print(f'{Fore.GREEN}{maquina: >40} ==> {item: <20}', ' '*23,'|')   
        elif repeticoes >= 2:
            print(f'{Fore.GREEN}{maquina: >40} ==> {item: <20}', ' ' *37, '|')
    print('-'*105)
    
#Dicionario de maquinas
dic_maquinas = {
                'maquina_01':'kali Roxo',   # nome da sua maquina virtual
                'maquina_02':'wubuntu', 
                'maquina_03':'Kali Linux', 
                'maquina_04':'ubuntu 23.04',
                 # Coloque quantas maquinas quiser
                
    }

# Função para iniciar a maquina virtual
def iniciar_maquina(options): #criando uma função
    command = 'virtualboxvm --startvm'
    machine = dic_maquinas.get(options) # Verifica se a opção está no dicionario 
    
    # Verifica se a opção que o usuario digitou esta no dicionario
    if machine:
        os.system(f"{command} '{machine}'") # Aspas simples em caso do nome da maquina ser separado
    else:
        print(f"{Fore.RED}Opção inválida: {options}")
          
# Imprimindo as maquinas
imprimir_maquinas(dic_maquinas)

# Solicitando a opção ao usuário
options = input('Qual maquina deseja inicar?\n') #atribuindo um valor a variavel options

# Iniciando a maquina escolhida
iniciar_maquina(options)
