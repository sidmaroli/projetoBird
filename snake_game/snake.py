import pygame
import random
import time


WIDTH = 700
HEIGTH = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))


white = (225,225,225)
green = (0,128,0)
blue = (0,0,225)
red = (225,0,0)
black = (0,0,0)
yellow = (255,255,102)


snake_block = 10
tickt = 13

clock = pygame.time.Clock()
snake_speed = 10

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Score(score):
    value = score_font.render("Ponto: " + str(score), True, yellow)
    screen.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green,[x[0], x[1], snake_block, snake_block])

def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [WIDTH / 10, HEIGTH / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1_change = 0
    y1_change = 0

    x1 = WIDTH/2
    y1 = HEIGTH/2

    snake_List = []
    Langth_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGTH - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
                screen.fill(white)
                message("Você perdeu! Pressione C-Jogar denovo ou Q-Sair", red)
                Score(Langth_snake - 1)
                pygame.display.update()
 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

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

        if x1 >= WIDTH or x1 <= 0 or y1 >= HEIGTH or y1 <= 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)

        pygame.draw.rect(screen, red,[foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) >= Langth_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Score(Langth_snake - 1)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGTH - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(tickt)
 
        pygame.display.update() 

    pygame.quit()     
    quit()  

gameLoop()
