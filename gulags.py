import pygame 


pygame.init()

S_WIDHT = 500
S_HEIGHT = 500

win = pygame.display.set_mode((S_WIDHT,S_HEIGHT))

pygame.display.set_caption("Gulag Simulator")

#Classe básica para um campo
class Campo():
    
    #Valores do campo
    def __init__(self,nome,r_detec,recursos,extracao,r_nevasca,clima):
        
        #Infor básica - imutável
        self.nome = nome
        self.r_detec = r_detec
        self.recursos = recursos
        self.extracao = extracao
        self.r_nevasca = r_nevasca
        self.clima = clima
        
        #Valores a serem alterados com upgrades
        self.aquecedor = 0
        self.seguranca = 0
        self.medica = 0
        self.lazer = 0
             
        #Status do campo
        self.felicidade = 50
        self.prod_mensal = 0
        self.medo = 0   #Alterado por eventos especiais
    
    #Print dos dados de cada campo  
    def __repr__(self):
        return f"""\nNome: '{self.nome}', R. deteção: '{self.r_detec}', Recursos: '{self.recursos}'
                   Extração: '{self.extracao}', R. Nevasca: '{self.r_nevasca}', Clima: '{self.clima}'
                   Aquecedor: '{self.aquecedor}', Segurança: '{self.seguranca}', Medica: '{self.medica}', Lazer: '{self.lazer}'
                   Felicidade: '{self.felicidade}', Prod_Mensal: '{self.prod_mensal}', Medo: '{self.medo}'\n"""
        

def setup_inicial():

    lista_gulags = []

    #Criação dos dados dos gulags
    Trofimovsk = Campo("Trofimovsk",0,6,"Madeira",4,"Congelante")
    Solovetsky = Campo("Solovetsky",35,8,"Madeira",0,"Frio")
    Norilsk = Campo("Norilsk",15,3,"Mineração de Ferro / Trabalho em Siderúrgica",3,"Muito Frio")
    Sevvostlag = Campo("Sevvostlag",30,10,"Ouro e estanho",1,"Frio")
    Pechorlag = Campo("Pechorlag",25,6,"Não",2,"Frio")
    Karlag  = Campo("Karlag ",20,0,"Não",1,"Frio")
    ALTAYSKIY  = Campo("ALTAYSKIY",10,0,"Não",0,"Frio")
    
    lista_gulags.extend([Trofimovsk, Solovetsky, Norilsk, Sevvostlag, Pechorlag, Karlag, ALTAYSKIY ])
    
    return lista_gulags

if __name__ == "__main__":
    
    lista_gulags = setup_inicial()
    
    for campo in lista_gulags:
        print (campo)
        
        
    