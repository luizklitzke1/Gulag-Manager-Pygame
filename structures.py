
import pygame
from pygame.locals import *
from general_functions import *
from animations import Animation

#Classe para a base de uma estrutura de um gulag
class Estrutura():
    
    def __init__(self,nome,alocados,path,lvl):
        self.id = id
        self.nome = nome
        self.nivel = lvl
        self.estado = 1  # 0-auxente 1-ativo  2-contrucao
        self.path = path
        
        self.current_ani = None
        
        self.alocados = 0
        
    #Carregar as texturas de exibição
    def load_textures(self):
        
        base_path = "imgs/gulags/" + self.path
        path = base_path + "/lvl" + str(self.nivel) + "/*.png"
        
        self.ani_normal = Animation(path)
        self.current_ani = self.ani_normal
        
    #Atualiza as posições da animação
    def update_frame(self):
        
        self.current_ani.update_frame()
        
    #Mostra o frame na tela
    def rep_visual(self,screen,escala,pos):
        
        self.current_ani.rep_visual(screen,escala,pos)
        
class Est_Medic(Estrutura):
    
    def __init__(self,path):
        super().__init__("medico",0,path,1)
        
        self.doentes = 0
        self.chance_morte = .5
        self.leitos = 5
        self.vel_atend = 4
        
class Est_Recur(Estrutura):
    def __init__(self,path):
        super().__init__("recursos",0,path,1)
        
        self.estoque = 0
        self.vel_extract = 10
        self.risc_injur = .2
        
class Est_Aloj(Estrutura):
    def __init__(self,path):
        super().__init__("alojamento",0,path,1)
        
        self.qual_com = 1
        self.vel_extract = 10
        
class Est_Segur(Estrutura):
    def __init__(self,path):
        super().__init__("seguranca",0,path,3)
        
        self.arm = 1
        self.intimi = 1
        self.prison = 0   
        
        
        
             
        