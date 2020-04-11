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

click = False

while True:
                    
    def menu_selecao():
        
        while True:
          
            screen.fill((0,0,0))
            margem_x = int(sw*0.03)
            draw_text('Selecione um Gulag', vermelho, screen, tamanho=int(sw*0.02), x=margem_x, y=int(sh*0.09))
            
    
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
    
            #Mostrar a imagem do mapa
            draw_img(screen,'map2.png',(int(sw*0.7),int(sh*0.7 )),(sw*0.25+10,int(sh*.2)))
            
            #Definição dos botões para os Gulags
            w_botao = int(sw*0.15)
            h_botao = int(sh*0.05)
            Trofimovsk = pygame.Rect(margem_x ,int(sh*0.20), w_botao, h_botao)
            Solovetsky = pygame.Rect(margem_x , int(sh*0.30), w_botao, h_botao)
            Norilsk= pygame.Rect(margem_x , int(sh*0.40), w_botao, h_botao)
            Sevvostlag= pygame.Rect(margem_x , int(sh*0.50), w_botao, h_botao)
            Pechorlag= pygame.Rect(margem_x , int(sh*0.60), w_botao, h_botao)
            Karlag= pygame.Rect(margem_x , int(sh*0.70), w_botao, h_botao)
            Altayskiy= pygame.Rect(margem_x , int(sh*0.80), w_botao, h_botao)
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
                    mini = pygame.transform.scale(mini, (int(sw*0.08),int(sh*0.14)))
                    if click:
                        btn1.play() 
                        mostrar_info_gulag(lista_gulags[num_gulag])
                    
                else:
                                 
                    draw_text(lista_gulags[num_gulag].nome, preto,screen,center = botao.center)
                    mini = pygame.transform.scale(mini, (int(sw*0.04),int(sh*0.07)))
                    
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
            #ret_esq = pygame.Rect(10, 10, sw*.45-10, screen.get_height()-20)
            #pygame.draw.rect(screen, azul, ret_esq)
            #ret_esq = draw_img(screen,"outline3.png",(int(sw*.45-10), int(sh-20)),(10,10))
            sec_esq = draw_section(screen,20,20,swi(sw,.45,-40),shi(sh,1,-40),8)
            
            w_bar = sw*.08
            
            #Cálcula da altura da representação do r_detec   0 até 50 
            altura_detec = -gulag.r_detec*(sh*.4/50)
            #Risco de detcção baixo
            if gulag.r_detec < 25 :
                visual_detec = pygame.Rect(int(sw*.05), 480, w_bar, altura_detec)
                pygame.draw.rect(screen, verde, visual_detec)
            #Risco de detcção alto
            if gulag.r_detec >= 25 :
                visual_detec = pygame.Rect(int(sw*.05), 480, w_bar, altura_detec)
                pygame.draw.rect(screen, vermelho, visual_detec)
            draw_text(gulag.r_detec, branco, screen, center=(visual_detec.centerx, visual_detec.bottom-20))   
            draw_text("Detecção", branco, screen, x=visual_detec.x, y=visual_detec.y+20)
            draw_text(str(gulag.r_detec)+"-50", branco, screen, x=visual_detec.x, y=visual_detec.y+40)
            
            
            #Cálcula da altura da representação do r_nevasca   de 0 até 5 
            altura_nevasca = -gulag.r_nevasca*(sh*.4/5)
            #Risco de nevasca baixo
            if gulag.r_nevasca < 3 :
                visual_nevasca = pygame.Rect(int(sw*.05*3.8), 480, w_bar, altura_nevasca)
                pygame.draw.rect(screen, verde, visual_nevasca)
            #Risco de nevasca alto
            if gulag.r_nevasca >= 3 :
                visual_nevasca = pygame.Rect(int(sw*.05*3.8), 480, w_bar, altura_nevasca)
                pygame.draw.rect(screen, vermelho, visual_nevasca)
            draw_text(gulag.r_nevasca, branco, screen, center=(visual_nevasca.centerx, visual_nevasca.bottom-20))   
            draw_text("Nevasca", branco, screen, x=visual_nevasca.x, y=visual_nevasca.y+20)
            draw_text(str(gulag.r_nevasca)+"-5", branco, screen, x=visual_nevasca.x, y=visual_nevasca.y+40)
            
            #Cálcula da altura da representação de aces_rec  0 até 10
            altura_rec = -gulag.recursos*(sh*.4/10)
            #Baixos recursos
            if gulag.recursos < 5 :
                visual_rec = pygame.Rect(int(sw*.05*6.5), 480, w_bar, altura_rec)
                pygame.draw.rect(screen, vermelho, visual_rec)
            #Altos recursos
            if gulag.recursos >= 5 :
                visual_rec = pygame.Rect(int(sw*.05*6.5), 480, w_bar, altura_rec)
                pygame.draw.rect(screen, verde, visual_rec)
            draw_text(gulag.recursos, branco, screen, center=(visual_rec.centerx, visual_rec.bottom-20))   
            draw_text("Recursos", branco, screen, x=visual_rec.x, y=visual_rec.y+20)
            draw_text(str(gulag.recursos)+"-10", branco, screen, x=visual_rec.x, y=visual_rec.y+40)
            
            #Mostrar clima
            draw_text("Clima: "+str(gulag.clima), branco, screen, x=int(sw*.05), y=int(sh*.7), tamanho=int(sw*0.013))
            
            #Mostrar tipo de extração
            draw_text("Tipo de extração: ", branco, screen, x=int(sw*.05), y=int(sh*.8), tamanho=int(sw*0.013))
            draw_text(str(gulag.extracao), branco, screen, x=int(sw*.05), y=int(sh*.8+40), tamanho=int(sw*0.013))
            
            #Painel lateral direita
            #ret_dir = pygame.Rect(sw*.45+10,10, sw*.55-20, 880)
            #pygame.draw.rect(screen, verde, ret_dir)
            #ret_dir = draw_img(screen,"outline3.png",(int(sw*.55-20), int(sh-20)),(int(sw*.45+10),10))
            sec_dir = draw_section(screen,swi(sw,.45,20),20,swi(sw,.55,-40),shi(sh,1,-40),8)
            
            #Mostrar a imagem do Gulag
            foto_gulag = pygame.image.load('imgs/'+str(gulag.foto))
            foto_gulag = pygame.transform.scale(foto_gulag, (int(sw*.55-80), int(sh*0.6)))
            screen.blit(foto_gulag, (sw*.45+40,40))
            
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
    
    