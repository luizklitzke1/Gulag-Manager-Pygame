
import pygame
from pygame.locals import *
from general_functions import *
import glob
import time


#Classe para a base de uma estrutura de um gulag
class Estrutura():
    
    def __init__(self,nome,alocados,path,lvl):
        self.id = id
        self.nome = nome
        self.nivel = lvl
        self.estado = 1  # 0-auxente 1-ativo  2-contrucao
        self.path = path
        
        self.alocados = 0
        
    #Carregar as texturas de exibição
    def load_textures(self):
        
        base_path = "imgs/gulags/" + self.path
        path = base_path + "/lvl" + str(self.nivel) + "/*.png"
        
        self.ani_list = load_frames(path)
        self.ani_max = len(self.ani_list)-1
        self.ani_pos = 0
        
        self.frame = self.ani_list[0]
        
    #Atualiza as posições da animação
    def update_frame(self):
        
        self.frame = self.ani_list[self.ani_pos]
        
        if self.ani_pos == self.ani_max:
            self.ani_pos = 0
        else:
            self.ani_pos += 1
        
    #Mostra o frame na tela
    def rep_visual(self,screen,escala,pos):
        
        self.frame = pygame.transform.scale(self.frame, escala)
        screen.blit(self.frame,pos)  
        
        
        
        
        
        
        
        
             
        