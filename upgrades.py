#Classe geral - abstrata - para base dos upgrades
class Upgrade():
    
    def __init__(self,name,div,desc,price,effect,effect_txt):
        
        self.name = name
        self.div = div
        self.desc = desc
        self.price = price
        self.effec = effec
        
    def apply_effec(self,est,effect):
        
    
        
##---------------------[Declaração dos upgrades em si] ---------------------##

def upg_Analgesicos(Upgrade):
    
    def __init__(self):
        
        super().__init__("Analgésicos",medico,
                         "Redução no tempo de recuperação de feridos",500,
                         
                         (("-20% tempo de recuperação",1)))
        

upg_list =