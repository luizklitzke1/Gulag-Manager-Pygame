import pygame
from pygame.locals import *
from general_functions import load_frames

class Animation():
    
    def __init__(self,path,speed):
        
        self.ani_list = load_frames(path)
        
        self.ani_max = len(self.ani_list)-1
        self.ani_pos = 0
        
        self.frame = ani_list[0]
        
    #Atualizar o frame da animação - Separado para vel 0x funcionar
    def update_frame(self):
        
        self.frame = self.ani_list[self.ani_pos]
        
        if self.ani_pos == self.ani_max:
            self.ani_pos = 0
        else:
            self.ani_pos += 1
        
    #Representação visual da animação na tela
    def rep_visual(self,screen,size):
        
        self.frame = pygame.transform.scale(self.frame, escala)
        screen.blit(self.frame,pos)  
        
        