import pygame
from pygame.locals import *
import general_functions as gf

#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,r_detec,recursos,extracao,r_nevasca,clima,minipos,mini="gulag3.png",foto="arnold.png"):
        
        #Infor básica - imutável
        self.nome = nome
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
        while running == True:
            screen.fill((0,0,0))
             
            #Painel lateral esquerda
            ret_esq = pygame.Rect(10, 10, screen.get_width()*0.45-10, screen.get_height()-20)
            pygame.draw.rect(screen, gf.azul, ret_esq)
            #Cálcula da altura da representação do r_detec    max = 400px   cada ponto de 0 até 50 = 8
            altura_detec = self.r_detec*-8
            #Risco de detcção baixo
            if self.r_detec < 3 :
                visual_detec = pygame.Rect(80, 480, 100, altura_detec)
                pygame.draw.rect(screen, gf.verde, visual_detec)
            #Risco de detcção alto
            if self.r_detec >= 3 :
                visual_detec = pygame.Rect(80, 480, 100, altura_detec)
                pygame.draw.rect(screen, gf.vermelho, visual_detec)
            gf.draw_text(self.r_detec, gf.branco, screen, center=(visual_detec.centerx, visual_detec.bottom-20))   
            gf.draw_text("Risco de detecção", gf.branco, screen, x=40, y=500)
            
            
            #Cálcula da altura da representação do r_nevasca    max = 400px   cada ponto de 0 até 5 
            altura_nevasca = self.r_nevasca*-80
            #Risco de nevasca baixo
            if self.r_nevasca < 3 :
                visual_nevasca = pygame.Rect(290, 480, 100, altura_nevasca)
                pygame.draw.rect(screen, gf.verde, visual_nevasca)
            #Risco de nevasca alto
            if self.r_nevasca >= 3 :
                visual_nevasca = pygame.Rect(290, 480, 100, altura_nevasca)
                pygame.draw.rect(screen, gf.vermelho, visual_nevasca)
            gf.draw_text(self.r_nevasca, gf.branco, screen, center=(visual_nevasca.centerx, visual_nevasca.bottom-20))   
            gf.draw_text("Risco de nevasca", gf.branco, screen, x=250, y=500)
            
            
            #Cálcula da altura da representação de aces_rec    max = 400px   cada ponto de 0 até 10
            altura_rec = self.r_nevasca*-40
            #Risco de nevasca baixo
            if self.r_nevasca < 5 :
                visual_rec = pygame.Rect(510, 480, 100, altura_rec)
                pygame.draw.rect(screen, gf.verde, visual_rec)
            #Risco de nevasca alto
            if self.r_nevasca >= 5 :
                visual_rec = pygame.Rect(510, 480, 100, altura_rec)
                pygame.draw.rect(screen, gf.vermelho, r_nevasca)
            gf.draw_text(self.r_nevasca, gf.branco, screen, center=(visual_rec.centerx, visual_rec.bottom-20))   
            gf.draw_text("Risco de nevasca", gf.branco, screen, x=480, y=500)
            
            #Mostrar clima
            gf.draw_text("Clima: "+str(self.clima), gf.branco, screen, x=40, y=600, tamanho=30)
            
            #Mostrar tipo de extração
            gf.draw_text("Tipo de extração: "+str(self.extracao), gf.branco, screen, x=40, y=700, tamanho=30)
            
            #Painel lateral direita
            ret_dir = pygame.Rect(screen.get_width()*0.45+10,10, screen.get_width()*0.55-20, 880)
            pygame.draw.rect(screen, gf.verde, ret_dir)
            
            #Mostrar a imagem do self
            foto_gulag = pygame.image.load('imgs/'+str(self.foto))
            foto_gulag = pygame.transform.scale(foto_gulag, (int(screen.get_width()*0.55-40), 600))
            screen.blit(foto_gulag, (screen.get_width()*0.45+20,20))
            
            #Mostrar o nome do Gulag
            gf.draw_text("Nome: "+str(self.nome),gf.branco, screen, x=screen.get_width()*0.45+20, y=640, tamanho= 60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
            pygame.display.update()
            mainClock.tick(30)

def setup_inicial():
    
    lista_gulags = []

    #Criação dos dados dos gulags
    Trofimovsk = Campo("Trofimovsk",0,6,"Madeira",4,"Congelante", foto="arnold.png")
    Solovetsky = Campo("Solovetsky",35,8,"Madeira",0,"Frio", foto="cash.jpg")
    Norilsk = Campo("Norilsk",15,3,"Mineração de Ferro / Trabalho em Siderúrgica",3,"Muito Frio",foto="cash.jpg")
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
        
        
    