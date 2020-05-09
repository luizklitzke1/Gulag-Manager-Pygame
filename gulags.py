import pygame
from pygame.locals import *
from general_functions import *
from structures import *
import glob
import time


#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,nome_r,r_detec,recursos,extracao,r_nevasca,clima,minipos,mini="gulag3.png",foto="arnold.png", anim_speed=10):
        
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
        self.seguranca = 3
        self.medica = 1
        self.lazer = 0
             
        #Status do campo
        self.felicidade = 50
        self.prod_mensal = 0
        self.medo = 0   #Alterado por eventos especiais
        self.populacao = 0
        self.machucados = 0
        self.dinheiro = 420.69
        
        #Nome da foto do camp na tela de seleção
        self.foto = foto
        
        #Miniaturas na tela de seleção
        self.mini = mini
        self.minipos = minipos
        
        #Velocidade para a animação das representações visuais
        self.ani_speed_init = anim_speed
        self.ani_speed = self.ani_speed_init
        self.ani_pos = 0
        self.pause = False
        
        #Criação das estruturas do campo
        if self.extracao == "Madeira":
            rec = "madeira"
        else:
            rec = "mineracao"
            
        #Estruturas do campo em si    
            
        #Estruturas são meramente as representações visuais das partes do campo
        self.est_Recursos = Estrutura("recursos",0,("recursos/"+rec),1)
        self.est_Aloj = Estrutura("alojamento",0,"alojamento",1)
        self.est_Medic = Est_Medic("medico",0,"medico",1)
        self.est_Segur = Estrutura("seguranca",0,"seguranca",3)
    
    #Print dos dados de cada campo  
    def __repr__(self):
        return f"""\nNome: '{self.nome}', R. deteção: '{self.r_detec}', Recursos: '{self.recursos}'
                   Extração: '{self.extracao}', R. Nevasca: '{self.r_nevasca}', Clima: '{self.clima}'
                   Aquecedor: '{self.aquecedor}', Segurança: '{self.seguranca}', Medica: '{self.medica}', Lazer: '{self.lazer}'
                   Felicidade: '{self.felicidade}', Prod_Mensal: '{self.prod_mensal}', Medo: '{self.medo}'\n"""

    
    #Define a velocidad de atualização:
    def set_vel(self,vel):
        if vel > 0:
            self.pause = False
            self.ani_speed_init = 10/vel
        else:
            self.pause = True
            self.ani_speed_init = 0
        
    
    #Redefine as imagens que serão utilizadas para a representação
    #(Apenas chamada quando o campo for inicializado como jogavel)    
    def load_imgs(self):
        
        #Imgs gerais para display de info
        self.img_pop = pygame.image.load("imgs/pop1.png")
        self.img_hurt = pygame.image.load("imgs/hurt1.png")
        self.img_mon = pygame.image.load("imgs/mon1.png")
        
        #Texturas das estruturas
        self.est_Recursos.load_textures()
        self.est_Aloj.load_textures()
        self.est_Medic.load_textures()
        self.est_Segur.load_textures()
        
    #Mostra a representação visual animada do campo na tela de gameplay
    def demo_visual(self,screen,sw,sh,pos):   
        
        escala_geral = (swi(sw,.75),shi(sh,.68))
         
        if self.pause == False:
            self.ani_speed -= 1
            
            if self.ani_speed == 0:
            
                self.est_Aloj.update_frame()
                self.est_Recursos.update_frame()
                self.est_Medic.update_frame()
                self.est_Segur.update_frame()
                
                #Reset do contador
                self.ani_speed = self.ani_speed_init 
            
        self.est_Aloj.rep_visual(screen,escala_geral,pos)
        self.est_Recursos.rep_visual(screen,escala_geral,pos)
        self.est_Medic.rep_visual(screen,escala_geral,pos)
        self.est_Segur.rep_visual(screen,escala_geral,pos)
            
    