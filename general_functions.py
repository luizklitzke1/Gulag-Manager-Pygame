import pygame

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

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)