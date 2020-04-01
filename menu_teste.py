#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
import general_functions as gf

#Inicia os gulags
lista_gulags = setup_inicial()
        
#Cores

fullscreen = False

# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
 
font = pygame.font.SysFont(None, 20)

click = False

while True:
    
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                    
    def menu_selecao():
        
        while True:
    
            screen.fill((0,0,0))
            gf.draw_text('Selecione um Gulag', (255, 255, 255), screen, tamanho=50, x=50, y=30)
    
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
                        lista_gulags[num_gulag].mostrar_info_gulag(screen,mainClock)
                else:
                    num_gulag += 1
            #Reseta o índice caso passe de 6
            if num_gulag >= 6:
                num_gulag = 0    
            
            #Chama a renderização dos botões
            pygame.draw.rect(screen, (255, 0, 0), Trofimovsk)
            gf.draw_text('Trofimovsk',gf.branco, screen, center =Trofimovsk.center)
            pygame.draw.rect(screen, (0, 255, 0), Solovetsky)
            gf.draw_text('Solovetsky',gf.branco, screen, center =Solovetsky.center)
            pygame.draw.rect(screen, (255, 0, 0), Norilsk)
            gf.draw_text('Norilsk',gf.branco, screen, center =Norilsk.center)
            pygame.draw.rect(screen, (0, 255, 0), Sevvostlag)
            gf.draw_text('Sevvostlag',gf.branco, screen, center =Sevvostlag.center)
            pygame.draw.rect(screen, (255, 0, 0), Pechorlag)
            gf.draw_text('Pechorlag',gf.branco, screen, center =Pechorlag.center)
            pygame.draw.rect(screen, (0, 255, 0), Karlag)
            gf.draw_text('Karlag',gf.branco, screen, center =Karlag.center)
            pygame.draw.rect(screen, (255, 0, 0), Altayskiy)
            gf.draw_text('Altayskiy',gf.branco, screen, center =Altayskiy.center)
    
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
    
    
    def game():
        running = True
        while running:
            screen.fill((0,0,0))
        
            gf.draw_text('game', (255, 255, 255), screen,  x= 20, y=20)
            
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
    
            gf.draw_text('options', font, (255, 255, 255), screen, (20,20))
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