#Classe geral - abstrata - para base dos upgrades
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
        
        
    def apply_effec(self,est,effect):
        
    
        
##---------------------[Declaração dos upgrades em si] ---------------------##

def upg_Analgesicos(Upgrade):
    
    def __init__(self):
        
        super().__init__("Analgésicos",medico,
                         "Redução no tempo de recuperação de feridos",500,
                         
                         (("-20% tempo de recuperação",1)))
        

upg_list =