import pygame
import glob 

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

#Função pra pre-carregar os frames das animações
def load_frames(path):
    frames = []
    lista = glob.glob(path)
    lista.sort()
    for frame in lista:
        novo_frame = pygame.image.load(frame)
        frames.append(novo_frame)
    
    return frames

#Facilitar cálculo de largura relativa a tela
def swi(sw,per,dif=0):
    return int(sw*per)+dif

#Facilitar cálculo de altura relativa a tela  
def shi(sh,per,dif=0):
    return int(sh*per)+dif

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
def draw_img(screen,nome,escala,pos):
    img = pygame.image.load('imgs/'+nome)
    img = pygame.transform.scale(img, escala)
    screen.blit(img, pos)
    
    return img
    #return img.get_rect(x = escala[0], y= escala[1])
    
#Método para desenhar retângulos com texto na tela - Usado nos botões
def draw_botao(screen,cor,larg,alt,x,y,texto,cor_texto=branco):
    novo_rect = pygame.Rect(x, y, larg, alt)
    pygame.draw.rect(screen, cor, novo_rect)
    draw_text(texto, cor_texto, screen, center =novo_rect.center)
    
    return novo_rect

#Método para desenhar uma seção preta com um contorno branco
def draw_section(screen,x,y,larg,alt,esp,cor1=preto,cor2=branco):
    contorno = pygame.Rect(x-esp, y-esp, larg+esp*2, alt+esp*2)
    pygame.draw.rect(screen, cor2, contorno)
    preenchimento = pygame.Rect(x, y, larg, alt)
    pygame.draw.rect(screen, cor1, preenchimento)
    


