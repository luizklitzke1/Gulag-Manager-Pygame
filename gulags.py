import pygame
from pygame.locals import *
from general_functions import *
import glob
import time


#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,nome_r,r_detec,recursos,extracao,r_nevasca,clima,minipos,mini="gulag3.png",foto="arnold.png", anim_speed=40):
        
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
        
        #Nome da foto do camp na tela de seleção
        self.foto = foto
        
        #Miniaturas na tela de seleção
        self.mini = mini
        self.minipos = minipos
        
        #Velocidade para a animação das representações visuais
        self.ani_speed_init = anim_speed
        self.ani_speed = self.ani_speed_init
        self.ani_pos = 0
    
    #Redefine as imagens que serão utilizadas para a representação
    #(Apenas chamada quando o campo for inicializado como jogavel)    
    def load_imgs(self):
        if self.extracao == "Madeira":
            self.ani_rec = glob.glob("imgs/gulags/recursos/madeira/m_*.png")
            self.ani_rec.sort()
            self.ani_rec_pos = 0
            self.ani_rec_max = len(self.ani_rec)-1
    
    #Print dos dados de cada campo  
    def __repr__(self):
        return f"""\nNome: '{self.nome}', R. deteção: '{self.r_detec}', Recursos: '{self.recursos}'
                   Extração: '{self.extracao}', R. Nevasca: '{self.r_nevasca}', Clima: '{self.clima}'
                   Aquecedor: '{self.aquecedor}', Segurança: '{self.seguranca}', Medica: '{self.medica}', Lazer: '{self.lazer}'
                   Felicidade: '{self.felicidade}', Prod_Mensal: '{self.prod_mensal}', Medo: '{self.medo}'\n"""

    #Mostra a representação visual animada do campo na tela de gameplay
    def demo_visual(self,screen):    
        self.ani_speed -= 1
        print("Speed: ", self.ani_speed)
        
        if True:
        
            if self.recursos:
                print("Pos: ", self.ani_rec_pos)
                print("Img: ", self.ani_rec[self.ani_rec_pos])
                img_rec = pygame.image.load(self.ani_rec[self.ani_rec_pos])
                
                screen.blit(img_rec,(250,250))
                time.sleep(0.5)
                if self.ani_rec_pos == self.ani_rec_max:
                    self.ani_rec_pos = 0
                else:
                    self.ani_rec_pos += 1
            
            print("RESEEEEET")
            self.ani_speed = self.ani_speed_init   
            


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
        
        
    