import pygame, sys
from pygame.locals import *
from math import *
from Topologie import *
from Hex import *
from Point import *
from Grid import *
from Scenario import *
from Unite import *
from Button import *

size = 25
hexagons = []
Scenario=Scenario(DISPLAY)
UniteLegionnaire= []
UnitCréer=True
NumeroUniteEnCours=None

def displayText():
    myfont = pygame.font.SysFont("monospace",20)
    DISPLAY.blit(myfont.render("Carte :",1,(255,0,0)),(80,20))
    DISPLAY.blit(myfont.render("Placer vos troupes :",1,(255,0,0)),(680,20))
    DISPLAY.blit(myfont.render("Etapes :",1,(255,0,0)),(680,130))
    DISPLAY.blit(myfont.render("Informations :",1,(255,0,0)),(680,400))
    myfont2 = pygame.font.SysFont("monospace",15)
    DISPLAY.blit(myfont2.render("ENTRER -> passer les étapes ",1,(255,0,0)),(680,420))
    DISPLAY.blit(myfont2.render("l'étape 'Imperial/Mineur Movement Phase' active les déplacements ",1,(255,0,0)),(700,440))
    DISPLAY.blit(myfont2.render("ESPACE -> affiche la portée de tir d'une unité sélectionnée",1,(255,0,0)),(680,460))
    DISPLAY.blit(myfont2.render("cliquer sur l'unité pour enlever l'affichage de la porté ",1,(255,0,0)),(700,480))
    DISPLAY.blit(myfont2.render("SUPPR -> réinitialise le jeu",1,(255,0,0)),(680,500))
    DISPLAY.blit(myfont2.render("CLIQUE UNITE -> déplacements possibles d'une unité sélectionnée",1,(255,0,0)),(680,520))
    DISPLAY.blit(myfont2.render("Cliquer sur une unité parmis la liste pour la placer sur la carte",1,(255,0,0)),(680,540))


def oddq_to_cube(hex):
    hex.dx = hex.col - (hex.row + (hex.row&1)) / 2
    hex.dz = hex.row
    hex.dy = -hex.dx-hex.dz

def position_to_cube(position):
    position.dx = position.col - (position.row + (position.row&1)) / 2
    position.dz = position.row
    position.dy = -position.dx-position.dz

def cube_to_axial(hex):
    hex.q = hex.dx
    hex.r = hex.dz

def evenr_offset_to_pixel(hex):
    hex.x = size * sqrt(3) * (hex.col - 0.5 * (hex.row&1)) + 100
    hex.y = size * 3/2 * hex.row + 75

def pixel_to_hex(x, y):
    hex.q = x * 2/3 / size
    hex.r = (-x / 3 + sqrt(3)/3 * y) / size
    return (q, r)

def evenr_offset_neighbor(hex, direction):
    parity = hex.row & 1
    dir = evenr_directions[parity][direction]
    return Hex(hex.col + dir.col, hex.row + dir.row)

def setButtonSelected(x,y):
    flag=False
    for i in range(0,len(buttons)):
        buttonSelect = buttons[i]
        if (buttonSelect.ifSelected(x,y)):
            if buttonSelect.selected:
                buttonSelect.selected = False
            else:
                buttonSelect.selected = True
                for i in range(0,len(buttons)):
                    button = buttons[i]
                    if buttonSelect.id != button.id:
                        button.selected = False
                break
    for i in range(0,len(buttons)):
        button = buttons[i]
        button.draw(DISPLAY)
    
def buttonSelectedExist():
    buttonSelected = False
    for i in range(0,len(buttons)):
        button = buttons[i]
        if button.selected:
            buttonSelected = True
            break
    return buttonSelected

def getButtonSelected():
    for i in range(0,len(buttons)):
        button = buttons[i]
        if button.selected:
            return button
            break

def unitExist(x,y):
    uniteExist = True
    for i in range(0,len(UniteLegionnaire)):
        unite = UniteLegionnaire[i]
        if unite.Unite.uniteExistInPosition(x,y):
            uniteExist = False
            break
    return uniteExist

def addUnit(id,hexagon):
    if id==1:
        UniteLegionnaire.append(Legionnaire_Trouper(len(UniteLegionnaire)))
        UniteLegionnaire[len(UniteLegionnaire)-1].Unite.SetPosition(hexagon)
    elif id==2:
        UniteLegionnaire.append(Legionnaire_ArmeLourde(len(UniteLegionnaire)))
        UniteLegionnaire[len(UniteLegionnaire)-1].Unite.SetPosition(hexagon)
    elif id==3:
        UniteLegionnaire.append(Legionnaire_Commander(len(UniteLegionnaire)))
        UniteLegionnaire[len(UniteLegionnaire)-1].Unite.SetPosition(hexagon)
    elif id==4:
        UniteLegionnaire.append(Colanial_Miner(len(UniteLegionnaire)))
        UniteLegionnaire[len(UniteLegionnaire)-1].Unite.SetPosition(hexagon)
    NumeroUniteEnCours=len(UniteLegionnaire)-1
    
def displayButtons():
    for i in range(0,len(buttons)):
        button = buttons[i]
        button.draw(DISPLAY)

def displayUnites():
    for i in range(0,len(UniteLegionnaire)) :              
        UniteLegionnaire[i].Unite.Draw(DISPLAY)

def reset():
    for i in range(0,len(hexagons)):
        hexagon = hexagons[i]
        hexagon.selected=None
    for i in range(0,len(buttons)):
        button = buttons[i]
        button.selected=False
    Scenario.Tours=0
    Scenario.EtapeScenario=10

def displayRangeFire():
    position_to_cube(UniteLegionnaire[NumeroUniteEnCours].Unite.position)
    x=UniteLegionnaire[NumeroUniteEnCours].Unite.position.dx
    y=UniteLegionnaire[NumeroUniteEnCours].Unite.position.dy
    z=UniteLegionnaire[NumeroUniteEnCours].Unite.position.dz
    N=UniteLegionnaire[NumeroUniteEnCours].Unite.portee
    print("coordonnée de l'unité= "+str(x)+","+str(y)+","+str(z) )
    for dx in range(int(x-N),int(x+N)+1):
        for dy in range(int(y+(-N)),int(y+N)+1):
            for dz in range(int(z+(-N)),int(z+N)+1):
                if dx + dy + dz==0:
                    grid.setHexRange(dx,dy,dz) 

evenr_directions = [
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1,  0), Hex( 0, +1), Hex(+1, +1) ],
   [ Hex(+1,  0), Hex( 0, -1), Hex(-1, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ]
]

buttons = [Button(1,"Legionnaire_Trouper",(102, 0, 153),700,75),Button(2,"Legionnaire_ArmeLourde",(201, 160, 220),740,75),Button(3,"Legionnaire_Commander",(136, 77, 167),780,75),Button(4,"Colanial_Miner",(255, 0, 255),820,75)]

for col in range(0,12):
    for row in range(0,14):
        hex = Hex(col,row)
        oddq_to_cube(hex)
        cube_to_axial(hex)
        evenr_offset_to_pixel(hex)
        hexagons.append(hex)

grid = Grid(hexagons)
grid.display()
displayButtons()
displayText()

while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                print(" CLICK ")
                print(Mouse_x)
                print(Mouse_y)
                setButtonSelected(Mouse_x,Mouse_y)
                buttonSelected = buttonSelectedExist()
                button = getButtonSelected()
                hexagonSelect = grid.hexagonSelected(Mouse_x,Mouse_y)
                if buttonSelected and hexagonSelect:
                    if unitExist(Mouse_x,Mouse_y):
                        hexagon = grid.getSelectedHexagon(Mouse_x,Mouse_y)
                        addUnit(button.id,hexagon)
                else:
                    hexagonSelect = grid.hexagonSelected(Mouse_x,Mouse_y)
                    if hexagonSelect:
                        grid.setSelectedHexagon(Mouse_x,Mouse_y)
                        hexagon = grid.getSelectedHexagon(Mouse_x,Mouse_y)
                        for Nunite in range(0,len(UniteLegionnaire)):
                            if UniteLegionnaire[Nunite].Unite.CompareCoordonneXY(hexagon):
                                NumeroUniteEnCours=Nunite
                        print(" Unite en cours: "+str(NumeroUniteEnCours))
                        if NumeroUniteEnCours!=None:
                            listHexProche = []
                            if Scenario.EtapeScenario<10 and ListeEtape[Scenario.EtapeScenario].Ordre==6:
                                for direction in range(0,6):
                                    hexagonProche = evenr_offset_neighbor(hexagon,direction)
                                    if hexagonProche.col==UniteLegionnaire[NumeroUniteEnCours].Unite.position.col and hexagonProche.row==UniteLegionnaire[NumeroUniteEnCours].Unite.position.row and UniteLegionnaire[NumeroUniteEnCours].Unite.mobiliteRestante>0 :
                                        UniteLegionnaire[NumeroUniteEnCours].Unite.SetPosition(hexagon)
                                        UniteLegionnaire[NumeroUniteEnCours].Unite.mobiliteRestante-=1
                            if UnitCréer==False or (hexagon.col==UniteLegionnaire[NumeroUniteEnCours].Unite.position.col and hexagon.row==UniteLegionnaire[NumeroUniteEnCours].Unite.position.row) and UniteLegionnaire[NumeroUniteEnCours].Unite.mobiliteRestante>0:
                                for direction in range(0,6):
                                    hexagonProche = evenr_offset_neighbor(hexagon,direction)
                                    listHexProche.append(hexagonProche)
                                    oddq_to_cube(hexagonProche)
                                    cube_to_axial(hexagonProche)
                                    evenr_offset_to_pixel(hexagonProche)
                                    grid.setHexAround(hexagonProche)

                            if Scenario.EtapeScenario<10 and ListeEtape[Scenario.EtapeScenario].Ordre==2:
                               displayRangeFire()        
                        grid.display()
                        Scenario.Draw()
                        displayButtons()
                        displayUnites()
                        displayText()
                displayUnites()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    grid.display()
                    Scenario.EtapeSuivante()      
                    displayButtons()
                    displayUnites()
                    displayText()
                elif event.key==pygame.K_DELETE:
                    print("DEL")
                    UniteLegionnaire.clear()
                    reset()
                    grid.display()
                    displayButtons()
                    displayUnites()
                    displayText()
                elif event.key==pygame.K_SPACE:
                    if NumeroUniteEnCours!=None:
                       displayRangeFire()
                    grid.display()
                    Scenario.Draw()
                    displayButtons()
                    displayUnites()
                    displayText()          
            elif event.type == pygame.MOUSEBUTTONUP:
                print(" CLICK UP")
            elif event.type == pygame.KEYUP:
                print(" CLICK UP")
                    
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
