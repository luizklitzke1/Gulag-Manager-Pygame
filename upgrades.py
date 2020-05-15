from general_functions import *
from buttons import Button

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
        #Botão para adquirir
        self.botao = Button(branco,0,0,0,0,"Comprar","")
        
    #Aplica o efeito do upgrade
    def apply_effec(self,gulag):
        
        est = getattr(gulag,self.div)
        for effect in self.effects_list:
            
            new_value = getattr(est,effect[0]) + effect[1]
            setattr(est,effect[0],new_value)
    
    #Representação visual na tela de compra
    def rep_visual(self,screen,sw,sh,margem_x,margem_y):
        
        draw_img(screen,"outline.png",(swi(sw,.32),shi(sh,.32)),(margem_x,margem_y))
        
        if self.div == "Est_Medic":
            color = (255,0,255)
        elif self.div == "Est_Segur":
            color = (255,0,0)
        elif self.div == "Est_Recur":
            color = (0,255,0)
            
        dif = swi(sw,.015)
            
        draw_text(self.name,color,screen,swi(sw,.013),
                  x=margem_x+dif,y=margem_y+dif)
        
        #Quebra a descrição em mais linhas
        font = pygame.font.Font("fonts/cmd2.ttf", swi(sw,.009))
        text_split = wrapline(self.desc,font,swi(sw,.28))
        
        for linha in text_split:   
            margem_y_linha = (margem_y+dif*4)+swi(sw,.01)*text_split.index(linha)
            draw_text(linha,branco,screen,swi(sw,.009),
                      x=margem_x+dif,y=margem_y_linha)
            
        #Beneficios e maleficios do upgrade
        bottom = margem_y + shi(sh,.28) - dif
        
        for effect in self.effects_txt_list:
            
            effects_txt_list = self.effects_txt_list[::-1]

            if effect[1] == 0:
                cor = vermelho
            else:
                cor = verde
            
            draw_text(effect[0],cor,screen,swi(sw,.009),
                      x=margem_x+dif,
                      y=bottom-effects_txt_list.index(effect)*swi(sw,.012)
                      )
            
        #Botão para adquirir
        self.botao.y = bottom
        self.botao.x = margem_x + swi(sw,.23)
        self.botao.width = swi(sw,.08)
        self.botao.height = shi(sh,.05)
        self.botao.draw(screen)
    
    #Representação em string
    def __repr__(self):
        return f"""\nNome: '{self.name}', Divisão: '{self.div}', 
                Descrição: '{self.desc}'
                Preço: '{self.price}',
                Lista de efeitos: '{self.effects_list}'"""
        
        
##---------------------[Declaração dos upgrades em si] ---------------------##

upg_Analgesicos=Upgrade("Analgésicos","Est_Medic",
                        "Redução no tempo de recuperação de feridos.",500,
                        (("vel_atend",3),),
                        (("-20% temp recuperação",1),
                         ("+10% custo mensal",0))
                        )    

upg_MaisCamas=Upgrade("Mais camas","Est_Medic",
                        "Mais camas para as falh... pessoas mais fracas no momento.",420,
                        (("leitos",3),),
                        (("+3 leitos",1),
                         ("- 2 vel. atendimento",0))
                      )     
upg_Metralhadoras=Upgrade("Metralhadoras","Est_Segur",
                        "Mais tiros, mais erros, porém mais chance de acertar!",500,
                        (("arm",2),),
                        (("+1 armamento",1),
                         ("+300 custo mensal",0))
                        )    
upg_MelhoresMachados=Upgrade("Melhores Machados","Est_Recur",
                        "Machados mais resistentes e afiados!",150,
                        (("vel_extract",3),),
                        (("+2 vel. extração",1),
                         ("-1 riscos",1))
                        )  
 
upg_list = [upg_Analgesicos,upg_MaisCamas,upg_Metralhadoras,upg_MelhoresMachados]