#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
import general_functions as gf
from general_functions import *
import random
import time
import os

fullscreen = False

# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
icone = pygame.image.load("imgs/icone.png")
pygame.display.set_icon(icone)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#FULLSCREEN | HWSURFACE | DOUBLEBUF)

#Música de fundo
#music = pygame.mixer.music.load("sounds/katyusha.mp3")
#pygame.mixer.music.play(-1)



#Criação dos dados dos gulags
Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",((int(screen.get_width()*0.7),int(screen.get_height()*0.22 ))), foto="arnold.png")
Solovetsky = Campo("Solovetsky","Соловетскы",35,8,"Madeira",0,"Frio",((int(screen.get_width()*0.45),int(screen.get_height()*0.27 ))), foto="cash.jpg")
Norilsk = Campo("Norilsk","Норилск",15,3,"Mineração / Siderúrgica",3,"Muito Frio",((int(screen.get_width()*0.63),int(screen.get_height()*0.2 ))),foto="cash.jpg")
Sevvostlag = Campo("Sevvostlag","Севвостлаг",30,10,"Ouro e estanho",1,"Frio",((int(screen.get_width()*0.83),int(screen.get_height()*0.28 ))),foto="arnold.png")
Pechorlag = Campo("Pechorlag","Печорлаг",25,6,"Não",2,"Frio",((int(screen.get_width()*0.5),int(screen.get_height()*0.3 ))),foto="jo.jpg")
Karlag  = Campo("Karlag ","Карлаг",20,0,"Não",1,"Frio",((int(screen.get_width()*0.56),int(screen.get_height()*0.43 ))), foto="cash.jpg")
Altayskiy  = Campo("Altayskiy","Алтаыскиы",10,0,"Não",0,"Frio",((int(screen.get_width()*0.6),int(screen.get_height()*0.4 ))),foto="jo.jpg")

lista_gulags =[Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, Altayskiy ]

click = False

while True:
    
    
                    
    def menu_selecao():
        colisao = []
        contador = 0

        while True:
          
            screen.fill((0,0,0))
            margem_x = int(screen.get_width()*0.03)
            draw_text('Selecione um Gulag', vermelho, screen, tamanho=int(screen.get_width()*0.02), x=margem_x, y=int(screen.get_height()*0.06))
            
    
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
    
            #Mostrar a imagem do mapa
            desenhar_img(screen,'map2.png',(int(screen.get_width()*0.7),int(screen.get_height()*0.7 )),(screen.get_width()*0.25+10,int(screen.get_height()*.2)))
            
            #Definição dos botões para os Gulags
            w_botao = int(screen.get_width()*0.15)
            h_botao = int(screen.get_height()*0.05)
            Trofimovsk = pygame.Rect(margem_x ,int(screen.get_height()*0.20), w_botao, h_botao)
            Solovetsky = pygame.Rect(margem_x , int(screen.get_height()*0.30), w_botao, h_botao)
            Norilsk= pygame.Rect(margem_x , int(screen.get_height()*0.40), w_botao, h_botao)
            Sevvostlag= pygame.Rect(margem_x , int(screen.get_height()*0.50), w_botao, h_botao)
            Pechorlag= pygame.Rect(margem_x , int(screen.get_height()*0.60), w_botao, h_botao)
            Karlag= pygame.Rect(margem_x , int(screen.get_height()*0.70), w_botao, h_botao)
            Altayskiy= pygame.Rect(margem_x , int(screen.get_height()*0.80), w_botao, h_botao)
            lista_botoes_gulags = [Trofimovsk,Solovetsky,Norilsk,Sevvostlag,Pechorlag,Karlag,Altayskiy]
            
            #Loop para mostrar os botões e miniatura no mapa, incluindo o fato de quando são selecionados
            #Utiliza o num_gulag para bater a relação entre os índices
            num_gulag= 0
            for botao_gulag in lista_botoes_gulags:
                botao = pygame.draw.rect(screen, branco, botao_gulag)
                mini = pygame.image.load('imgs/'+lista_gulags[num_gulag].mini)
                
                #Checa colisao com o mouse
                if botao_gulag.collidepoint((mx,my)):
                        
                    draw_text(lista_gulags[num_gulag].nome_r, preto,screen,center = botao.center, tamanho= 18)
                    mini = pygame.transform.scale(mini, (int(screen.get_width()*0.08),int(screen.get_height()*0.14)))
                    if click:
                        btn1.play() 
                        lista_gulags[num_gulag].mostrar_info_gulag(screen,mainClock)
                    
                else:
                                 
                    draw_text(lista_gulags[num_gulag].nome, preto,screen,center = botao.center)
                    mini = pygame.transform.scale(mini, (int(screen.get_width()*0.04),int(screen.get_height()*0.07)))
                    
                #Cria um rect com a img para poder reposicionar corretamente
                mini_rect = mini.get_rect(center=lista_gulags[num_gulag].minipos)
                screen.blit(mini, mini_rect)
                num_gulag += 1
            
            
            #Reseta o índice caso passe de 6
            if num_gulag >= 6:
                num_gulag = 0  
                
                  
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        btn2.play() 
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)
            contador +=1 
    
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
    
    