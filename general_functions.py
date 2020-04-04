import pygame

pygame.init()


#Módulo com as funções gerais utilizadas por todo o código
#Servem como resumos para outras coisas que acabariam ocupando muito espaço desnecessariamente

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)

#Sons dos botões
btn1 = pygame.mixer.Sound("sounds/btn1.wav")
btn2 = pygame.mixer.Sound("sounds/btn2.wav")

#Método para impressão de texto na tela
def draw_text(text, color, screen,tamanho=None, font=None, x=None, y=None, center=None):
    if not tamanho:
        tamanho =int(screen.get_width()*0.01)
    font = pygame.font.Font("fonts/cmd2.ttf", tamanho)
    textobj = font.render(str(text), 20, color)
    textrect = textobj.get_rect()
    
    #Defina caso seja informado centralização
    if center:
        textrect.center = center
    #Define caso sejam dados X e Y
    else:
        textrect.x = x
        textrect.y = y
        
    screen.blit(textobj, textrect)

#Método para desenhar imagens na tela
def desenhar_img(screen,nome,escala,pos):
    img = pygame.image.load('imgs/'+nome)
    img = pygame.transform.scale(img, escala)
    screen.blit(img, pos)
    
    return img
    #return img.get_rect(x = escala[0], y= escala[1])
    
#Método para desenhar retângulos com texto na tela - Usado nos botões
def desenhar_botao(screen,cor,larg,alt,x,y,texto,cor_texto=branco):
    
    novo_rect = pygame.Rect(x, y, larg, alt)
    pygame.draw.rect(screen, cor, novo_rect)
    draw_text(texto, cor_texto, screen, center =novo_rect.center)
    
    return novo_rect


