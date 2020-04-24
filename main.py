#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo
from general_functions import *
from buttons import *
from calendario import Calendario
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
#music = pygame.mixer.music.load("sounds/katyusha.mp3")
#pygame.mixer.music.play(-1)

#Criação dos dados dos gulags
Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",((int(screen.get_width() *.7),int(screen.get_height()*.22 ))), foto="arnold.png")
Solovetsky = Campo("Solovetsky","Соловетскы",35,8,"Madeira",0,"Frio",((int(screen.get_width() *.45),int(screen.get_height()*.27 ))), foto="cash.jpg")
Norilsk = Campo("Norilsk","Норилск",15,3,"Mineração / Siderúrgica",3,"Muito Frio",((int(screen.get_width() *.63),int(screen.get_height()*.2 ))),foto="cash.jpg")
Sevvostlag = Campo("Sevvostlag","Севвостлаг",30,10,"Ouro e estanho",1,"Frio",((int(screen.get_width() *.83),int(screen.get_height()*.28 ))),foto="arnold.png")
Pechorlag = Campo("Pechorlag","Печорлаг",25,6,"Não",2,"Frio",((int(screen.get_width() *.5),int(screen.get_height()*.3 ))),foto="jo.jpg")
Karlag  = Campo("Karlag ","Карлаг",20,0,"Não",1,"Frio",((int(screen.get_width() *.56),int(screen.get_height()*.43 ))), foto="cash.jpg")
Altayskiy  = Campo("Altayskiy","Алтаыскиы",10,0,"Não",0,"Frio",((int(screen.get_width() *.6),int(screen.get_height()*.4 ))),foto="jo.jpg")

lista_gulags =[Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, Altayskiy]

#Definição dos botões para os Gulags
margem_x = int(sw*.03)
lista_botoes_gulags = setup_botoes_inicial(sh,sw)

#Criação do calendário
calendario = Calendario()

click = False

if True:
                    
    def menu_selecao():
        
        while True:
          
            screen.fill((0,0,0))
            
            draw_text('Selecione um Gulag', vermelho, screen, tamanho=int(sw*.02), x=margem_x, y=int(sh*.09))
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
    
            #Mostrar a imagem do mapa
            draw_img(screen,'map2.png',(int(sw*.7),int(sh*.7 )),(sw*.25+10,int(sh*.2)))
            
            #Loop para mostrar os botões e miniatura no mapa, incluindo o fato de quando são selecionados
            #Utiliza o num_gulag para bater a relação entre os índices
            num_gulag= 0
            for botao_gulag in lista_botoes_gulags:
                mini = pygame.image.load('imgs/'+lista_gulags[num_gulag].mini)
                
                #Checa colisao com o mouse
                if botao_gulag.isOver((mx,my)):
                    
                    botao_gulag.draw(screen,rus=True)    
                    mini = pygame.transform.scale(mini, (swi(sw,.08),shi(sh,.14)))
                    
                    if click == True:
                        btn1.play() 
                        mostrar_info_gulag(lista_gulags[num_gulag])
                else:
                    botao_gulag.draw(screen)
                    mini = pygame.transform.scale(mini, (swi(sw,.04),shi(sh,.07)))
                    
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
        lista_btns = setup_botoes_game(sh,sw)
        lista_vel = setup_botoes_vel(sh,sw)
        click = False

        while running:
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
            
            screen.fill((0,0,0))
            
            draw_text(gulag.nome, vermelho, screen, tamanho=swi(sw,.02), x=swi(sw,.013), y=shi(sh,.05))
            
            #Quadro do preview visual do campo
            sec_preview = draw_section(screen,swi(sw,.22,10),shi(sh,.15),swi(sw,.75),shi(sh,.68),8)
            gulag.demo_visual(screen,sw,sh,(swi(sw,.22,10),shi(sh,.15)))
            
            #Atualização do calendário
            calendario.update()
            calendario.rep_visual(screen,sw,sh)
            
            #Display dos dados de dinheiros e populacao
            tamanho_icones = (swi(sw,.045),swi(sw,.035))
            img_hurt = pygame.transform.scale(gulag.img_hurt,tamanho_icones)
            screen.blit(img_hurt,(swi(sw,.53),shi(sh,.05)))
            draw_text(gulag.machucados, branco, screen, tamanho=swi(sw,.017), x=swi(sw,.59), y=shi(sh,.07))
            
            img_pop = pygame.transform.scale(gulag.img_pop,tamanho_icones)
            screen.blit(img_pop,(swi(sw,.65), shi(sh,.05)))
            draw_text(gulag.populacao, branco, screen, tamanho=swi(sw,.017),x=swi(sw,.71), y=shi(sh,.07))
            
            img_mon = pygame.transform.scale(gulag.img_mon,tamanho_icones)
            screen.blit(img_mon,(swi(sw,.78), shi(sh,.05)))
            draw_text(str(gulag.dinheiro)+"коп", amarelo, screen,tamanho=swi(sw,.017), x=swi(sw,.84), y=shi(sh,.07))

            #Botões de ação da tela
            for btn in lista_btns:
                if btn.isOver((mx,my)):
                    btn.draw(screen,rus=True)
                else:
                    btn.draw(screen)
                    
            #Botões de velocidade
            for btn in lista_vel:
    
                #Verifica se a vel do btn está selecionada
                if ((calendario.ciclo==10 and btn.text=="1x")or
                    (calendario.ciclo==5 and btn.text=="2x") or 
                    (calendario.ciclo==2 and btn.text=="5x")):
                    btn.draw(screen,outline=vermelho)
                    
                else:
                    btn.draw(screen)
                    
                if btn.isOver((mx,my)):
                    if click == True:
                        if btn.text == "1x":
                            gulag.set_vel(1)
                            calendario.set_vel(1)
                        elif btn.text == "2x":
                            gulag.set_vel(2)
                            calendario.set_vel(2)
                        else:
                            gulag.set_vel(5)
                            calendario.set_vel(5)
                        btn1.play()    
                                 
            click = False 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause()
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
    #Tela de pause
    def pause():
        lista_btn_pause = setup_botoes_pause(sh,sw)
        paused = True 
        click = False
        
        while paused:
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
            
            screen.fill((0,0,255))   
            draw_text("Pause",vermelho,screen,tamanho=swi(sw,.05),center=(swi(sw,.5),shi(sh,.15))) 
    
            for btn in lista_btn_pause:
                btn.draw(screen)
                
                if btn.isOver((mx,my)):
                    if click == True:
                        
                        btn1.play()
                        if btn.text == "Resume":
                            paused = False
                            
                        if btn.text == "Opções":
                            options()
                        
                        if btn.text == "Sair do jogo":
                            pygame.quit()
                            sys.exit()
                        
                    
            draw_text("Precione ESCAPE para voltar ao jogo",branco,screen,tamanho=swi(sw,.015),center=(swi(sw,.5),shi(sh,.85)))  
            
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        paused = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            pygame.display.update()
            mainClock.tick(60)
                        
    #Tela de opções    
    def options():
        running = True
        lista_btn_res = setup_botoes_res(sh,sw)
        click = False
        
        while running:
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
            
            screen.fill((0,255,0))

            margem_x = swi(sw,.07)
            draw_text("Opções",vermelho,screen,tamanho=swi(sw,.025),x= margem_x, y = shi(sh,.1)) 
            
            draw_text("Tela cheia: ",branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.23)) 
            
            draw_text("Resolução da tela: ",branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.34)) 
            
            draw_text("Resolução da tela: " + str(screen.get_width()) +" X " +str(screen.get_height()),branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.8)) 
            
            #screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            for btn in lista_btn_res:
                
                res = btn.text.split("x")
                if screen.get_width() == int(res[0]):
                    
                    btn.draw(screen,outline=vermelho)
                else:
                    btn.draw(screen)
                
                if btn.isOver((mx,my)):
                    if click == True:
                        
                        if btn.text == "852x480":
                            pygame.display.set_mode((852,480))
                        
                        elif btn.text == "1280x720":
                            pygame.display.set_mode((1280,720))
                            pygame.display.flip()
                        
                        elif btn.text == "1365x768":
                            pygame.display.set_mode((1365,768))
                            pygame.display.flip()
                            
                        elif btn.text == "1600x900":
                            pygame.display.set_mode((1600,900))
                            pygame.display.flip()
                    
                        elif btn.text == "1920x1080":
                            pygame.display.set_mode((1920,1080))
                            pygame.display.flip()
            
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
        
            pygame.display.flip()
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
            
            draw_text("Clima: "+str(gulag.clima), branco, screen, x=int(sw*.05), y=int(sh*.7), tamanho=int(sw*.013))
            
            draw_text("Tipo de extração: ", branco, screen, x=int(sw*.05), y=int(sh*.8), tamanho=int(sw*.013))
            draw_text(str(gulag.extracao), branco, screen, x=int(sw*.05), y=int(sh*.8+40), tamanho=int(sw*.013))
            
            #Painel lateral direita
            sec_dir = draw_section(screen,swi(sw,.45,20),20,swi(sw,.55,-40),shi(sh,1,-40),8)
            
            draw_img(screen,gulag.foto,(swi(sw,.55,-80),shi(sh,.6)),(swi(sw,.45,40),40))
            
            draw_text("Nome: "+str(gulag.nome),branco, screen, x=int(sw*.45+50), y=int(sh*.7), tamanho= int(sw*.02))
            draw_text("Номе: "+str(gulag.nome_r),vermelho, screen, x=int(sw*.45+50), y=int(sh*.75), tamanho= int(sw*.02))
            
            #Botão de escolher
            #btn_iniciar = pygame.Rect(int(sw*.77) ,int(sh*.85), int(sw*.2), int(sh*.10))
            #btn_iniciar=pygame.draw.rect(screen,vermelho,btn_iniciar)
            btn_iniciar = Button(vermelho,swi(sw,.77),shi(sh,.85),swi(sw,.2),shi(sh,.1),"Escolher","выбирать",text_color=preto,text_size=swi(sw,.02))
            
            #Checa colisao com o mouse
            if btn_iniciar.isOver((mx,my)):
                btn_iniciar.draw(screen,rus=True) 
                
                if click == True:
                    btn1.play() 
                    gulag.load_imgs()
                    game(gulag)
                    
            else:
                btn_iniciar.draw(screen) 
            
            click = False
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
    
    #menu_selecao()
    lista_gulags[0].load_imgs()
    game(lista_gulags[0])
    