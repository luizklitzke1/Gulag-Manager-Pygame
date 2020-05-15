#Série de testes para setar e pegar dados baseados em uma str de ref
#Luiz 12/05/202

class Cobaia():
    
    def __init__(self):
        self.a = "a"
        self.b = B()
        self.cobaia2 = Cobaia2()

class Cobaia2():
    
    def __init__(self):
        self.a = "aaaaaaaaa"  
      
class B():
    
    def __init__(self):
        self.c = "C"

class Teste():
    
    def __init__(self):
        self.a = "A"
        self.effects = [ 
            ["a","bbbbbbbbbbbbb"]
        ]
        self.divisao = "cobaia2"
        
    def apply_effect(self,cobaia):
        
        for effect in self.effects:
            
            est = getattr(cobaia,self.divisao)
            new = getattr(est,effect[0]) + effect[1]
            setattr(est,effect[0],new)


cobaia = Cobaia()
teste = Teste()
print(cobaia.cobaia2.a)
teste.apply_effect(cobaia)
print(cobaia.cobaia2.a)
        