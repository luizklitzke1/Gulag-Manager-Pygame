import pygame
from pygame.locals import *
from general_functions import *
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
        
        #Extração
        if self.extracao:
            if self.extracao == "Madeira":
                path = ("imgs/gulags/recursos/madeira/m_*.png")
            if self.extracao == "Mineração / Siderúrgica":
                path = ("imgs/gulags/recursos/mineracao/m_*.png")
            self.ani_rec = load_frames(path)
            self.ani_rec_pos = 0
            self.ani_rec_max = len(self.ani_rec)-1
            self.img_rec = self.ani_rec[0]
            
        #Alojamento
        self.ani_alo = load_frames("imgs/gulags/alojamento/a_*.png")
        self.ani_alo_pos = 0
        self.ani_alo_max = len(self.ani_alo)-1 
        self.img_alo =  self.ani_alo[0] 
        
        #Médico
        if self.medica != 0:
            self.ani_med = load_frames("imgs/gulags/medico/lvl"+str(self.medica)+"/m_*.png")
            self.ani_med_pos = 0
            self.ani_med_max = len(self.ani_med)-1
            self.img_med = self.ani_med[0]
        
        #Segurança
        if self.seguranca != 0:
            self.ani_seg = load_frames("imgs/gulags/seguranca/lvl"+str(self.seguranca)+"/s_*.png")
            self.ani_seg_pos = 0
            self.ani_seg_max = len(self.ani_seg)-1
            self.img_seg = self.ani_seg[0]
        
    #Print dos dados de cada campo  
    def __repr__(self):
        return f"""\nNome: '{self.nome}', R. deteção: '{self.r_detec}', Recursos: '{self.recursos}'
                   Extração: '{self.extracao}', R. Nevasca: '{self.r_nevasca}', Clima: '{self.clima}'
                   Aquecedor: '{self.aquecedor}', Segurança: '{self.seguranca}', Medica: '{self.medica}', Lazer: '{self.lazer}'
                   Felicidade: '{self.felicidade}', Prod_Mensal: '{self.prod_mensal}', Medo: '{self.medo}'\n"""

    #Mostra a representação visual animada do campo na tela de gameplay
    def demo_visual(self,screen,sw,sh):   
         
        self.ani_speed -= 1
        
        escala_geral = (swi(sw,.75),shi(sh,.68))
        
        if self.ani_speed == 0:
        
            #Img dos rescuros
            if self.recursos:
                self.img_rec = self.ani_rec[self.ani_rec_pos]
                
                if self.ani_rec_pos == self.ani_rec_max:
                    self.ani_rec_pos = 0
                else:
                    self.ani_rec_pos += 1
            
            #Img do alojamento
            self.img_alo = self.ani_alo[self.ani_alo_pos]
            if self.ani_alo_pos == self.ani_alo_max:
                self.ani_alo_pos = 0
            else:
                self.ani_alo_pos += 1

            #Img do medico
            if self.medica != 0:
                self.img_med = self.ani_med[self.ani_med_pos]
                if self.ani_med_pos == self.ani_med_max:
                    self.ani_med_pos = 0
                else:
                    self.ani_med_pos += 1
                   
            #Img da seguranca
            if self.seguranca != 0:
                self.img_seg = self.ani_seg[self.ani_seg_pos]
                if self.ani_seg_pos == self.ani_seg_max:
                    self.ani_seg_pos = 0
                else:
                    self.ani_seg_pos += 1
                     
            #Reset do contador
            self.ani_speed = self.ani_speed_init 
        
        self.img_rec = pygame.transform.scale(self.img_rec, escala_geral)
        screen.blit(self.img_rec,(swi(sw,.22,20),shi(sh,0.06)))    
        
        self.img_alo = pygame.transform.scale(self.img_alo, escala_geral)
        screen.blit(self.img_alo,(swi(sw,.22,20),shi(sh,0.06))) 
        
        if self.medica != 0:
            self.img_med = pygame.transform.scale(self.img_med, escala_geral)
            screen.blit(self.img_med,(swi(sw,.22,20),shi(sh,0.06))) 
            
        if self.seguranca != 0:
            self.img_seg = pygame.transform.scale(self.img_seg, escala_geral)
            screen.blit(self.img_seg,(swi(sw,.22,20),shi(sh,0.06)))
    
        
    