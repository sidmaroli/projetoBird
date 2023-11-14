from math import gamma
from sys import flags
from tkinter import font
import pygame
import time
import random



WIDTH = 800
HEIGTH = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))

game_over = False

white = (225,225,225)
blue = (0,0,225)
red = (225,0,0)


x1 = WIDTH/2
y1 = HEIGTH/2

snake_block = 10

x1_change = 0
y1_change = 0


clock = pygame.time.Clock()
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (WIDTH/2, HEIGTH/2))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0




    x1 += x1_change
    y1 += y1_change
    screen.fill(white)

    pygame.draw.rect(screen, blue,[x1, y1, snake_block, snake_block])

    clock.tick(snake_speed)


    message("Você perdeu", red)    
    pygame.display.update()        
    time.sleep(2)


