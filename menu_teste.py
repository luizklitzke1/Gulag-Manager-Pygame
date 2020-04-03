#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
import general_functions as gf
from general_functions import *

fullscreen = False

# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Criação dos dados dos gulags
    
Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",((int(screen.get_width()*0.65),int(screen.get_height()*0.13 ))), foto="arnold.png")
Solovetsky = Campo("Solovetsky","Соловетскы",35,8,"Madeira",0,"Frio",((int(screen.get_width()*0.40),int(screen.get_height()*0.2 ))), foto="cash.jpg")
Norilsk = Campo("Norilsk","Норилск",15,3,"Mineração de Ferro / Trabalho em Siderúrgica",3,"Muito Frio",((int(screen.get_width()*0.54),int(screen.get_height()*0.16 ))),foto="cash.jpg")
Sevvostlag = Campo("Sevvostlag","Севвостлаг",30,10,"Ouro e estanho",1,"Frio",((int(screen.get_width()*0.83),int(screen.get_height()*0.2 ))),foto="arnold.png")
Pechorlag = Campo("Pechorlag","Печорлаг",25,6,"Não",2,"Frio",((int(screen.get_width()*0.48),int(screen.get_height()*0.2 ))),foto="jo.jpg")
Karlag  = Campo("Karlag ","Карлаг",20,0,"Não",1,"Frio",((int(screen.get_width()*0.55),int(screen.get_height()*0.35 ))), foto="cash.jpg")
Altayskiy  = Campo("Altayskiy","Алтаыскиы",10,0,"Não",0,"Frio",((int(screen.get_width()*0.60),int(screen.get_height()*0.32 ))),foto="jo.jpg")
    
lista_gulags =[Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, Altayskiy ]


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
    
            #Mostrar a imagem do mapa
            desenhar_img(screen,'map.png',(int(screen.get_width()*0.70),int(screen.get_height()*0.70 )),(screen.get_width()*0.25+10,int(screen.get_height()*.15)))
            
            #Definição dos botões e miniaturas para os Gulags
            
            Trofimovsk = pygame.Rect(50,150, 200, 50)
            
            Solovetsky = pygame.Rect(50, 250, 200, 50)
            
            Norilsk= pygame.Rect(50, 350, 200, 50)
            
            Sevvostlag= pygame.Rect(50, 450, 200, 50)
            
            Pechorlag= pygame.Rect(50, 550, 200, 50)
            
            Karlag= pygame.Rect(50, 650, 200, 50)
            
            Altayskiy= pygame.Rect(50, 750, 200, 50)
            
            lista_botoes_gulags = [Trofimovsk,Solovetsky,Norilsk,Sevvostlag,Pechorlag,Karlag,Altayskiy]
            
            """
            Trofimovsk = desenhar_botao(screen, vermelho,200,50,50,150,"Trofimovsk")
            ma = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.65),int(screen.get_height()*0.13 ))))

            Solovetsky = desenhar_botao(screen, azul,200,50,50,250,"Solovetsky")
            mb = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.40),int(screen.get_height()*0.2 ))))
            
            Norilsk = desenhar_botao(screen, vermelho,200,50,50,350,"Norilsk")
            mc = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.54),int(screen.get_height()*0.16 ))))
            
            Sevvostlag = desenhar_botao(screen, azul,200,50,50,450,"Sevvostlag")
            md = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.83),int(screen.get_height()*0.2 ))))
            
            Pechorlag = desenhar_botao(screen, vermelho,200,50,50,550,"Norilsk")
            me = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.48),int(screen.get_height()*0.2 ))))
            
            Karlag = desenhar_botao(screen, azul,200,50,50,650,"Karlag")
            mf = desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.55),int(screen.get_height()*0.35 ))))
            
            Altayskiy = desenhar_botao(screen, vermelho,200,50,50,750,"Altayskiy")
            mg= desenhar_img(screen,'gulag3.png',(tamanho_mini),((int(screen.get_width()*0.60),int(screen.get_height()*0.32 ))))
            
            lista_botoes_gulags = [Trofimovsk,Solovetsky,Norilsk,Sevvostlag,Pechorlag,Karlag,Altayskiy]
            lista_mini_gulags = [ma,mb,mc,md,me,mf,mg]
            """
            
            #Loop para mostrar os botões e miniatura no mapa, incluindo o fato de quando são selecionados
            #Utiliza o num_gulag para bater a relação entre os índices
            num_gulag= 0
            for botao_gulag in lista_botoes_gulags:
                botao = pygame.draw.rect(screen, branco, botao_gulag)
                mini = pygame.image.load('imgs/'+lista_gulags[num_gulag].mini)
                if botao_gulag.collidepoint((mx,my)):
                    draw_text(lista_gulags[num_gulag].nome_r, preto,screen,center = botao.center)
                    mini = pygame.transform.scale(mini, (int(screen.get_width()*0.08),int(screen.get_height()*0.14)))
                    if click:
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
    
    