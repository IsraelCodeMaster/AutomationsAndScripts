#!/usr/bin/env python3   
#shebang

# Script para baixar vídeos do YOUTUBE
# Canal do Youtube: https://www.youtube.com/@israelalvespro/videos?sub_confirmation=1


# Importando as bibliotecas necessárias
import yt_dlp
import threading

# Criando um timeout para escolher a resposta automaticamente 
def input_with_timeout(prompt, timeout=10):
    result = [None]

    def get_input():
        result[0] = input(prompt)

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    input_thread.join(timeout)
    if input_thread.is_alive():
        print("\nTempo esgotado! Seleção automática configurada para 'não'.")
        return "n"
    return result[0]

# Função para extrair links do youtube e baixar os vídeos
def download_youtube_video(video_url):
    """Baixar vídeo do Youtube usando yt-dlp."""

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Baixar melhor vídeo e áudio
        "merge_output_format": "mp4",          # Garantir que vídeo e áudio estejam em mp4
        "outtmpl": "%(title)s.%(ext)s",        # Template do nome do arquivo de saída
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get("formats", None)

        # Mostrar todos formatos disponiveis e pedir para usuario selecionar
        for f in formats:
            print(f"{f['format_id']}:\t{f['ext']} ({f.get('format_note', None)}p)")

        resolution_choice = input_with_timeout("Do you want to select from the available options? (y/n): ")

        if resolution_choice.lower() == "y":
            format_id = input("Enter the format id of the video: ")
            ydl_opts["format"] = format_id + "+bestaudio"
        else:
            # Select the highest resolution format
            highest_resolution = max(formats, key=lambda x: (x.get("height") or 0))
            format_id = highest_resolution["format_id"]
            ydl_opts["format"] = format_id + "+bestaudio"

        # Atualizando a opção com o formato selecionado
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completo usando yt-dlp.\nNão se esqueça de increver no canal: https://www.youtube.com/@israelalvespro/videos?sub_confirmation=1")

if __name__ == "__main__":
    video_url = input("Cole a URL: ")
    download_youtube_video(video_url)
  
