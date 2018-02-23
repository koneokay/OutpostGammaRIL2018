import pygame, sys
from pygame.locals import *
from math import *
import random 
from Topologie import *
from Hexagon import *
from Direction import *
from Point import *
from Grid import *
from Scenario import *
from Unite import *
import time
hexagones = []

listetopo= [Topologie(1,"Clear",(136,66,29,0.50)),
 Topologie(2,"Ridge",(91,60,17,0.50)),
 Topologie(3,"Canal",(20,147,20,0.50)),
 Topologie(4,"AccesSPUR",(22,184,78,0.50)),
 Topologie(5,"Vapor pool",(255,255,255,0.50)),
 Topologie(4,"Rise",(146,109,39,0.50)),
 Topologie(7,"Cliffside",(255,206,154,0.50)),
 Topologie(8,"Mesa-Top",(240,195,0,0.50)),
 Topologie(9,"Crater",(0,0,0,0.50))]

Scenario=Scenario(DISPLAY)
UniteLegionnaire= [Legionnaire_Trouper(1)]
def evenr_offset_to_pixel(direction):
    x = size * sqrt(3) * (direction.q - 0.5 * (direction.r&1))
    y = size * 3/2 * direction.r
    return Point(x, y)

for q in range(0,12):
    for r in range(0,14):
        hexagones.append(Hexagone(evenr_offset_to_pixel(Direction(q,r)),listetopo[random.randint(0,8)]))

grid = Grid(hexagones)
grid.display()

while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                print(" CLICK ")
                print(Mouse_x)
                print(Mouse_y)
                grid.setSelectedHexagon(Mouse_x,Mouse_y)
                grid.display()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(" CLICK UP")
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_KP_ENTER:
                        Scenario.EtapeSuivante()
                        grid.display()
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def hex_to_pixel(direction):
    x = size * sqrt(3) * (direction.q + direction.r/2)
    y = size * 3/2 * direction.r
    return Point(x, y)

def pixel_to_hex(x, y):
    q = (x * sqrt(3)/3 - y / 3) / size
    r = y * 2/3 / size
    return hex_round(Direction(q, r))