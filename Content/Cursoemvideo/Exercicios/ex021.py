# DESAFIO 021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''
import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
'''

import pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()
    