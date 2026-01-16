from datetime import datetime
import os
import subprocess
import webbrowser
from urllib.parse import quote_plus

# Deixa os dicionários fora das funções (mais simples pra iniciante)
programas = {
  "calculadora": "calc",
  "bloco de notas": r"C:\Windows\system32\notepad.exe",
  "notepad": "notepad",
  "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
}

sites = {
  "youtube": "https://www.youtube.com",
  "google": "https://www.google.com",
  "gmail": "https://mail.google.com",
}

def abrir_programa(nome):
  if nome not in programas:
    print("Smiley: não conheço esse programa ainda.")
    return

  caminho = programas[nome]

  # Se for comando do Windows (calc, notepad)
  if caminho in ["calc", "notepad"]:
    subprocess.Popen(caminho)
    print(f"Smiley: abrindo '{nome}'...")
    return

  # Se for caminho completo (chrome, notepad.exe)
  if os.path.exists(caminho):
    subprocess.Popen([caminho])
    print(f"Smiley: abrindo '{nome}'...")
    return

  print("Smiley: achei o comando, mas não encontrei o programa instalado.")

def processar(comando):
  if comando == "sair":
    print("Smiley vai dormir!")
    return False

  if "hora" in comando:
    agora = datetime.now().strftime("%H:%M")
    print(f"Agora são {agora}.")
    return True

  if "nome" in comando:
    print("Meu nome é Smiley!")
    return True

  if "obrigado" in comando:
    print("é noiss :)")
    return True

  # abrir sitesa
  if comando.startswith("abrir "):
    alvo = comando.replace("abrir ", "").strip()

    if alvo in sites:
      webbrowser.open(sites[alvo])
      print(f"Smiley: abrindo '{alvo}'...")
      return True

    abrir_programa(alvo)
    return True

  # pesquisar
  if comando.startswith("pesquisar "):
    termo = comando.replace("pesquisar ", "").strip()
    if termo:
      url = "https://www.google.com/search?q=" + quote_plus(termo)
      webbrowser.open(url)
      print(f"Smiley: pesquisando por '{termo}'...")
    else:
      print("Smiley: pesquisa o quê? Ex: pesquisar gatos")
    return True

  print("Não entendi o que você escreveu!")
  return True


print("Opa, Smiley On, o que deseja?")

rodando = True
while rodando:
  comando = input("Você: ").lower()
  rodando = processar(comando)