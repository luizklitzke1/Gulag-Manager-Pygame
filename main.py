#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
from general_functions import *
from general_classes import *
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
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#,FULLSCREEN | HWSURFACE | DOUBLEBUF)
sh= screen.get_height()
sw = screen.get_width() 


#Música de fundo
music = pygame.mixer.music.load("sounds/katyusha.mp3")
pygame.mixer.music.play(-1)

#Criação dos dados dos gulags
Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",((int(screen.get_width() *0.7),int(screen.get_height()*0.22 ))), foto="arnold.png")
Solovetsky = Campo("Solovetsky","Соловетскы",35,8,"Madeira",0,"Frio",((int(screen.get_width() *0.45),int(screen.get_height()*0.27 ))), foto="cash.jpg")
Norilsk = Campo("Norilsk","Норилск",15,3,"Mineração / Siderúrgica",3,"Muito Frio",((int(screen.get_width() *0.63),int(screen.get_height()*0.2 ))),foto="cash.jpg")
Sevvostlag = Campo("Sevvostlag","Севвостлаг",30,10,"Ouro e estanho",1,"Frio",((int(screen.get_width() *0.83),int(screen.get_height()*0.28 ))),foto="arnold.png")
Pechorlag = Campo("Pechorlag","Печорлаг",25,6,"Não",2,"Frio",((int(screen.get_width() *0.5),int(screen.get_height()*0.3 ))),foto="jo.jpg")
Karlag  = Campo("Karlag ","Карлаг",20,0,"Não",1,"Frio",((int(screen.get_width() *0.56),int(screen.get_height()*0.43 ))), foto="cash.jpg")
Altayskiy  = Campo("Altayskiy","Алтаыскиы",10,0,"Não",0,"Frio",((int(screen.get_width() *0.6),int(screen.get_height()*0.4 ))),foto="jo.jpg")

lista_gulags =[Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, Altayskiy ]

#Definição dos botões para os Gulags
w_botao = int(sw*0.15)
h_botao = int(sh*0.05)

margem_x = int(sw*0.03)

btn_Trofimovsk = Button(branco,margem_x,int(sh*0.2),w_botao,h_botao,"Trofimovsk","Трофимовск")
btn_Solovetsky = Button(branco,margem_x,int(sh*0.3),w_botao,h_botao,"Solovetsky","Трофимовск")
btn_Norilsk = Button(branco,margem_x,int(sh*0.4),w_botao,h_botao,"Norilsk","Трофимовск")
btn_Sevvostlag = Button(branco,margem_x,int(sh*0.5),w_botao,h_botao,"Sevvostlag","Трофимовск")
btn_Pechorlag = Button(branco,margem_x,int(sh*0.6),w_botao,h_botao,"Pechorlag","Трофимовск")
btn_Karlag = Button(branco,margem_x,int(sh*0.7),w_botao,h_botao,"Karlag","Трофимовск")
btn_Altayskiy = Button(branco,margem_x,int(sh*0.8),w_botao,h_botao,"Altayskiy","Трофимовск")

lista_botoes_gulags = [btn_Trofimovsk,btn_Solovetsky,btn_Norilsk,btn_Sevvostlag,btn_Pechorlag,btn_Karlag,btn_Altayskiy]

click = False

while True:
                    
    def menu_selecao():
        
        while True:
          
            screen.fill((0,0,0))
            
            draw_text('Selecione um Gulag', vermelho, screen, tamanho=int(sw*0.02), x=margem_x, y=int(sh*0.09))
            
    
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
    
            #Mostrar a imagem do mapa
            draw_img(screen,'map2.png',(int(sw*0.7),int(sh*0.7 )),(sw*0.25+10,int(sh*.2)))
            
            #Loop para mostrar os botões e miniatura no mapa, incluindo o fato de quando são selecionados
            #Utiliza o num_gulag para bater a relação entre os índices
            num_gulag= 0
            for botao_gulag in lista_botoes_gulags:
                mini = pygame.image.load('imgs/'+lista_gulags[num_gulag].mini)
                
                
                #Checa colisao com o mouse
                if botao_gulag.isOver((mx,my)):
                    
                    botao_gulag.draw(screen,rus=True)    
                    mini = pygame.transform.scale(mini, (swi(sw,.08),shi(sh,0.14)))
                    
                    if click:
                        btn1.play() 
                        mostrar_info_gulag(lista_gulags[num_gulag])
                else:
                    botao_gulag.draw(screen)
                    mini = pygame.transform.scale(mini, (swi(sw,.04),shi(sh,0.07)))
                    
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
                    if event.key == K_m:
                        if pygame.mixer.music.get_volume()==0:
                            pygame.mixer.music.set_volume(1)
                        else:
                            pygame.mixer.music.set_volume(0)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)
            
    def game(gulag):
        running = True

        while running:
            
            screen.fill((0,0,0))
            
            #draw_text(gulag.nome, vermelho, screen, tamanho=swi(sw,0.02), x=swi(sw,0.02), y=shi(sh,0.05))
            
            #Quadro do preview visual do campo
            sec_preview = draw_section(screen,swi(sw,.22,10),shi(sh,.05),swi(sw,.75),shi(sh,.68),8)
            
            gulag.demo_visual(screen,sw,sh)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_m:
                        if pygame.mixer.music.get_volume()==0:
                            pygame.mixer.music.set_volume(1)
                        else:
                            pygame.mixer.music.set_volume(0)
        
            pygame.display.update()
            mainClock.tick(60)
    
    #Mostra a informação básica do Gulag - Menu Geral 
    def mostrar_info_gulag(gulag):
    
        running = True
        click = False
        
        while running == True:
            
            screen.fill((0,0,0))
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
             
            #Painel lateral esquerda
            sec_esq = draw_section(screen,20,20,swi(sw,.45,-40),shi(sh,1,-40),8)
        
            w_bar = sw*.08
            #Gráfico para a detecção
            draw_graf_vert(screen,0,50,25,gulag.r_detec,shi(sh,.4),w_bar,swi(sw,.05),480,"dec","Detecção")
            #Gráfico para a nevasca
            draw_graf_vert(screen,0,5,3,gulag.r_nevasca,shi(sh,.4),w_bar,int(sw*.05*3.8),480,"dec","Nevasca")
            #Gráfico para os recursos
            draw_graf_vert(screen,0,10,5,gulag.recursos,shi(sh,.4),w_bar,int(sw*.05*6.5),480,"cres","Recursos")
            
            #Mostrar clima
            draw_text("Clima: "+str(gulag.clima), branco, screen, x=int(sw*.05), y=int(sh*.7), tamanho=int(sw*0.013))
            
            #Mostrar tipo de extração
            draw_text("Tipo de extração: ", branco, screen, x=int(sw*.05), y=int(sh*.8), tamanho=int(sw*0.013))
            draw_text(str(gulag.extracao), branco, screen, x=int(sw*.05), y=int(sh*.8+40), tamanho=int(sw*0.013))
            
            #Painel lateral direita
            sec_dir = draw_section(screen,swi(sw,.45,20),20,swi(sw,.55,-40),shi(sh,1,-40),8)
            
            #Mostrar a imagem do Gulag
            draw_img(screen,gulag.foto,(swi(sw,.55,-80),shi(sh,.6)),(swi(sw,.45,40),40))
            
            #Mostrar o nome do Gulag
            draw_text("Nome: "+str(gulag.nome),branco, screen, x=int(sw*.45+50), y=int(sh*.7), tamanho= int(sw*0.02))
            draw_text("Номе: "+str(gulag.nome_r),vermelho, screen, x=int(sw*.45+50), y=int(sh*.75), tamanho= int(sw*0.02))
            
            #Botão de escolher
            btn_iniciar = pygame.Rect(int(sw*.77) ,int(sh*0.85), int(sw*.2), int(sh*0.10))
            btn_iniciar=pygame.draw.rect(screen,vermelho,btn_iniciar)
            #Checa colisao com o mouse
            if btn_iniciar.collidepoint((mx,my)):
                draw_text("выбирать",branco,screen,tamanho= int(sw*0.02),center=btn_iniciar.center)
                if click:
                    btn1.play() 
                    gulag.load_imgs()
                    game(gulag)
            else:
                draw_text("Escolher",branco,screen,tamanho= int(sw*0.02),center=btn_iniciar.center)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_m:
                        if pygame.mixer.music.get_volume()==0:
                            pygame.mixer.music.set_volume(1)
                        else:
                            pygame.mixer.music.set_volume(0)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            pygame.display.update()
            mainClock.tick(30)
    
    def options():
        running = True
        while running:
            screen.fill((0,0,0))
            
    
            
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
    
    