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

#game init vars
answer = "guitarhero"
current = len(answer)*"_ "
found = len(answer)*[False]
incorrect = 0

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        for index,x in enumerate(pressed[pygame.K_a:pygame.K_z+1]):
            if x == True:
                input_key = pygame.key.name(pygame.K_a+index)
    hangman_img = pygame.image.load("data/Hangman-"+str(incorrect)+".png")
    current_text = font.render(current, 1, (255, 255, 255))
    screen.fill((0,0,0))
    screen.blit(hangman_img,(50,200))
    screen.blit(title, title.get_rect(centerx=screen.get_width()/2,y=50))
    screen.blit(current_text, current_text.get_rect(centerx=width/2,centery=height/2))
    pygame.display.flip()