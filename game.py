import pygame 


pygame.init()

S_WIDHT = 500
S_HEIGHT = 500

win = pygame.display.set_mode((S_WIDHT,S_HEIGHT))

pygame.display.set_caption("Gulag Simulator")

class 


#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,r_detec,recursos,r_nevasca,clima):
        
        #Infor básica - imutável
        self.nome = nome
        self.r_detec = r_detec
        self.recursos = recursos
        self.r_nevasca = r_nevasca
        self.clima = clima
        
        #Valores a serem alterados
        self.aquecedor = 0
        self.seguranca = 0
        self.medica = 0
        self.lazer = 0
        
        #Status do campo
        self.feliciade = 50
        self.prod_mensal = 0
        self.medo = 0   #Alterado por eventos especiais
        
        
        
    