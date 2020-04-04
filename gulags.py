import pygame
from pygame.locals import *
from general_functions import *

#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,nome_r,r_detec,recursos,extracao,r_nevasca,clima,minipos,mini="gulag3.png",foto="arnold.png"):
        
        #Infor básica - imutável
        self.nome = nome
        self.nome_r = nome_r
        self.r_detec = r_detec
        self.recursos = recursos
        self.extracao = extracao
        self.r_nevasca = r_nevasca
        self.clima = clima
        
        #Valores a serem alterados com upgrades
        self.aquecedor = 0
        self.seguranca = 0
        self.medica = 0
        self.lazer = 0
             
        #Status do campo
        self.felicidade = 50
        self.prod_mensal = 0
        self.medo = 0   #Alterado por eventos especiais
        
        #Nome da foto
        self.foto = foto
        
        #Miniaturas
        self.mini = mini
        self.minipos = minipos
    
    #Print dos dados de cada campo  
    def __repr__(self):
        return f"""\nNome: '{self.nome}', R. deteção: '{self.r_detec}', Recursos: '{self.recursos}'
                   Extração: '{self.extracao}', R. Nevasca: '{self.r_nevasca}', Clima: '{self.clima}'
                   Aquecedor: '{self.aquecedor}', Segurança: '{self.seguranca}', Medica: '{self.medica}', Lazer: '{self.lazer}'
                   Felicidade: '{self.felicidade}', Prod_Mensal: '{self.prod_mensal}', Medo: '{self.medo}'\n"""
        
    #Mostra a informação básica do Gulag - Menu Gerla   
    def mostrar_info_gulag(self, screen, mainClock):
    
        running = True
        click = False
        while running == True:
            
            screen.fill((0,0,0))
            
            #Pega constantemente a posição do mouse 
            mx, my = pygame.mouse.get_pos()
             
            #Painel lateral esquerda
            #ret_esq = pygame.Rect(10, 10, screen.get_width()*.45-10, screen.get_height()-20)
            #pygame.draw.rect(screen, azul, ret_esq)
            ret_esq = desenhar_img(screen,"outline3.png",(int(screen.get_width()*.45-10), int(screen.get_height()-20)),(10,10))
            
            w_bar = screen.get_width()*.08
            
            #Cálcula da altura da representação do r_detec   0 até 50 
            altura_detec = -self.r_detec*(screen.get_height()*.4/50)
            #Risco de detcção baixo
            if self.r_detec < 25 :
                visual_detec = pygame.Rect(int(screen.get_width()*.05), 480, w_bar, altura_detec)
                pygame.draw.rect(screen, verde, visual_detec)
            #Risco de detcção alto
            if self.r_detec >= 25 :
                visual_detec = pygame.Rect(int(screen.get_width()*.05), 480, w_bar, altura_detec)
                pygame.draw.rect(screen, vermelho, visual_detec)
            draw_text(self.r_detec, branco, screen, center=(visual_detec.centerx, visual_detec.bottom-20))   
            draw_text("Detecção", branco, screen, x=visual_detec.x, y=visual_detec.y+20)
            draw_text(str(self.r_detec)+"-50", branco, screen, x=visual_detec.x, y=visual_detec.y+40)
            
            
            #Cálcula da altura da representação do r_nevasca   de 0 até 5 
            altura_nevasca = -self.r_nevasca*(screen.get_height()*.4/5)
            #Risco de nevasca baixo
            if self.r_nevasca < 3 :
                visual_nevasca = pygame.Rect(int(screen.get_width()*.05*3.8), 480, w_bar, altura_nevasca)
                pygame.draw.rect(screen, verde, visual_nevasca)
            #Risco de nevasca alto
            if self.r_nevasca >= 3 :
                visual_nevasca = pygame.Rect(int(screen.get_width()*.05*3.8), 480, w_bar, altura_nevasca)
                pygame.draw.rect(screen, vermelho, visual_nevasca)
            draw_text(self.r_nevasca, branco, screen, center=(visual_nevasca.centerx, visual_nevasca.bottom-20))   
            draw_text("Nevasca", branco, screen, x=visual_nevasca.x, y=visual_nevasca.y+20)
            draw_text(str(self.r_nevasca)+"-5", branco, screen, x=visual_nevasca.x, y=visual_nevasca.y+40)
            
            #Cálcula da altura da representação de aces_rec  0 até 10
            altura_rec = -self.recursos*(screen.get_height()*.4/10)
            #Baixos recursos
            if self.recursos < 5 :
                visual_rec = pygame.Rect(int(screen.get_width()*.05*6.5), 480, w_bar, altura_rec)
                pygame.draw.rect(screen, vermelho, visual_rec)
            #Altos recursos
            if self.recursos >= 5 :
                visual_rec = pygame.Rect(int(screen.get_width()*.05*6.5), 480, w_bar, altura_rec)
                pygame.draw.rect(screen, verde, visual_rec)
            draw_text(self.recursos, branco, screen, center=(visual_rec.centerx, visual_rec.bottom-20))   
            draw_text("Recursos", branco, screen, x=visual_rec.x, y=visual_rec.y+20)
            draw_text(str(self.recursos)+"-10", branco, screen, x=visual_rec.x, y=visual_rec.y+40)
            
            #Mostrar clima
            draw_text("Clima: "+str(self.clima), branco, screen, x=int(screen.get_width()*.05), y=int(screen.get_height()*.7), tamanho=int(screen.get_width()*0.013))
            
            #Mostrar tipo de extração
            draw_text("Tipo de extração: ", branco, screen, x=int(screen.get_width()*.05), y=int(screen.get_height()*.8), tamanho=int(screen.get_width()*0.013))
            draw_text(str(self.extracao), branco, screen, x=int(screen.get_width()*.05), y=int(screen.get_height()*.8+40), tamanho=int(screen.get_width()*0.013))
            
            #Painel lateral direita
            #ret_dir = pygame.Rect(screen.get_width()*.45+10,10, screen.get_width()*.55-20, 880)
            #pygame.draw.rect(screen, verde, ret_dir)
            ret_dir = desenhar_img(screen,"outline3.png",(int(screen.get_width()*.55-20), int(screen.get_height()-20)),(int(screen.get_width()*.45+10),10))
            
            #Mostrar a imagem do Gulag
            foto_gulag = pygame.image.load('imgs/'+str(self.foto))
            foto_gulag = pygame.transform.scale(foto_gulag, (int(screen.get_width()*.55-80), int(screen.get_height()*0.6)))
            screen.blit(foto_gulag, (screen.get_width()*.45+40,40))
            
            #Mostrar o nome do Gulag
            draw_text("Nome: "+str(self.nome),branco, screen, x=int(screen.get_width()*.45+50), y=int(screen.get_height()*.7), tamanho= int(screen.get_width()*0.02))
            draw_text("Номе: "+str(self.nome_r),vermelho, screen, x=int(screen.get_width()*.45+50), y=int(screen.get_height()*.75), tamanho= int(screen.get_width()*0.02))
            
            #Botão de escolher
            btn_iniciar = pygame.Rect(int(screen.get_width()*.77) ,int(screen.get_height()*0.85), int(screen.get_width()*.2), int(screen.get_height()*0.10))
            btn_iniciar=pygame.draw.rect(screen,vermelho,btn_iniciar)
            #Checa colisao com o mouse
            if btn_iniciar.collidepoint((mx,my)):
                draw_text("выбирать",branco,screen,tamanho= int(screen.get_width()*0.02),center=btn_iniciar.center)
                if click:
                    btn1.play() 
            else:
                draw_text("Escolher",branco,screen,tamanho= int(screen.get_width()*0.02),center=btn_iniciar.center)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        btn2.play() 
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            pygame.display.update()
            mainClock.tick(30)

def setup_inicial():
    
    lista_gulags = []

    #Criação dos dados dos gulags
    Trofimovsk = Campo("Trofimovsk",0,6,"Madeira",4,"Congelante", foto="arnold.png")
    Solovetsky = Campo("Solovetsky",35,8,"Madeira",0,"Frio", foto="cash.jpg")
    Norilsk = Campo("Norilsk",15,3,"Mineração / Siderúrgica",3,"Muito Frio",foto="cash.jpg")
    Sevvostlag = Campo("Sevvostlag",30,10,"Ouro e estanho",1,"Frio",foto="arnold.png")
    Pechorlag = Campo("Pechorlag",25,6,"Não",2,"Frio",foto="jo.jpg")
    Karlag  = Campo("Karlag ",20,0,"Não",1,"Frio", foto="cash.jpg")
    Altayskiy  = Campo("Altayskiy",10,0,"Não",0,"Frio", foto="jo.jpg")
    
    lista_gulags.extend([Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, Altayskiy ])
    
    return lista_gulags
    

if __name__ == "__main__":
    
    lista_gulags = setup_inicial()
    
    for campo in lista_gulags:
        print (campo)
        
        
    