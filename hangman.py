import os, sys
import pygame
import time
from pygame.locals import *

#initialization
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

size = width, height = 500, 400

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Python Hangman')

font = pygame.font.Font(None, 36)
title = font.render("The Hangman Game", 1, (255, 255, 255))
answer = "guitarhero"
current = len(answer)*"_ "

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    current_text = font.render(current, 1, (255, 255, 255))
    screen.fill((0,0,0))
    screen.blit(title, title.get_rect(centerx=screen.get_width()/2,y=50))
    screen.blit(current_text, current_text.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2))
    pygame.display.flip()