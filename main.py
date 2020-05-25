#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo
from general_functions import *
from buttons import *
from calendario import Calendario
from upgrades import upg_list
from characters import lista_char
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
global sh, sw
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


#Criação do calendário
calendario = Calendario()

click = False
   
def menu_selecao():
    
    global sh, sw
    
    #Setup dos botões
    margem_x = swi(sw,.03)
    w_botao = swi(sw,.15)
    h_botao = shi(sh,.08)
    btn_Trofimovsk = Button(branco,margem_x,shi(sh,.2),w_botao,h_botao,"Trofimovsk","Трофимовск")
    btn_Solovetsky = Button(branco,margem_x,shi(sh,.3),w_botao,h_botao,"Solovetsky","Соловетскы")
    btn_Norilsk = Button(branco,margem_x,shi(sh,.4),w_botao,h_botao,"Norilsk","Норилск")
    btn_Sevvostlag = Button(branco,margem_x,shi(sh,.5),w_botao,h_botao,"Sevvostlag","Севвостлаг")
    btn_Pechorlag = Button(branco,margem_x,shi(sh,.6),w_botao,h_botao,"Pechorlag","Печорлаг")
    btn_Karlag = Button(branco,margem_x,shi(sh,.7),w_botao,h_botao,"Karlag","Карлаг")
    btn_Altayskiy = Button(branco,margem_x,shi(sh,.8),w_botao,h_botao,"Altayskiy","Алтаыскиы")
    
    lista_botoes_gulags = [btn_Trofimovsk,btn_Solovetsky,btn_Norilsk,btn_Sevvostlag,btn_Pechorlag,btn_Karlag,btn_Altayskiy]

    
    while True:
        
        screen.fill((0,0,0))
        
        draw_text('Selecione um Gulag', vermelho, screen, tamanho=swi(sw,.02), x=margem_x, y=int(sh*.09))
        
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()

        #Mostrar a imagem do mapa
        draw_img(screen,'map2.png',(swi(sw,.7),int(sh*.7 )),(sw*.25+10,int(sh*.2)))
        
        #Loop para mostrar os botões e miniatura no mapa, incluindo o fato de quando são selecionados
        #Utiliza o num_gulag para bater a relação entre os índices

        w_botao = swi(sw,.15)
        h_botao = shi(sh,.08)
        for botao_gulag in lista_botoes_gulags:
            
            num_gulag = lista_botoes_gulags.index(botao_gulag)
            
            mini = pygame.image.load('imgs/'+lista_gulags[num_gulag].mini)
            
            #Checa colisao com o mouse
            if botao_gulag.isOver((mx,my)):
                
                botao_gulag.draw(screen,margem_x,shi(sh,(.2+.1*num_gulag)),w_botao,h_botao,rus=True)    
                mini = pygame.transform.scale(mini, (swi(sw,.08),shi(sh,.14)))
                
                if click == True:
                    btn1.play() 
                    mostrar_info_gulag(lista_gulags[num_gulag])
            else:
                botao_gulag.draw(screen,margem_x,shi(sh,(.2+.1*num_gulag)),w_botao,h_botao)
                mini = pygame.transform.scale(mini, (swi(sw,.04),shi(sh,.07)))
                
            #Cria um rect com a img para poder reposicionar corretamente
            mini_rect = mini.get_rect(center=lista_gulags[num_gulag].minipos)
            screen.blit(mini, mini_rect)
                
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
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

#Tela principal do jogo  
def game(gulag):
    running = True
    click = False
    
    global sh, sw
    
    #Setup dos botões gerais
    margem_x = swi(sw,.015)
    w_botao = swi(sw,.17)
    h_botao = shi(sh,.08)
    btn_status= Button(branco,margem_x,shi(sh,.15,-8),w_botao,h_botao,"Status","Статус")
    btn_recursos = Button(branco,margem_x,shi(sh,.25,-8),w_botao,h_botao,"Recursos","Рецурсос")
    btn_upgrades= Button(branco,margem_x,shi(sh,.35,-8),w_botao,h_botao,"Upgrades","Упградес")
    
    lista_btns = [btn_status,btn_recursos,btn_upgrades]
    
    #Setup dos botões de velocidade
    margem_x = swi(sw,.675)
    margem_y = shi(sh,.85)
    w_botao = swi(sw,.07)
    h_botao = shi(sh,.08)
    btn_0x = Button(branco,margem_x,margem_y,w_botao,h_botao,"0x",text_size=swi(sw,.013))
    btn_1x = Button(branco,margem_x+w_botao+10,margem_y,w_botao,h_botao,"1x",text_size=swi(sw,.013))
    btn_2x = Button(branco,margem_x+w_botao*2+20,margem_y,w_botao,h_botao,"2x",text_size=swi(sw,.013))
    btn_5x = Button(branco,margem_x+w_botao*3+30,margem_y,w_botao,h_botao,"5x",text_size=swi(sw,.013))
    
    lista_vel = [btn_0x,btn_1x,btn_2x,btn_5x]
    
    
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
        screen.blit(img_mon,(swi(sw,.75), shi(sh,.05)))
        draw_text(str(gulag.dinheiro)+"коп", amarelo, screen,tamanho=swi(sw,.017), x=swi(sw,.81), y=shi(sh,.07))

        #Botões de ação da tela
        for btn in lista_btns:
            w_botao = swi(sw,.17)
            h_botao = shi(sh,.08)
            margem_x = swi(sw,.015)
            margem_y = shi(sh,(.15+0.1*lista_btns.index(btn)),-8)
            if btn.isOver((mx,my)):
                btn.draw(screen,rus=True)
            else:
                btn.draw(screen,margem_x,margem_y,w_botao,h_botao)
                
        #Botões de velocidade
        for btn in lista_vel:
            
            margem_x = swi(sw,.675)
            margem_y = shi(sh,.85)
            w_botao = swi(sw,.07)
            h_botao = shi(sh,.08)
            pos = lista_vel.index(btn)
            x_btn = (margem_x+(w_botao*pos)) + (10*(pos+1))

            #Verifica se a vel do btn está selecionada
            if ((calendario.pause==True and btn.text=="0x") or
                (calendario.ciclo==10 and btn.text=="1x")or
                (calendario.ciclo==5 and btn.text=="2x") or 
                (calendario.ciclo==2 and btn.text=="5x")):
                
                btn.draw(screen,x_btn,margem_y,w_botao,h_botao,text_size=swi(sw,.013)
                         ,outline=vermelho)

            else:
                
                btn.draw(screen,x_btn,margem_y,w_botao,h_botao,text_size=swi(sw,.013))
                
            if btn.isOver((mx,my)) and click == True:
                if btn.text == "0x":
                    gulag.set_vel(0)
                    calendario.set_vel(0)
                elif btn.text == "1x":
                    gulag.set_vel(1)
                    calendario.set_vel(1)
                elif btn.text == "2x":
                    gulag.set_vel(2)
                    calendario.set_vel(2)
                else:
                    gulag.set_vel(5)
                    calendario.set_vel(5)
                btn1.play()    
                    
        #Botões de gameplay
        for btn in lista_btns:
                
            btn.draw(screen)
                
            if btn.isOver((mx,my)) and click == True:
                if btn.text == "Status":
                    pass
                elif btn.text == "Recursos":
                    pass
                elif btn.text == "Upgrades":
                        upgrades_choose(gulag)
                                
        click = False 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
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
    paused = True 
    click = False
    global sh, sw
    global lista_btn_pause
    lista_btn_pause = setup_botoes_pause(sh,sw)
    
    while paused:
    
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
        
        screen.fill((0,0,0))   
        draw_text("Pause",vermelho,screen,tamanho=swi(sw,.05),center=(swi(sw,.5),shi(sh,.15))) 

        for btn in lista_btn_pause:
            btn.draw(screen)
            
            if btn.isOver((mx,my)) and click == True:

                if btn.text == "Resume":
                    paused = False
                    
                elif btn.text == "Opções":
                    options()
                
                if btn.text == "Menu inicial":
                    menu_selecao()
                
                elif btn.text == "Sair do jogo":
                    pygame.quit()
                    sys.exit()
                    
                
        draw_text("Precione ESCAPE para voltar ao jogo",branco,screen,tamanho=swi(sw,.015),center=(swi(sw,.5),shi(sh,.85)))  
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
                    paused = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        mainClock.tick(60)

#Tela de upgrades - escolha de div  
def upgrades_choose(gulag):
    running = True
    click = False
    global sh, sw
    
    while running:
        
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
        
        screen.fill((0,0,0))
        draw_text("Upgrades - Escolha a área: ",vermelho,screen,tamanho=swi(sw,.02),
                  x= swi(sw,.05), y = shi(sh,.1)) 

        margem_y = shi(sh,.23)
        
        for char in lista_char:
            
            larg = swi(sw,.21)
            esp_x = swi(sw,.05) +larg*lista_char.index(char)*1.1
            draw_section(screen,esp_x,margem_y,larg,shi(sh,.6),5)
            
            btn_y = margem_y + shi(sh,.5)
            char.rep_visual(screen,(larg,shi(sh,.5)),(esp_x,margem_y))
            char.btn_chs.draw(screen,esp_x,btn_y,larg,shi(sh,0.1),outline=branco)
            
            if char.btn_chs.isOver((mx,my)) and click == True:
                upgrades_esp(gulag,char)
            
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
        pygame.display.flip()
        mainClock.tick(60)
            

#Tela de upgrades específicos   
def upgrades_esp(gulag,char):
    running = True
    click = False
    global sh, sw
    
    while running:
        
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
        
        screen.fill((0,0,0))
        margem_x = swi(sw,.03)
        draw_text(char.div,vermelho,screen,tamanho=swi(sw,.02),x= margem_x, y = shi(sh,.05)) 

        margem_y = shi(sh,.18)
        for upgrade in upg_list:
            
            if upg_list.index(upgrade) %2 == 0:
                margem_x_up = margem_x
            else:
                margem_x_up = margem_x + swi(sw,.34)
                
            if upg_list.index(upgrade) <2:
                margem_y_up = margem_y
            else:
                margem_y_up = margem_y + shi(sh,.35)
                
            upgrade.rep_visual(screen,sw,sh,margem_x_up,margem_y_up)
            
            if upgrade.botao.isOver((mx,my)) and click == True:
                upgrade.botao.color = verde
                upgrade.apply_effec(gulag)
                btn3.play()
                upg_list.remove(upgrade)
             
        char.rep_visual(screen,(swi(sw,.21),shi(sh,.5)),(swi(sw,.75),shi(sh,.18)))           
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
        pygame.display.flip()
        mainClock.tick(60)
        
            
#Tela de opções    
def options():
    running = True
    click = False
    
    global lista_btn_pause
    global sh, sw
    
    #Setup dos botões
    checkbox_fc = Checkbox(swi(sw,.275),shi(sh,.226),swi(sw,0.019),swi(sw,0.019))
    margem_x = swi(sw,.07)
    margem_y = shi(sh,.4)
    w_botao = swi(sw,.13)
    h_botao = shi(sh,.08)
    btn_1 = Button(branco,margem_x,margem_y,w_botao,h_botao,"1280x720",text_size=swi(sw,.013))
    btn_2 = Button(branco,margem_x+w_botao+10,margem_y,w_botao,h_botao,"1365x768",text_size=swi(sw,.013))
    btn_3 = Button(branco,margem_x+w_botao*2+20,margem_y,w_botao,h_botao,"1600x900",text_size=swi(sw,.013))
    btn_4 = Button(branco,margem_x+w_botao*3+30,margem_y,w_botao,h_botao,"1920x1080",text_size=swi(sw,.013))
    btn_5 = Button(branco,margem_x+w_botao*4+40,margem_y,w_botao,h_botao,"2560x1080",text_size=swi(sw,.013))

    lista_btn_res = [btn_1,btn_2,btn_3,btn_4,btn_5]
    
    while running:
        
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
        
        screen.fill((0,0,0))
        margem_x = swi(sw,.07)
        draw_text("Opções",vermelho,screen,tamanho=swi(sw,.02),x= margem_x, y = shi(sh,.1)) 
        
        draw_text("Tela cheia: ",branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.23)) 
        checkbox_fc.draw(screen)
        
        if checkbox_fc.isOver((mx,my)) and click == True:
            checkbox_fc.checked = not(checkbox_fc.checked)
            if checkbox_fc.checked == True:
                pygame.display.set_mode((sw,sh),FULLSCREEN)
            else:
                pygame.display.set_mode((sw,sh))
            
        
        draw_text("Resolução da tela: ",branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.34)) 
        
        draw_text("Resolução da tela: " + str(screen.get_width()) +" X " +str(screen.get_height()),branco,screen,tamanho=swi(sw,.018),x=margem_x, y = shi(sh,.8)) 
        
        margem_x = swi(sw,.07)
        margem_y = shi(sh,.4)
        w_botao = swi(sw,.13)
        h_botao = shi(sh,.08)
        #screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        for btn in lista_btn_res:
            
            res = btn.text.split("x")
            
            num_btn = lista_btn_res.index(btn)
            x_btn = margem_x+ (w_botao*num_btn)+(10*num_btn)
            
            if screen.get_width() == int(res[0]):
                btn.draw(screen,x_btn,margem_y,w_botao,h_botao,
                         outline=vermelho)
            else:
                btn.draw(screen,x_btn,margem_y,w_botao,h_botao)
            
            if btn.isOver((mx,my)) and click == True:
                    
                if checkbox_fc.checked == True:
                    pygame.display.set_mode((int(res[0]),int(res[1])),FULLSCREEN)
                else:
                    pygame.display.set_mode((int(res[0]),int(res[1])))
                sw = screen.get_width()
                sh = screen.get_height()

                lista_btn_pause = setup_botoes_pause(sh,sw)
                calendario.reload_x(screen,sw,sh)
                checkbox_fc = Checkbox(swi(sw,.275),shi(sh,.226),
                                        swi(sw,0.019),swi(sw,0.019),checked=checkbox_fc.checked)

        pygame.display.flip()
                        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
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
    global sh, sw
    btn_bk = Button(branco,swi(sw,.03),shi(sh,.05),swi(sw,.1),shi(sh,.08),"Voltar",text_rus="убирйс")
    btn_iniciar = Button(vermelho,swi(sw,.77),shi(sh,.85),swi(sw,.2),shi(sh,.1),
                         "Escolher","выбирать",text_color=preto,text_size=swi(sw,.02))
    
    while running == True:
        
        screen.fill((0,0,0))
        
        #Pega constantemente a posição do mouse 
        mx, my = pygame.mouse.get_pos()
            
        #Painel lateral esquerda
        sec_esq = draw_section(screen,20,20,swi(sw,.45,-40),shi(sh,1,-40),8)
    
        if btn_bk.isOver((mx,my)):
            btn_bk.draw(screen,swi(sw,.03),shi(sh,.05),swi(sw,.1),shi(sh,.08),rus=True)
            if click == True:  
                btn1.play()
                running = False
        else:
            btn_bk.draw(screen,swi(sw,.03),shi(sh,.05),swi(sw,.1),shi(sh,.08))
        w_bar = sw*.08
        y_bar = shi(sh,.55)
        #Gráfico para a detecção
        draw_graf_vert(screen,0,50,25,gulag.r_detec,shi(sh,.4),w_bar,swi(sw,.05),y_bar,"dec","Detecção")
        #Gráfico para a nevasca
        draw_graf_vert(screen,0,5,3,gulag.r_nevasca,shi(sh,.4),w_bar,swi(sw,(.05*3.8)),y_bar,"dec","Nevasca")
        #Gráfico para os recursos
        draw_graf_vert(screen,0,10,5,gulag.recursos,shi(sh,.4),w_bar,swi(sw,(.05*6.5)),y_bar,"cres","Recursos")
        
        draw_text("Clima: "+str(gulag.clima), branco, screen, x=swi(sw,.05), y=shi(sh,.7), tamanho=swi(sw,.013))
        
        draw_text("Tipo de extração: ", branco, screen, x=swi(sw,.05), y=shi(sh,.8), tamanho=swi(sw,.013))
        draw_text(str(gulag.extracao), branco, screen, x=swi(sw,.05), y=shi(sh,.8,40), tamanho=swi(sw,.013))
        
        #Painel lateral direita
        sec_dir = draw_section(screen,swi(sw,.45,20),20,swi(sw,.55,-40),shi(sh,1,-40),8)
        
        draw_img(screen,gulag.foto,(swi(sw,.55,-80),shi(sh,.6)),(swi(sw,.45,40),40))
        
        draw_text("Nome: "+str(gulag.nome),branco, screen, x=swi(sw,.45+50), y=int(sh*.7), tamanho= swi(sw,.02))
        draw_text("Номе: "+str(gulag.nome_r),vermelho, screen, x=swi(sw,.45+50), y=int(sh*.75), tamanho= swi(sw,.02))
        
        #Checa colisao com o mouse
        if btn_iniciar.isOver((mx,my)):
            
            btn_iniciar.draw(screen,swi(sw,.77),shi(sh,.85),swi(sw,.2),shi(sh,.1),
                             text_size=swi(sw,.02),rus=True) 
            if click == True:
                btn2.play() 
                gulag.load_imgs()
                game(gulag)
        else:
            btn_iniciar.draw(screen,swi(sw,.77),shi(sh,.85),swi(sw,.2),shi(sh,.1),
                             text_size=swi(sw,.02)) 
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_TAB:
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
    