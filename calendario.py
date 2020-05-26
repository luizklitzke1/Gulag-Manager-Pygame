from general_functions import *

class Calendario():
    
    def __init__(self,screen,sw,sh,ciclo=10,dia=1,mes=1,ano=1969):
        self.dia = 1
        self.dias = [
            "Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira",
            "Sábado","Domingo"
        ]
        self.dia_pos = 0
        self.mes = 1
        self.semana = 0
        self.meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                      "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.ano = ano
    
        self.ciclo= ciclo
        self.ciclo_pos = ciclo
        self.pause = False
        
        self.lista_x = [(swi(sw,.025)+swi(sw,.0265),shi(sh,.556)+shi(sw,.023))]
        self.reload_x(screen,sw,sh)
        
    #Define a velocidad de atualização:
    def set_vel(self,vel):
        if vel > 0:
            self.pause = False
            self.ciclo = 10//vel
        else:
            self.pause = True
            self.ciclo = 0
        
    #Atualização dos dados a cada frame
    def update(self,screen,sw,sh):
        
        if self.pause == False:
            self.ciclo_pos -= 1
            
            print(self.dia_pos == 0)
            
            if self.ciclo_pos == 0:
                if self.dia_pos == 6:
                    self.dia_pos = 0
                    self.semana += 1
                else:
                    self.dia_pos += 1  
                    
                if self.dia == 28:
                    self.mes += 1
                    self.dia = 1
                    self.semana = 0
                    self.lista_x = []
                else:
                    self.dia += 1
                
                if self.mes == 13:
                    self.ano += 1
                    self.mes = 1
                
                self.ciclo_pos = self.ciclo
                
                pygame.draw.rect(screen,preto,[swi(sw,.01),shi(sh,.47),swi(sw,.205),int(swi(sw,.2)*1.036)])
                screen.blit(self.img_calend,(swi(sw,.01),shi(sh,.47)))
                
                draw_text(self.meses[self.mes-1]+" - "+str(self.ano),preto,screen,x=swi(sw,.018),y=shi(sh,.495))
            
                draw_text("Dia - "+str(self.dia),branco,screen,x=swi(sw,.023),y=shi(sh,.73))
                    
                draw_text("Velocidade - "+str(self.ciclo)+"tpd",branco,screen,x=swi(sw,.023),y=shi(sh,.795))
                
                x_dia=swi(sw,.025) + swi(sw,.0265)*self.dia_pos
                y_dia = shi(sh,.556)  + shi(sw,.023)*self.semana 
                    
                draw_text("O",verde,screen,x=x_dia,y=y_dia,tamanho=swi(sw,.019))
                
                if len(self.lista_x)== 0 or (self.lista_x[-1] != (x_dia,y_dia)):
                    self.lista_x.append((x_dia,y_dia))

                for x in self.lista_x[0:-1]:
                    draw_text("X",vermelho,screen,x=x[0],y=x[1], tamanho=swi(sw,.019))

    
    #Recarrega a posição do X no calend - caso ocorra mudança de res
    def reload_x(self,screen,sw,sh):
        
        temp = []
        
        #Recarrega o calendário em si
        img_calend = pygame.image.load("imgs/calend2.png",).convert_alpha()
        self.img_calend = pygame.transform.scale(img_calend, (swi(sw,.205),int(swi(sw,.2)*1.036)))
        
        if len(self.lista_x) > 0:
            for x in self.lista_x:
                semana = self.lista_x.index(x)//7
                dia_pos = self.lista_x.index(x)-semana*7
                x_dia=swi(sw,.025) + swi(sw,.0265)*dia_pos
                y_dia = shi(sh,.556)  + shi(sw,.023)*semana 
                
                temp.append((x_dia,y_dia))
        
            self.lista_x = temp      
        
    #Print dos valores atuais            
    def __repr__(self):
        return f""" {self.dias[self.dia_pos]} - Dia: {self.dia}\
               {self.meses[self.mes-1]} - Mês:  {self.mes}  Ano: {self.ano} """
      
               
