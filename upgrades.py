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
            
    def __repr__(self):
        return f"""\nNome: '{self.name}', Divisão: '{self.div}', 
                Descrição: '{self.desc}'
                Preço: '{self.price}',
                Lista de efeitos: '{self.effects_list}'"""
        
##---------------------[Declaração dos upgrades em si] ---------------------##

upg_Analgesicos=Upgrade("Analgésicos","medico",
                        "Redução no tempo de recuperação de feridos",500,
                        (("vel_atend",3)),
                        (("-20% tempo de recuperação",1))
                        )    
upg_list = [upg_Analgesicos]
print (upg_list[0])