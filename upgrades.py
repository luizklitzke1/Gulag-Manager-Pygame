#Classe geral - abstrata - para base dos upgrades
class Upgrade():
    
    def __init__(self,name,div,desc,price,effec):
        
        self.name = name
        self.div = div
        self.desc = desc
        self.price = price
        self.effec = effec
        
##---------------------[Declaração dos upgrades em si] ---------------------##

def upg_Analgesicos(Upgrade):
    
    def __init__(self):