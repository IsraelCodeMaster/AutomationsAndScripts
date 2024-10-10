#!/usr/bin/env python3

# Automação Web com selenium para pegar informações sobre um canal do Youtube
# Canal do Youtube: https://www.youtube.com/@israelalvespro

# Importando todas as bibliotecas necessarias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configuração do WebDriver do Chrome
driver = webdriver.Chrome()

# Navegue até o seu canal do YouTube
url_do_canal = "https://www.youtube.com/@israelalvespro/videos"
driver.get(url_do_canal)
sleep(7)

# Role a página para baixo para carregar mais vídeos
for i in range(3):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    sleep(1) # tive que usar esse bloco de código para pegar todos os nomes e links

# Encontre todos os elementos de vídeo
elementos_de_video = driver.find_elements(By.CSS_SELECTOR, "a#video-title-link")

# Extraia os links e títulos dos vídeos
links_de_video = [elemento.get_attribute("href") for elemento in elementos_de_video]
titulos_de_video = [elemento.text for elemento in elementos_de_video]

# Criar um documento para salvar todos os nome e links
f = open('links_videos_youtube_israel.txt', 'a', encoding='utf-8')

# Imprima os links e títulos dos vídeos
# zip usado para percorrer as listas em paralelo. Não precisando criar dois loops for separados para fazer o mesmo
for link, titulo in zip(links_de_video, titulos_de_video): 
    print(f"Título do Vídeo: {titulo}")
    print(f"Link do Vídeo: {link}")
    print("-" * 30)

    f.write(f"Título do Vídeo: {titulo}\n")
    f.write(f"Link do Vídeo: {link}\n")
    f.write(f"{'-'* 30}\n\n")

sleep(3)

print('O script acabou')
# Feche o navegador
driver.quit()

#Israel Alves
