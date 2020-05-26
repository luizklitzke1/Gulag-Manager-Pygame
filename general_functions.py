#Módulo com as funções gerais utilizadas por todo o código
#Servem como resumos para outras coisas que acabariam ocupando muito espaço desnecessariamente

from itertools import chain
import pygame
import glob 

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.init()

#Cores padrão
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)
amarelo = (255,255,0)
magenta = (255,0,255)

#Sons dos botões
btn1 = pygame.mixer.Sound("sounds/btn1.wav")
btn2 = pygame.mixer.Sound("sounds/btn2.wav")
btn3 = pygame.mixer.Sound("sounds/btn3.wav")

#Split do texto em mais linhas

def show_fps(screen,mainClock):
    
    fps = str(mainClock.get_fps())
    
    pygame.draw.rect(screen,preto,[30,screen.get_height()*.945,500,30])
    draw_text("FPS: "+fps,vermelho,screen,x=10,y=screen.get_height()*.95)

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)


#Gerar os gráficos de progresso verticais
def draw_graf_vert(screen,val_min,val_max,mid,val,maxh,width,x,y,tipo,text):
    altura = -(val*(maxh/val_max))
    visual= pygame.Rect(x, y, width, altura)
            
    if val < mid:
        if tipo == "cres":
            pygame.draw.rect(screen, vermelho, visual)
        else:
            pygame.draw.rect(screen, verde, visual)
    if val >= mid:
        if tipo == "cres":
            pygame.draw.rect(screen, verde, visual)
        else:
            pygame.draw.rect(screen, vermelho, visual)
            
    draw_text(val, branco, screen, center=(visual.centerx, visual.bottom-20))   
    draw_text(text, branco, screen, x=visual.x, y=visual.y+20)
    draw_text(str(val)+"-"+str(val_max), branco, screen, x=visual.x, y=visual.y+40)
        
#Função pra pre-carregar os frames das animações
def load_frames(path):
    frames = []
    lista = glob.glob(path)
    lista.sort()
    for frame in lista:
        novo_frame = pygame.image.load(frame).convert_alpha()
        frames.append(novo_frame)
    return frames

#Facilitar cálculo de largura relativa a tela
def swi(sw,per,dif=0):
    return int(sw*per)+dif

#Facilitar cálculo de altura relativa a tela  
def shi(sh,per,dif=0):
    return int(sh*per)+dif

#Método para impressão de texto na tela
def draw_text(text, color, screen,tamanho=None,font=None, x=None, y=None, center=None):
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
def draw_img(screen,path,dimensoes,pos):
    img = pygame.image.load('imgs/'+path)
    img = pygame.transform.scale(img, dimensoes)
    img.convert_alpha()
    screen.blit(img, pos)
    return img
    
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
    


