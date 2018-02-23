import pygame, sys
from pygame.locals import *
from Etape import *
ListeEtape = [Etape(1,"Energy Storm Phase"),
 Etape(2,"Disrupting Fire Phase"),
 Etape(3,"Irdan Movement Phase"),
 Etape(4,"Irdan Combat Phase"),
 Etape(5,"Irdan Stun recovery Phase"),
 Etape(6,"Imperial/Mineur Movement Phase"),
 Etape(7,"Imperial/Mineur Combat Phase"),
 Etape(8,"Remove Disruption Markers"),
 Etape(9,"ImperialLegionnaire Stun Recovery Phase")]


class Scenario:
    def __init__(self,Display):
        self.Tours=0
        self.EtapeScenario=10
        self.Display=Display
    
    def Draw(self):
        if self.EtapeScenario>8:
            self.Tours+=1
            self.EtapeScenario=0
            #time.ssleep(10)
        if self.Tours>0:
            if self.EtapeScenario>=0: 
                myfont = pygame.font.SysFont("monospace",15)
                label = myfont.render("Tour "+str(self.Tours),1,(255,0,0))
                self.Display.blit(label,(700,200))
                myfont = pygame.font.SysFont("monospace",15)
                label = myfont.render(ListeEtape[self.EtapeScenario].Nom,1,(255,0,0))
                self.Display.blit(label,(700,250))
            #time.sleep(10)

    def EtapeSuivante(self):
        self.EtapeScenario+=1
        if self.Tours<13:             
            self.Draw()
        else:
            myfont = pygame.font.SysFont("monospace",150)
            label = myfont.render("FIN DU JEUX",1,(255,0,0))
            self.Display.blit(label,(300,300))