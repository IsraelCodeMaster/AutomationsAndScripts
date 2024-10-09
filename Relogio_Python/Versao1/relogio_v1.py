#!/usr/bin/env python3   
#shebang or hashbeng

# Projeto Relógio em Python
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando as bibliotecas necessarias
import tkinter as tk
from tkinter import *
import os
from time import strftime


# Configuração da janela principal
root = tk.Tk()
root.title('My Clock In Python')
root.geometry('450x350')
root.maxsize(1000,1000)
root.minsize(450, 350)
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
     dark_mode_button['image'] = light
     dark_mode_button['bg'] = 'white'
   else:
     root['bg'] = '#1d1d1d'
     tela['bg'] = '#1d1d1d'
     saudacao['bg'] = '#1d1d1d'
     data['bg'] = '#1d1d1d'
     horas['bg'] = '#1d1d1d'
     dark_mode_button['image'] = dark
     dark_mode_button['bg'] = '#1d1d1d'

# Função para obter e exibir a saudação com o nome do usuário
def get_saudacao():
   nome_usuario = os.getlogin()
   saudacao.config(text='Olá, ' + nome_usuario)

# Função para obter e exibir a data atual
def get_data():
   data_atual = strftime('%a, %d %b %Y')
   data.config(text=data_atual)

# Função para obter e exibir a hora atual, atualizando a cada segundo
def get_horas():
   hora_atual = strftime('%H:%M:%S')
   horas.config(text=hora_atual)
   horas.after(1000, get_horas)

# Configuração do botão de modo escuro/claro
dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=8, bg='#1d1d1d')
dark_mode_button.pack(pady=10)

# Configuração da tela e dos widgets
tela = tk.Canvas(root, width=600, height=20, bg ='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg ='#1d1d1d', fg='#8e27ea', font=('Arial', 14, 'bold'))
saudacao.pack()
data = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Arial', 14))
data.pack(pady=2)
horas = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Arial', 60, 'bold'))
horas.pack(pady=2)

# Chamando as funções para exibir saudação, data e hora
get_saudacao()
get_data()
get_horas()

# Iniciando o loop principal da interface gráfica
root.mainloop()


