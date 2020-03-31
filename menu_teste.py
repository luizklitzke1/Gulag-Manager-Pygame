#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial

#Inicia os gulags
lista_gulags = setup_inicial()

for campo in lista_gulags:
        print (campo)
        
#Cores

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)
 
# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
 
font = pygame.font.SysFont(None, 20)

#Método para impressão de texto na tela
def draw_text(text, color, surface,tamanho=30, font=None, x=None, y=None, center=None):
    font = pygame.font.Font(font, tamanho)
    textobj = font.render(text, 10, color)
    textrect = textobj.get_rect()
    
    #Defina caso seja informado centralização
    if center:
        textrect.center = center
    #Define caso sejam dados X e Y
    else:
        textrect.x = x
        textrect.y = y
    surface.blit(textobj, textrect)

click = False
 
def menu_selecao():
    
    while True:
 
        screen.fill((0,0,0))
        draw_text('Selecione um Gulag', (255, 255, 255), screen, tamanho=50, x=50, y=30)
 
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
 
        #Definição dos botões para os Gulags
        
        Trofimovsk = pygame.Rect(50, 100, 200, 50)
        Solovetsky = pygame.Rect(50, 200, 200, 50)
        Norilsk = pygame.Rect(50, 300, 200, 50)
        Sevvostlag = pygame.Rect(50, 400, 200, 50)
        Pechorlag = pygame.Rect(50, 500, 200, 50)
        Karlag = pygame.Rect(50, 600, 200, 50)
        Altayskiy = pygame.Rect(50, 700, 200, 50)
        
        lista_botoes_gulags = [Trofimovsk,Solovetsky,Norilsk,Sevvostlag,Pechorlag,Karlag,Altayskiy]
        
        #Loop para definir qual botão for selecionado e enviar os dados caso for
        num_gulag= 0
        for botao_gulag in lista_botoes_gulags:
            if botao_gulag.collidepoint((mx,my)):
                if click:
                    mostrar_info_gulag(lista_gulags[num_gulag])
                    print(num_gulag)
            else:
                num_gulag += 1
            print(num_gulag)
        #Reseta o índice caso passe de 6
        if num_gulag >= 6:
            num_gulag = 0
        
        """
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
        """       
                
        #Chama a renderização dos botões
        pygame.draw.rect(screen, (255, 0, 0), Trofimovsk)
        draw_text('Trofimovsk',branco, screen, center =Trofimovsk.center)
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
       
        draw_text(gulag.nome,(255, 255, 255), screen, x=50, y=30)
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
       
        draw_text('game', (255, 255, 255), screen,  x= 20, y=20)
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
 
        draw_text('options', font, (255, 255, 255), screen, (20,20))
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