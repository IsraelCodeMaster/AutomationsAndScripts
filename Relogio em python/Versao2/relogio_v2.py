#!/usr/bin/env/ python3 

# Projeto Relógio em Python
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando as bibliotecas necessarias
import requests
import tkinter as tk
from tkinter import *
import os
from time import strftime
import time
from threading import Thread 
from datetime import datetime, timedelta # para atualizar a data a cada  1 dia

# Configuração da janela principal
root = tk.Tk()
root.title('My Clock In Python')
root.geometry('460x410') # 450x390
root.maxsize(460, 410)# antes 1000, 1000
root.minsize(460, 410)#root.minsize(450, 350)    
root.configure(background='#1d1d1d')

# Carregando as imagens para o modo claro e escuro
light = PhotoImage(file='imagens/brightness.png')
dark = PhotoImage(file='imagens/dark.png')

# Função para alternar entre modo claro e escuro
def toggle_dark_mode():
    if root['bg'] == '#1d1d1d':
        root['bg'] = 'white'
        tela['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        horas['bg'] = 'white'
        weather_02['bg'] = 'white'
        locate_02['bg'] = 'white'
        temperatura['bg'] = 'white' 
        humidade['bg'] = 'white' #new line add
        dark_mode_button['image'] = light
        dark_mode_button['bg'] = 'white'

    else:
        root['bg'] = '#1d1d1d'
        tela['bg'] = '#1d1d1d'
        saudacao['bg'] = '#1d1d1d'
        data['bg'] = '#1d1d1d'
        horas['bg'] = '#1d1d1d'
        weather_02['bg']='#1d1d1d'
        locate_02['bg']='#1d1d1d'
        temperatura['bg']='#1d1d1d'
        humidade['bg']='#1d1d1d' # new line add
        dark_mode_button['image'] = dark
        dark_mode_button['bg'] = 'white' 

# Função para obter e exibir a saudação com o nome do usuário
def get_saudacao():

    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)

# Função para obter e exibir a data atual
def get_data():
    # essa parte é para mostrar no relogio
    data_atual=(strftime('%A %d %B %Y'))
    data.config(text=data_atual)
    
    # essa parte está sendo implementada para logica de atualizar a data automaticamente
    # calcula o tempo até 00:01 do próximo dia
    now = datetime.now()
    next_day = now + timedelta(days=1)
    target_time = next_day.replace(hour=0, minute=1, second=0, microsecond=0)
    
    # calcula a diferença em milissegundos
    time_difference = target_time - now
    milliseconds = int(time_difference.total_seconds() * 1000)

    # Agende a chamada da função
    root.after(milliseconds, get_data)

# Essa função atualiza a hora no display grafico a cada 1 segundo ou 1000 milissegundos
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

# Função para pegar a previsao do tempo para sua região
repeticoes=0
def get_weather():
    API_KEY = 'sua_chave_API'

    cidade = 'juatuba' # sua cidade ou a cidade que desejar
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'
    request = requests.get(link)
    request_dic = request.json()
    
    # debug para analisar as informações do dicionario
    print(request_dic, '\n\n')
    
    locate = request_dic['name'] 
    description = request_dic['weather'][0]['description']
    weather = request_dic['main']['temp'] - 273.25  # -273.25 é o calculo feito para transformar graus firengih em celcius
    
    ### Pegar as informações de temperatura máxima e minima para colocar no relogio tbm
    temperatura_max = request_dic['main']['temp_max'] - 273.25
    temperatura_min = request_dic['main']['temp_min'] - 273.25
    
    # Debug para analisar informações no terminal
    print(f"Temperatura MAX = {int(temperatura_max)}ºC\nTemperatura MIN = {int(temperatura_min)}ºC\n")
    
    texto_04 = f"max: {int(temperatura_max)}ºC\nmin: {int(temperatura_min)}ºC"
    temperatura['text']=(texto_04)
    
    # a funcao de conversao int() para converter float em inteiro em python é muito util....
    texto=f'{description} {int(weather)}°C'
    weather_02['text']=(texto)
    
    texto_02=(f"{locate}-MG")
    locate_02['text']=(texto_02)
    
    # tentando acrescentar a humidade do ár no código
    temp_humidade = request_dic['main']['humidity']
    if temp_humidade <= 30:
        texto_03 = f"Humidade baixa: {temp_humidade}%"
        
    elif 30 < temp_humidade <=50:
        texto_03 = f"Humidade moderada: {temp_humidade}%"
    
    else:
        texto_03 = f"Humidade alta: {temp_humidade}%"
        
    humidade['text']=(texto_03)
    
    
    global repeticoes
    repeticoes+=1
    temp=time.asctime()
    print(f"Nº de atualizações da temperatura = {repeticoes} ==> Hora update = {temp}\n")
    
    # o tempo é em milissegundos ==> vai atualizar a cada 5 minutos
    root.after(300000, get_weather) # apenas essa linha eu resolvi o problema de todo o código. Ele atualiza auto agora

# Configuração do botão de modo escuro/claro
dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=8, bg='white')
dark_mode_button.place(x=200,y=10)

# Configuração da tela e dos widgets
tela = tk.Canvas(root, width=600, height=20, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
saudacao = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 20, 'bold')) #backup #8e27ea
saudacao.place(x=160,y=80)
data = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 20, 'bold'))
data.place(x=80,y=120)
horas = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 60, 'bold'))
horas.place(x=70,y=160)
weather_02 = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 20),text=' ')
weather_02.place(x=120,y=260)
humidade = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 15),text=' ') # new line add
humidade.place(x=120,y=300) # new line add x=120, y=330
locate_02 = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 15),text=' ')
locate_02.place(x=160,y=330) # x=160,y=300

# informação nova adicionada sobre tmp MAX e MIN
temperatura = Label(root, bg='#1d1d1d', fg='#800080', font=('Arial', 10),text=' ')
temperatura.place(x=370,y=260) # x=320,y=270


#chamando as funções
get_saudacao()
get_data()
get_horas()
get_weather()


#botão para atualizar a temperatura
botao_01=Button(root, bg='#1d1d1d', fg='#800080', font=('Arial', 12), text='Temp', command=get_weather).place(x=130,y=370)#x=130,y=340

# Botão para fechar o relógio
botao_02=Button(root, bg='#1d1d1d', fg='#800080', font=('Arial', 12), text='Exit', command=root.destroy).place(x=200,y=370)#x=200,y=340

# Botao para atualizar a data manualmente
botao_03=Button(root, bg='#1d1d1d', fg='#800080', font=('Arial', 12), text='Date', command=get_data).place(x=255,y=370)#x=255,y=340

# Iniciando o loop principal da interface gráfica
root.mainloop()
