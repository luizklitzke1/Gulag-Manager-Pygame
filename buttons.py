import pygame
import glob 

pygame.init()


#Módulo com as classes gerais utilizadas por todo o código

from general_functions import *

class Button():
    def __init__(self,color,x,y,width,height,text,text_rus,text_size=None,text_color=branco):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_rus = text_rus
        self.text_size = text_size
        self.hover = False

    #Desenha o botão na tela
    def draw(self,screen,rus=False,outline=None):
        
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if rus:
            draw_text(self.text_rus,preto,screen,center=rect.center,tamanho=self.text_size)
        else:
            draw_text(self.text,preto,screen,center=rect.center,tamanho=self.text_size)
            

    #Testa colisão 
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if self.hover == False:
                    btn2.play()
                    self.hover = True
                return True
        self.hover = False
        return False
    
#Setup separado dos botões utilizados na tela de seleção inicial
def setup_botoes_inicial(sh,sw):
    margem_x = swi(sw,.03)
    w_botao = swi(sw,.15)
    h_botao = shi(sh,.05)
    btn_Trofimovsk = Button(branco,margem_x,shi(sh,.2),w_botao,h_botao,"Trofimovsk","Трофимовск")
    btn_Solovetsky = Button(branco,margem_x,shi(sh,.3),w_botao,h_botao,"Solovetsky","Соловетскы")
    btn_Norilsk = Button(branco,margem_x,shi(sh,.4),w_botao,h_botao,"Norilsk","Норилск")
    btn_Sevvostlag = Button(branco,margem_x,shi(sh,.5),w_botao,h_botao,"Sevvostlag","Севвостлаг")
    btn_Pechorlag = Button(branco,margem_x,shi(sh,.6),w_botao,h_botao,"Pechorlag","Печорлаг")
    btn_Karlag = Button(branco,margem_x,shi(sh,.7),w_botao,h_botao,"Karlag","Карлаг")
    btn_Altayskiy = Button(branco,margem_x,shi(sh,.8),w_botao,h_botao,"Altayskiy","Алтаыскиы")
    
    return [btn_Trofimovsk,btn_Solovetsky,btn_Norilsk,btn_Sevvostlag,btn_Pechorlag,btn_Karlag,btn_Altayskiy]

def setup_botoes_game(sh,sw):

    #Setup separado dos botões utilizados na tela do jogo em si
    margem_x = swi(sw,.015)
    w_botao = swi(sw,.17)
    h_botao = shi(sh,.08)
    btn_Trofimovsk = Button(branco,margem_x,shi(sh,.15)-8,w_botao,h_botao,"Status","Статус")
    btn_Solovetsky = Button(branco,margem_x,shi(sh,.25)-8,w_botao,h_botao,"Recursos","Рецурсос")
    btn_Norilsk = Button(branco,margem_x,shi(sh,.35)-8,w_botao,h_botao,"Upgrades","Упградес")
    
    lista_btns = [btn_Trofimovsk,btn_Solovetsky,btn_Norilsk]
    
    return lista_btns