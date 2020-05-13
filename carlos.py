class Cobaia():
    
    def __init__(self):
        self.a = "a"
        self.b = B()
        
class B():
    
    def __init__(self):
        self.c = "C"

class Teste():
    
    def __init__(self):
        self.a = "A"
        self.effects = [ 
            ["a","a"]
        ]
        
    def apply_effect(self,cobaia):
        
        for effect in self.effects:
            new = getattr(cobaia,effect[0]) + effect[1]
            setattr(cobaia,effect[0],new)


cobaia = Cobaia()
print(cobaia.a)
teste = Teste()
teste.apply_effect(cobaia)
print(cobaia.a)
        