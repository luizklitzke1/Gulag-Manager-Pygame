import pygame
from pygame.locals import *
from general_functions import *
from animations import Animation

class Character():
    
    def __init__(self,id,speed):
        
        self.id = id
        self.speed = speed
        
        self.base_path = "imgs/characters/" + self.id + "/"
        
        self.ani_general = Animation(self.base_path+"general/*png",speed=self.speed)
        
        self.ani_happy = Animation(self.base_path+"happy/*png",speed=self.speed)
        
        self.ani_angry = Animation(self.base_path+"angry/*png",speed=self.speed)
        
        self.current_ani = self.ani_general
        
    #Muda a animação
    def change_ani(self,ani):
        
        new_ani= getattr(self,ani)
        self.current_ani = new_ani
        self.current_ani.frame = self.current_ani.ani_list[0]
        
    #Mostra o frame na tela
    def rep_visual(self,screen,escala,pos):
        
        self.current_ani.update_frame()
        self.current_ani.rep_visual(screen,escala,pos)
        
        
    
    