from gtts import gTTS
from playsound import playsound
import os 
from NumeroporExtenso import Numeros

class Robo:
    def __init__(self,texto:str) -> None:
        self.__robo = gTTS(text = texto, lang = 'pt-br', slow = False)
    
    def salva_audio(self) -> None:
        nome_arquivo = input ("Digite o nome do Arquivo a ser salvo: ")
        nome_file = f"{nome_arquivo}.mp3"
        self.__robo.save(nome_file)
        playsound(nome_file)
        return

    def fala(self,saveFile=False) -> None:
        nomefile = "audio.mp3"
        self.__robo.save(nomefile)
        playsound(nomefile)
        if saveFile == True:
            self.salva_audio()
            return
        os.remove(nomefile)
        return
    
    

if __name__ == "__main__":
    while True:
        emtrada = input(":")
        if emtrada in (""," "):
            break
        if emtrada in ("falar","f"):
            texto = input("Digite o texto a ser falado:")
            rb = Robo(texto=texto)
            rb.fala()
            
        if emtrada in ("numeros","n"):
            numero = int(input("Digite um nuemero: "))
            text = Numeros()
            rb = Robo(texto=text.main(emtrada_numero=numero))
            rb.fala()