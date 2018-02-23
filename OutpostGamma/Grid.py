import pygame
import sys
from pygame.locals import *
from math import *
from Hex import *

size = 25
DISPLAY=pygame.display.set_mode((1300,650),0,32)
WHITE=(255,255,255)
DISPLAY.fill(WHITE)
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 10)
blue=(0,0,255)
red=(255,0,0)

class Grid:

    def __init__(self, hexagons):
        self.hexagons = hexagons

    def display(self):
        DISPLAY.fill(WHITE)
        for i in range(0,len(self.hexagons)):
            self.hexagons[i].draw(DISPLAY)

    def setSelectedHexagon(self,x,y):
        flag = True
       #hexagonSelected
        for i in range(0,len(self.hexagons)):
            hexagon =  self.hexagons[i]
            if sqrt((x-hexagon.x)*(x-hexagon.x)+(hexagon.y-y)*(hexagon.y-y)) < size and flag:
                hexagon.selected = blue
                #hexagonSelected = hexagon
                flag=False
            else:
                hexagon.selected = None

    def getSelectedHexagon(self,x,y):
        for i in range(0,len(self.hexagons)):
            hexagon =  self.hexagons[i]
            if sqrt((x-hexagon.x)*(x-hexagon.x)+(hexagon.y-y)*(hexagon.y-y)) < size:
                return hexagon

    def hexagonSelected(self,x,y):
        flag = False
        for i in range(0,len(self.hexagons)):
            hexagon =  self.hexagons[i]
            if sqrt((x-hexagon.x)*(x-hexagon.x)+(hexagon.y-y)*(hexagon.y-y)) < size:
                flag = True
                break
        return flag

    def setHexAround(self,hex):
        for i in range(0,len(self.hexagons)):
            hexagon =  self.hexagons[i]
            if hex.q==hexagon.q and hex.r==hexagon.r:
                hexagon.selected = red
    
    def setHexRange(self,x,y,z):
        for i in range(0,len(self.hexagons)):
            hexagon =  self.hexagons[i]
            self.oddq_to_cube(hexagon)
            if x==hexagon.dx and y==hexagon.dy and z==hexagon.dz:
                hexagon.selected = red
        
    def oddq_to_cube(self,hex):
        hex.dx = hex.col - (hex.row + (hex.row&1)) / 2
        hex.dz = hex.row
        hex.dy = -hex.dx-hex.dz





