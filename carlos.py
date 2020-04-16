import pickle
import pygame, sys
from pygame.locals import *
from gulags import Campo, setup_inicial
from general_functions import *
import random
import time
import os


Trofimovsk = Campo("Trofimovsk","Трофимовск",0,6,"Madeira",4,"Congelante",(10,10), foto="arnold.png")

outfile = open("saves/teste.pkl","wb")

pickle.dump(Trofimovsk,outfile)

outfile.close()

infile = open("saves/teste.pkl","rb")

z = pickle.load(infile)

print(z)

print(z.teste(2,1))