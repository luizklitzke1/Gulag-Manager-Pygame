#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial

#Inicia os gulags
lista_gulags = setup_inicial()
        
#Cores

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)

fullscreen = False

# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Gulag Manager')
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
 
font = pygame.font.SysFont(None, 20)



#Método para impressão de texto na tela
def draw_text(text, color, surface,tamanho=30, font=None, x=None, y=None, center=None):
    font = pygame.font.Font(font, tamanho)
    textobj = font.render(str(text), 10, color)
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
            #Reseta o índice caso passe de 6
            if num_gulag >= 6:
                num_gulag = 0
                    
            #Chama a renderização dos botões
            pygame.draw.rect(screen, (255, 0, 0), Trofimovsk)
            draw_text('Trofimovsk',branco, screen, center =Trofimovsk.center)
            pygame.draw.rect(screen, (0, 255, 0), Solovetsky)
            draw_text('Solovetsky',branco, screen, center =Solovetsky.center)
            pygame.draw.rect(screen, (255, 0, 0), Norilsk)
            draw_text('Norilsk',branco, screen, center =Norilsk.center)
            pygame.draw.rect(screen, (0, 255, 0), Sevvostlag)
            draw_text('Sevvostlag',branco, screen, center =Sevvostlag.center)
            pygame.draw.rect(screen, (255, 0, 0), Pechorlag)
            draw_text('Pechorlag',branco, screen, center =Pechorlag.center)
            pygame.draw.rect(screen, (0, 255, 0), Karlag)
            draw_text('Karlag',branco, screen, center =Karlag.center)
            pygame.draw.rect(screen, (255, 0, 0), Altayskiy)
            draw_text('Altayskiy',branco, screen, center =Altayskiy.center)
    
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
        
            #Painel lateral esquerda
            ret_esq = pygame.Rect(10, 10, 700, 880)
            pygame.draw.rect(screen, azul, ret_esq)
            #Cálcula da altura da representação do r_detec    max = 400px   cada ponto de 0 até 50 = 8
            altura_detec = gulag.r_detec*8
            #Risco de detcção baixo
            if gulag.r_detec < 3 :
                visual_detec = pygame.Rect(80, 480, 100, -altura_detec)
                pygame.draw.rect(screen, verde, visual_detec)
            #Risco de detcção alto
            if gulag.r_detec >= 3 :
                visual_detec = pygame.Rect(80, 480, 100, -altura_detec)
                pygame.draw.rect(screen, vermelho, visual_detec)
            draw_text(gulag.r_detec, branco, screen, center=(visual_detec.centerx, visual_detec.bottom-20))   
            draw_text("Risco de detecção", branco, screen, x=40, y=500)
            
            
            #Cálcula da altura da representação do r_nevasca    max = 400px   cada ponto de 0 até 5 
            altura_nevasca = gulag.r_nevasca*80
            #Risco de nevasca baixo
            if gulag.r_nevasca < 3 :
                visual_nevasca = pygame.Rect(290, 480, 100, -altura_nevasca)
                pygame.draw.rect(screen, verde, visual_nevasca)
            #Risco de nevasca alto
            if gulag.r_nevasca >= 3 :
                visual_nevasca = pygame.Rect(290, 480, 100, -altura_nevasca)
                pygame.draw.rect(screen, vermelho, visual_nevasca)
            draw_text(gulag.r_nevasca, branco, screen, center=(visual_nevasca.centerx, visual_nevasca.bottom-20))   
            draw_text("Risco de nevasca", branco, screen, x=250, y=500)
            
            
            #Cálcula da altura da representação de aces_rec    max = 400px   cada ponto de 0 até 10
            altura_rec = gulag.r_nevasca*40
            #Risco de nevasca baixo
            if gulag.r_nevasca < 5 :
                visual_rec = pygame.Rect(510, 480, 100, -altura_rec)
                pygame.draw.rect(screen, verde, visual_rec)
            #Risco de nevasca alto
            if gulag.r_nevasca >= 5 :
                visual_rec = pygame.Rect(510, 480, 100, -altura_rec)
                pygame.draw.rect(screen, vermelho, r_nevasca)
            draw_text(gulag.r_nevasca, branco, screen, center=(visual_rec.centerx, visual_rec.bottom-20))   
            draw_text("Risco de nevasca", branco, screen, x=480, y=500)
            
            #Mostrar clima
            draw_text("Clima: "+str(gulag.clima), branco, screen, x=40, y=600, tamanho=30)
            
            #Mostrar tipo de extração
            draw_text("Tipo de extração: "+str(gulag.extracao), branco, screen, x=40, y=700, tamanho=30)
            
            #Painel lateral direita
            ret_dir = pygame.Rect(720, 10, 870, 880)
            pygame.draw.rect(screen, verde, ret_dir)
            
            #Mostrar a imagem do Gulag
            foto_gulag = pygame.image.load('imgs/'+str(gulag.foto))
            foto_gulag = pygame.transform.scale(foto_gulag, (850, 600))
            screen.blit(foto_gulag, (730,20))
            
            #Mostrar o nome do Gulag
            draw_text("Nome: "+str(gulag.nome),branco, screen, x=730, y=640, tamanho= 60)
            
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