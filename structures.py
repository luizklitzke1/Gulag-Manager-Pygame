
import pygame
from pygame.locals import *
from general_functions import *
import glob

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
        
class Est_Medic(Estrutura):
    
    def __init__(self,nome,alocados,path,lvl):
        super().__init__("medico",0,"medico",1)
        
        self.doentes = 0
        self.chance_morte = .5
        self.leitos = 5
        self.vel_atend = 4
        
class Est_Recur(Estrutura)
    def __init__(self,path):
        super().__init__(path)
        
        self.estoque = 0
        self.vel_extract = 10
        self.risc_injur = .2
        
class Est_Aloj(Estrutura)
    def __init__(self,pat):
        super().__init__(path)
        
        self.qual_com = 1
        self.vel_extract = 10
        
class Est_Segur(Estrutura)
    def __init__(self,pat):
        super().__init__(path)
        
        self.arm = 1
        self.intimi = 1
        self.prison = 0   
        
        
        
             
        