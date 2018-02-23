import pygame, sys
from pygame.locals import *
from math import *
from Topologie import *
import random 

size=25
listetopo= [Topologie(1,"Clear",(136,66,29,0.50)),
 Topologie(2,"Ridge",(91,60,17,0.50)),
 Topologie(3,"Canal",(20,147,20,0.50)),
 Topologie(4,"AccesSPUR",(22,184,78,0.50)),
 Topologie(5,"Vapor pool",(255,255,255,0.50)),
 Topologie(4,"Rise",(146,109,39,0.50)),
 Topologie(7,"Cliffside",(255,206,154,0.50)),
 Topologie(8,"Mesa-Top",(240,195,0,0.50)),
 Topologie(9,"Crater",(0,0,0,0.50))]
class Hex:

    def __init__(self,col,row):
        self.col = col
        self.row = row
        self.selected = None
        self.topologie = listetopo[random.randint(0,8)]

    def draw (self,Display): 
        height = size * 2
        width = sqrt(3)/2 * height
        if(self.selected!=None):
            color = self.selected
        else:
            color = self.topologie.couleur

        pygame.draw.polygon(Display,color,[ [self.x+(width/2), self.y+(height/4)]                                     
                                        ,[self.x+(width/2), self.y-(height/4)]
                                        ,[self.x, self.y-(height/2)]
                                        ,[self.x-(width/2), self.y-(height/4)]                                                    
                                        ,[self.x-(width/2), self.y+(height/4)]
                                        ,[self.x, self.y+(height/2)]                                    
                                        ],0)
