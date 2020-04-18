class Calendario():
    
    def __init__(self,ciclo=5,dia=1,mes=1,ano=1969):
        self.dia = 1
        self.dias = [
            "Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira",
            "Sábado","Domingo"
        ]
        self.dia_pos = 0
        self.mes = 1
        self.meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                      "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.ano = ano
        
        self.ciclo= ciclo
        self.ciclo_pos = ciclo
        
    def update(self):
        self.ciclo_pos -= 1
        
        if self.ciclo_pos == 0:
                
            if self.dia == 30:
                self.mes += 1
                self.dia = 1
            else:
                self.dia += 1
            
            if self.dia_pos == 6:
                self.dia_pos = 0
            else:
                self.dia_pos += 1
                
            if self.mes == 13:
                self.ano += 1
                self.mes = 1
            
            self.ciclo_pos = self.ciclo
            
    def __repr__(self):
        return f""" {self.dias[self.dia_pos]} - Dia: {self.dia}\
               {self.meses[self.mes-1]} - Mês:  {self.mes}  Ano: {self.ano} """
               
               