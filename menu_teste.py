#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
import general_functions as gf
from general_functions import *

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
            draw_text('Selecione um Gulag', (255, 255, 255), screen, tamanho=50, x=50, y=30)
    
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
    
            #Definição dos botões para os Gulags
            
            Trofimovsk = desenhar_botao(screen, vermelho,200,50,50,150,"Trofimovsk")
            Solovetsky = desenhar_botao(screen, azul,200,50,50,250,"Solovetsky")
            Norilsk = desenhar_botao(screen, vermelho,200,50,50,350,"Norilsk")
            Sevvostlag = desenhar_botao(screen, azul,200,50,50,450,"Sevvostlag")
            Pechorlag = desenhar_botao(screen, vermelho,200,50,50,550,"Norilsk")
            Karlag = desenhar_botao(screen, azul,200,50,50,650,"Karlag")
            Altayskiy = desenhar_botao(screen, vermelho,200,50,50,750,"Altayskiy")
            
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
                
            #Mostrar a imagem do mapa
            desenhar_img(screen,'map.png',(int(screen.get_width()*0.70-20),int(screen.get_height()*0.70 )),(screen.get_width()*0.25+10,int(screen.get_height()*.15)))
    
            #Mostrar as imagens dos gulags no mapa
            tamanho_mini = (int(screen.get_width()*0.04),int(screen.get_height()*0.07))
            
            #Trofimovsk
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.65),int(screen.get_height()*0.13 ))))
            
            #Solovetsky 
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.40),int(screen.get_height()*0.2 ))))
            
            #Norilsk
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.54),int(screen.get_height()*0.16 ))))
            
            #Sevvostlag
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.83),int(screen.get_height()*0.2 ))))
            
            #Pechorlag
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.48),int(screen.get_height()*0.2 ))))
            
            #Karlag 
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.55),int(screen.get_height()*0.35 ))))
            
            #ALTAYSKIY 
            desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.60),int(screen.get_height()*0.32 ))))
            
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