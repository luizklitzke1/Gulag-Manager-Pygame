#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial

#Inicia os gulags
lista_gulags = setup_inicial()

for campo in lista_gulags:
        print (campo)
 
# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
screen = pygame.display.set_mode((800, 800),0,32)
 
font = pygame.font.SysFont(None, 20)

#Método para impressão de texto na tela
def draw_text(text, color, surface, x, y,tamanho=1, font=None):
    font = pygame.font.Font(font, tamanho)
    textobj = font.render(text, 10, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

 
click = False
 
def menu_selecao():
    
    while True:
 
        screen.fill((0,0,0))
        draw_text('Selecione um Gulag', (255, 255, 255), screen, 50, 30, tamanho=50)
 
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
 
        #Definição dos botões para os Gulags
        
        Trofimovsk = pygame.Rect(50, 100, 200, 50),
        Solovetsky = pygame.Rect(50, 200, 200, 50),
        Norilsk = pygame.Rect(50, 300, 200, 50),
        Sevvostlag = pygame.Rect(50, 400, 200, 50),
        Pechorlag = pygame.Rect(50, 500, 200, 50),
        Karlag = pygame.Rect(50, 600, 200, 50),
        Altayskiy = pygame.Rect(50, 700, 200, 50)
        
        
        
        if Trofimovsk.collidepoint((mx, my)):
            if click:
                mostrar_info_gulag(Trofimovsk)
                
        elif Solovetsky.collidepoint((mx, my)):
            if click:
                game(Solovetsky)
        
        elif Norilsk.collidepoint((mx, my)):
            if click:
                game(Norilsk)
                
        elif Sevvostlag.collidepoint((mx, my)):
            if click:
                game(Sevvostlag)
                
        
        elif Pechorlag.collidepoint((mx, my)):
            if click:
                game(Pechorlag)
        
        elif Karlag.collidepoint((mx, my)):
            if click:
                game(Karlag)
                
        elif Altayskiy.collidepoint((mx, my)):
            if click:
                game(Altayskiy)
                
                
        #Chama a renderização dos botões
        pygame.draw.rect(screen, (255, 0, 0), Trofimovsk)
        pygame.draw.rect(screen, (0, 255, 0), Solovetsky)
        pygame.draw.rect(screen, (255, 0, 0), Norilsk)
        pygame.draw.rect(screen, (0, 255, 0), Sevvostlag)
        pygame.draw.rect(screen, (255, 0, 0), Pechorlag)
        pygame.draw.rect(screen, (0, 255, 0), Karlag)
        pygame.draw.rect(screen, (255, 0, 0), Altayskiy)
 
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def mostrar_info_gulag(gulag):
    
    running = True
    while running:
        screen.fill((0,0,0))
       
        draw_text(lista_gulags[0].nome, font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
       
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
 
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
menu_selecao()