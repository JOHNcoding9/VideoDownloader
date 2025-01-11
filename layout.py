# O que é um fork?
#Um fork é uma cópia de um projeto de software que permite modificá-lo independentemente do projeto original. Forks geralmente acontecem quando:
#A comunidade deseja implementar mudanças que o autor original não aceita ou não tem tempo para adicionar.
#O projeto original fica inativo, e alguém decide continuar o desenvolvimento.
#Divergências de visão entre os desenvolvedores originais e novos contribuintes.
#No caso de software open-source (código aberto), como o youtube-dl, qualquer pessoa pode fazer um fork, modificar o código e compartilhar sua #própria versão.

import yt_dlp
import tkinter as tk
import validators # verificar se a url é válida
from tkinter import Checkbutton, BooleanVar
from urllib.parse import urlparse
from tkinter import ttk

cor_1 = '#030303'  # Preto
cor_3 = '#ffffff'  # Branco
cor_5 = '#616161'  # Cinza
cor_6 = '#23fa02' # verde
cor_7 = '#02faee' # ciano
cor_8 = '#f7f7e6' # sei não


# Janela principal
janela = tk.Tk()

# Configuração da janela
janela.title("URL Downloader")
janela.geometry("800x600")  # Largura x Altura
janela.configure(bg=cor_3)

# Criando a label principal
label = tk.Label(janela, text="Baixe URLs da mídia de sua escolha", font=("Arial", 16), bg=cor_3, fg=cor_1)
label.pack()

# Criar o frame principal
frame = tk.Frame(janela, width=600, height=150, bg=cor_3)
frame.pack(side="top", padx=10, pady=10)

# Variável global para o estado do Checkbutton
apenas_audio = BooleanVar() # audio apenas
legendas = BooleanVar()


# Função para atualizar a tela
def Atualizar_tela():
    # Limpar o conteúdo do frame atual
    for widget in frame.winfo_children():
        widget.destroy()

def Funcoes_botao(entrada):
   url = entrada.get().strip() 
   if url:
        if not validators.url(url):
         print("URL inválida! Por favor, insira uma URL válida.")
         return
        
        ListarFormatos(url)
        Update_progress()
        Download(url)

def Tela_inicial():

    # Atualiza a tela e limpa widgets existentes no frame
    Atualizar_tela()

    entrada = tk.Entry(frame, font=("Arial", 14), width=30, bg=cor_8,fg=cor_1)
    entrada.pack(pady=5)

    botao = tk.Button(frame,
        text='Download',
        command=lambda: Funcoes_botao(entrada),
            fg=cor_3,
            bg=cor_6,
            width=15,
            height=2,
            font=("Helvetica", 12, "bold"),
            activebackground=cor_7,
            activeforeground=cor_3,
            relief="flat",
            bd=4
        )
    
    botao.pack(side='top', padx=5)

    check1 = Checkbutton(janela, text="Apenas Áudio (MP3)", variable=apenas_audio,bg=cor_8)
    check1.pack()

    check2 = Checkbutton(janela, text="Legendas (pt-BR)", variable=legendas, bg=cor_8)
    check2.pack()


def Update_progress():

    # Barra de progresso
    progress = ttk.Progressbar(janela, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)
    for i in range(101):
        progress['value'] = i  # Atualiza a barra
        janela.update_idletasks()  # Atualiza a interface gráfica
        janela.after(50)  # Aguarda 50 milissegundos para dar a sensação de progresso

    progress.destroy()


def Download(url):  
     
     # Definindo as opções do ydl_opts para vídeo e áudio
     ydl_opts = {
            'format': 'best',  # Baixar o melhor formato de vídeo e áudio
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Nome do arquivo de saída
            'merge_output_format': 'mp4', # Converte para MP4
            'preferredcodec': 'mp4',  # Formato final
        }
    
     if legendas.get():
        ydl_opts.update({'writesubtitles': True,  # Baixar legenda
    'writeautomaticsub': True, # Baixar legendas automatica
    'subtitleslangs': ['pt'],  # Idiomas das legendas (substitua 'en' por 'pt', 'es', etc.)
    'subtitlesformat': 'srt',   # Formato das legendas (ex.: 'srt', 'vtt')
    })


     dominio = urlparse(url).netloc
     if "youtube.com" in dominio or "youtu.be" in dominio:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio',
            'outtmpl': 'downloads/youtube/%(title)s.%(ext)s',
             })

     if apenas_audio.get():  # Se a opção "apenas áudio" estiver selecionada
         if "youtube.com" in dominio or "youtu.be" in dominio:
          ydl_opts.update({
            'format': 'bestaudio',
            'merge_output_format': 'mp3',
            'preferredquality': '192',
             })

         else:
          ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]


         ydl_opts['ffmpeg_location'] = r'C:\ProgramData\chocolatey\bin\ffmpeg.exe' # Substitua pelo caminho do seu ffmpeg (se não tiver é necessário baixar, ou então remover a parte 'ffmpeg_location' e 'preferredcodec': 'mp3'. Pórem, o arquivo voltará com o formato WEBM ao invés de MP3 )

     try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
       ydl.download([url])
       print("Download concluído!")

     except yt_dlp.utils.DownloadError as e:
        print(f"Erro ao processar a URL: {e}")

def ListarFormatos(url):
    try:
        with yt_dlp.YoutubeDL({'listformats': None}) as ydl:
            info = ydl.extract_info(url, download=False)
            formatos = info.get('formats', [])
            print("Formatos disponíveis:")
            for formato in formatos:
                print(f"ID: {formato['format_id']}, Resolução: {formato.get('resolution', 'N/A')}, Extensão: {formato.get('ext', 'N/A')}")
    except Exception as e:
        print(f"Erro ao listar formatos: {e}")




Tela_inicial()
# Inicializar o projeto
janela.mainloop()

# bolar maneira de baixar video de outras midias alem do yt (ok)

# testes
# https://youtu.be/C6h0Qt329jI?si=YEP0SrQrm_g6eUuj

# https://www.tiktok.com/@zueirarrando/video/7436160671470914871?is_from_webapp=1&sender_device=pc

# https://www.youtube.com/shorts/D3eTV1h2JXg?feature=share

# https://www.twitch.tv/tck10/clip/EnticingRacyEndiveWutFace-tN_mAsj_AkhZmIHH