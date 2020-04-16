import pickle
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
from general_functions import *
import random
import time
import os
from save import *

Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",(10,10), foto="arnold.png")

save = Save(Trofimovsk,50,30)

outfile = open("saves/teste.pkl","wb")

pickle.dump(save,outfile)

outfile.close()

infile = open("saves/teste.pkl","rb")

z = pickle.load(infile)

print(z)
