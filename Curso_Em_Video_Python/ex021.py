# Ex: 021 - Faça um programa em Python que abra o áudio de um arquivo MP3.
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('aa.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''import playsound
playsound.playsound('aa.mp3', True)'''

'''from pygame import mixer
mixer.init()
mixer.music.load('aa.mp3')
mixer.music.play()
input('Agora você escuta?')'''
