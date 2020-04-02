import pygame

#Módulo com as funções gerais utilizadas por todo o código
#Servem como resumos para outras coisas que acabariam ocupando muito espaço desnecessariamente

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)

#Método para impressão de texto na tela
def draw_text(text, color, surface,tamanho=30, font=None, x=None, y=None, center=None):
    font = pygame.font.Font(font, tamanho)
    textobj = font.render(str(text), 10, color)
    textrect = textobj.get_rect()
    
    #Defina caso seja informado centralização
    if center:
        textrect.center = center
    #Define caso sejam dados X e Y
    else:
        textrect.x = x
        textrect.y = y
        
    surface.blit(textobj, textrect)

#Método para desenhar imagens na tela
def desenhar_img(screen,nome,escala,pos):
    img = pygame.image.load('imgs/'+nome)
    img = pygame.transform.scale(img, escala)
    screen.blit(img, pos)
    
#Método para desenhar retângulos com texto na tela - Usado nos botões
def desenhar_botao(screen,cor,larg,alt,x,y,texto,cor_texto=branco):
    
    novo_rect = pygame.Rect(x, y, larg, alt)
    pygame.draw.rect(screen, cor, novo_rect)
    draw_text(texto, cor_texto, screen, center =novo_rect.center)
    
    return novo_rect

#Método para desenhar botões - v2
class button():
    def __init__(self, cor,x,y, width,height, text='',text_color=branco):
        self.color = cor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color

    #Desenha o retângulo na tela
    def draw(self,screen,outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen, self.color, rect)
        draw_text(self.text,branco,screen,center=rect.center)
            

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False 
    

