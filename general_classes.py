import pygame
import glob 

pygame.init()


#Módulo com as classes gerais utilizadas por todo o código

from general_functions import *

class Button():
    def __init__(self,color,x,y,width,height,text,text_rus,text_size=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_rus = text_rus

    #Desenha o botão na tela
    def draw(self,screen,rus,outline=None):
        
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if rus:
            draw_text(self.text_rus,preto,screen,center=rect.center)
        else:
            draw_text(self.text,preto,screen,center=rect.center)
            

    #Testa colisão 
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False