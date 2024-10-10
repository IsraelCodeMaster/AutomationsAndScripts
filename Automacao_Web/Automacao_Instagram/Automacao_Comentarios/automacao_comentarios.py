#!/usr/bin/env/ python3 

# Automação de comentários no Instagram
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importar as bibliotecas que serão usadas
import pyautogui as py
from time import sleep
import pyperclip
import random
from time import strftime


# Tempo de espera para executar cada linha de comando
py.PAUSE = 2 

# Link do sorteio
link = ('https://www.instagram.com/p/C3bADVGOHwo/') 
pyperclip.copy(link)

# Abrindo uma nova aba do navegador
py.hotkey('ctrl', 't')
py.hotkey('ctrl', 'v')
sleep(2)
py.press('enter')
sleep(3)
py.scroll(-2)
sleep(2)

## Parte de comentar ##

# Lista de usuarios do seu perfil do instagram
list_users = (
"""
wemersonsilva660

wemerson6120

welliton_silva_777

gu__santoss

gu_santos031

boffito_ronyy

bartolomeu.siqueira.902

ronyy123dias
"""

).split()

# Variavel para obter a data atual e horario 
data = strftime('%d/%m/%y %H:%M:%S')

# Criando um arquivo para anotações importantes para analise
f = open('Anotações_Comentarios_Sorteio_PIX300.txt', 'a', encoding='utf-8')
f.write(f'\nO scrip iniciou: ==> {data}\n')

# Função para comentar
def comentar():
    for i in range(1): 
    
        data_01 = strftime('%d/%m/%y %H:%M:%S')
        random.shuffle(list_users) # Embaralhando a lista de users
        users_list = random.choice(list_users) # Escolhendo um item da lista de usuarios
    
        print(f'@{users_list} ==> {data_01}\n')
        f.write(f'\n@{users_list} ==> {data_01}\n') # Escrevendo no arquivo
    
        py.click(x=937, y=427) # Clicando no botão comentar
        py.write(f'@{users_list}', interval=0.05) # Escrevendo na barra comentar 
        py.click(x=1120, y=536) # clicando em publicar comentário

comentar()# chamando função
f.close() # fechando o arquivo de texto

f = open('Anotações_Comentarios_Sorteio_PIX300.txt', 'a', encoding='utf-8')# Abrindo o arquivo 2 vez
f.write('\n2º Loop da função comentar\n')
print('2º Loop da função comentar\n')

f.write(f'Aguarde 60 segundos p/ loop\n')

sleep(1)# Tempo de espera para iniciar o próximo loop
rep = 0

for i in range (15):     
    sorteio=('60 80 60 50 90 80 60 90').split()# Escolhendo o tempo de espera para cada comentário
    random.shuffle(sorteio)
    sort = random.choice(sorteio) # Escolhendo 1 usuário
    rep+=1
    comentar() # Chamando a função
    
    # Debug das informações úteis
    print(f'Valor sorteado de espera: {sort}\n')
    print(f'Repetições: {rep}')
    
    # Anotações no arquivo de texto
    f.write(f'\nValor sorteado de espera: {sort}')
    f.write(f'\nRepetições: {rep}\n')
    
    # Pausa entre repetições
    sleep(int(sort))

# Escrevendo no arquivo de texto    
f.write('\nO script acabou\n')

f.close() # fechando o arquivo de texto

py.click(x=1224, y=90) # posição para fechar a janela x

print('\nO script acabou')
#Israel Alves
