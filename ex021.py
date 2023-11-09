#FAÇA UM PROGRAMA QUE ABRA E REPRODUZA UM ÁUDIO DE ARQUIVO MP3 COM UM MÓDULO
#Não quer funcionar no run normal, só no debug
import pygame
#Para inicializar o pygame
pygame.init()
#Para carregar o arquivo, com nome simples e na mesma pasta
pygame.mixer.music.load('life.mp3')
#Para dar play na música
pygame.mixer.music.play()
#Para que ele aguarde a música terminar de tocar:
pygame.event.wait()
#pygame.quit() <= desnecessário