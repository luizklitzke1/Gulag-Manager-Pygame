from general_functions import *

#Classe geral para os upgrades
class Upgrade():
    
    def __init__(self,name,div,desc,price,effects_list,effects_txt_list):
        
        self.name = name
        self.div = div
        self.desc = desc
        self.price = price
        #Uma lista dos efeitos -> [ [att1,mudanca1] , [att2,mudanca2] ]
        self.effects_list = effects_list
        #Lista dos textos dos efeitos  ->  [ [ef1,0 ou 1 (ruim ou bom)] ]
        self.effects_txt_list = effects_txt_list
        
    #Aplica o efeito do upgrade
    def apply_effec(self,est,effects_list):
        
        for effect in effects_list:
            new_value = getattr(est,effect[0]) + effect[1]
            setattr(est,effect[0],new)
    
    #Representação visual na tela de compra
    def rep_visual(self,screen,sw,sh,margem_x,margem_y):
        
        draw_img(screen,"outline.png",(swi(sw,.3),shi(sh,.3)),(margem_x,margem_y))
        
        if self.div == "medico":
            color = (255,0,255)
        elif self.div == "seguranca":
            color = (255,0,0)
        elif self.div == "recursos":
            color = (0,255,0)
            
        dif = swi(sw,.012)
            
        draw_text(self.name,color,screen,swi(sw,.013),
                  x=margem_x+dif,y=margem_y+dif)
        
        #Quebra a descrição em mais linhas
        text_split = split_text(self.desc,swi(sw,.009),swi(sw,.28))
        
        for linha in text_split:   
            margem_y_linha = (margem_y+dif*4)+swi(sw,.01)*text_split.index(linha)
            draw_text(linha,branco,screen,swi(sw,.009),
                      x=margem_x+dif,y=margem_y_linha)
        
    
    #Representação em string
    def __repr__(self):
        return f"""\nNome: '{self.name}', Divisão: '{self.div}', 
                Descrição: '{self.desc}'
                Preço: '{self.price}',
                Lista de efeitos: '{self.effects_list}'"""
        
        
##---------------------[Declaração dos upgrades em si] ---------------------##

upg_Analgesicos=Upgrade("Analgésicos","medico",
                        "Redução no tempo de recuperação de feridos.",500,
                        (("vel_atend",3)),
                        (("-20% tempo de recuperação",1),
                         ("+10% custo mensal",0))
                        )    
upg_MaisCamas=Upgrade("Mais camas","medico",
                        "Mais camas - leitos.",420,
                        (("leitos",3)),
                        (("+3 leitos",1),
                         ("- 2 vel. atendimento",0))
                      )    
upg_MelhoresMachados=Upgrade("Melhores Machados","recursos",
                        "Aumenta velocidade do corte de árvores.",150,
                        (("vel_extract",3)),
                        (("+2 vel. extração",1))
                        )    
upg_Metralhadoras=Upgrade("Metralhadoras","seguranca",
                        "Mais tiros, mais erros, porém mais chance de acertar!.",500,
                        (("arm",2)),
                        (("+1 armamento",1),
                         ("+300 custo mensal",0))
                        )    
upg_list = [upg_Analgesicos,upg_MaisCamas,upg_MelhoresMachados,upg_Metralhadoras]