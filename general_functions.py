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
    font = pygame.font.Font("fonts/win_cmd.ttf", tamanho)
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
    
    return img
    #return img.get_rect(x = escala[0], y= escala[1])
    
#Método para desenhar retângulos com texto na tela - Usado nos botões
def desenhar_botao(screen,cor,larg,alt,x,y,texto,cor_texto=branco):
    
    novo_rect = pygame.Rect(x, y, larg, alt)
    pygame.draw.rect(screen, cor, novo_rect)
    draw_text(texto, cor_texto, screen, center =novo_rect.center)
    
    return novo_rect


