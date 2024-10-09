#!/usr/bin/env python3

# Projeto de Monitoramento de Bateria em Python
# Autor: Israel Alves
# Canal do Youtube: https://www.youtube.com/@israelalvespro

#importando as bibliotecas necessarias
import psutil
import os
import colorama 
from colorama import Fore, Back, Style
import time

# Iniciando o colorama..
colorama.init(autoreset=True)

# Configurando variaveis importantes
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
percent_02 = f'{percent:,.0f}'
percent_03 = int(percent_02)


# Loop para verificar as condições ligado/desligado carregador da bateria
while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        percent_02 = f'{percent:,.0f}'
        percent_03 = int(percent_02)
        plugged = battery.power_plugged
        hora_02 = time.strftime('%d/%m/%y %H:%M:%S')
        f=open('Percent_battery.log', 'a', encoding='utf-8') # Criando um arquivo de LOG do código
        
        if plugged:   
            print(Back.GREEN+'A bateria está conectada e carregando!')
            print('Próxima verificação em 10 minutos')
            print(f'Porcentagem da bateria está em {Back.GREEN}{percent:,.0f}%', end=''), print(' ==>',Back.BLUE+hora_02)  # Utilizei {percent:,.0f} para formatar a saída 100.0% 100%
            print('')
            
            f.write(f'\nPorcentagem da bateria está em {percent:,.0f}% ==> {hora_02}\n')
            f.write('A bateria está conectada e carregando!\n')
            f.write('Próxima verificação em 10 minutos\n')
            time.sleep(600)#esperar 10 minutos           
            continue
        
        if not plugged:
            print(Back.RED + 'A bateria não está carregando. Cabo desconectado!')
            f.write('\nA bateria não está carregando. Cabo desconectado!\n')
            
            if percent_03 != 30:
                hora = time.strftime('%d/%m/%y %H:%M:%S')
                print('Verificando porcentagem da bateria a cada 1 minuto')
                f.write('Verificando porcentagem da bateria a cada 1 minuto\n')

                print(f"Porcentagem Atual está em {Back.RED}{percent_02}%" , end=''), print(' ==> Hora: ',Back.BLUE+hora,'\n') 
                f.write(f"Porcentagem Atual está em {percent_02}% ==> Hora: {hora}\n")
                time.sleep(60)#esperar 1 minuto
                
                
                if percent_03 <= 70: # 50% colocar 
                    print('vou desligar a maquina agora\n')
                    print(Fore.RED + ('Good By.. ' * 5))
                    f.write(f'\nVou desligar a maquina agora: Battery {percent_02}% ==> Hora: {hora}\n')
                    f.write('Good By... ' * 5)
                    time.sleep(10)
                    os.system('shutdown +1')#acrescentando 2 minutos para poder desligar a maquina para poder salvar o documento log
                    exit()#fechando o código

