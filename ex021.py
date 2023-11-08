#FAÇA UM PROGRAMA QUE ABRA E REPRODUZA UM ÁUDIO DE ARQUIVO MP3 COM UM MÓDULO

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Life.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()
