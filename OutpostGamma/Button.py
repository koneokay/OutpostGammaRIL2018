from Hex import *

size = 30

red = (255,0,0)

class Button:
    def __init__(self,id,name,color,x,y):
        self.id = id
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.selected = False

    def draw(self,Display):
        
        if self.selected:
            color = red
        else:
            color = self.color
            
        rayon=int(size/2)
        pygame.draw.circle(Display,color,(int(self.x), int(self.y)),rayon)

    def ifSelected(self,x,y):
            if sqrt((x-self.x)*(x-self.x)+(self.y-y)*(self.y-y)) < 30:
                return True

