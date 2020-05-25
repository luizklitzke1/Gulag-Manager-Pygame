import pygame
from pygame.locals import *
from general_functions import *
from animations import Animation
from buttons import Button

class Character():
    
    def __init__(self,id,div,speed=20):
        
        self.id = id
        self.div = div
        self.speed = speed
        
        self.base_path = "imgs/characters/" + self.id + "/"
        
        self.ani_general = Animation(self.base_path+"general/*png",speed=self.speed)
        self.ani_happy = Animation(self.base_path+"happy/*png",speed=self.speed)
        self.ani_angry = Animation(self.base_path+"angry/*png",speed=self.speed)
        self.current_ani = self.ani_general
        
        if self.id == "medic":
            self.color = magenta
        elif self.id == "secur":
            self.color = vermelho
        elif self.id == "recur":
            self.color = verde
        elif self.id == "construct":
            self.color = azul
        
        self.btn_chs = Button(self.color,0,0,0,0,self.div,text_size=20)
        
    #Muda a animação
    def change_ani(self,ani):
        
        new_ani= getattr(self,"ani_"+ani)
        self.current_ani = new_ani
        self.current_ani.frame = self.current_ani.ani_list[0]
        
    #Mostra o frame na tela
    def rep_visual(self,screen,escala,pos):
        
        self.current_ani.update_frame()
        self.current_ani.rep_visual(screen,escala,pos)

#Bolhas de dialogo    
class Text_Bubble():
    
    def __init__(self,text,sound,delay=10):
        
        self.text = text
        self.text_render = ""
        self.text_sound = pygame.mixer.Sound("sounds/"+sound+".wav")
        
        self.delay = delay
        self.delay_init = delay
    
    #Atualiza o texto
    def update_text(self):
        
        if len(self.text_render) != len(self.text):
            self.delay -= 1
            
            if self.delay == 0:
                
                self.text_render += (self.text[len(self.text_render)])
                self.delay = self.delay_init

    #Mostra a bolha e o texto na tela
    def rep_visual(self,screen=0,w=0,h=0,text_size=0):
        self.update_text()
        print(self.text_render)
    
    
##------------------[Declaração dos personagens em si] ------------------##  
 
char_Construct = Character("construct","Countruções")
char_Medic = Character("medic","Médico")
char_Recur = Character("recur","Recursos")
char_Secur = Character("secur","Segurança")
 
lista_char = [char_Construct,char_Medic,char_Recur,char_Secur]
 