from Hex import *

class Unite:
    def __init__(self, id,portee,attaque,defense,mobilite,position,color):
        self.id = id
        self.portee = portee 
        self.attaque = attaque
        self.defense = defense
        self.mobilite = mobilite
        self.mobiliteRestante=mobilite
        self.etatDisruption=False
        self.position=position
        self.color=color

    def Draw(self,Display):
       # self.position.col=Hex.col
       # self.position.row=Hex.row
        rayon=int(size/2)
        pygame.draw.circle(Display,self.color,
        (int(self.position.x), int(self.position.y))
        ,rayon)                       

    def SetPosition(self,Hex):
        self.position.x=Hex.x
        self.position.y=Hex.y    
        self.position.col=Hex.col
        self.position.row=Hex.row        

    def uniteExistInPosition(self,x,y):
        flag = False
        if sqrt((x-self.position.x)*(x-self.position.x)+(self.position.y-y)*(self.position.y-y)) < 30:
            flag=True
        return flag      

    def Deplacer(hex):  
        print("DEPLACER")

    def Attaquer(Unite):
        print("ATTAQUER")

    def CompareCoordonneXY(self,Hex):
        if self.position.x==Hex.x and self.position.y==Hex.y:
            return True
        else:
            return False    
    def CompareCoordonneCR(self,Hex):
        if self.position.col==Hex.col and self.position.row==Hex.row :
            return True
        else:
            return False  

class position:
    def __init__(self,col,row):
        self.col=col
        self.row=row
        self.x=0
        self.y=0

class Legionnaire_Trouper:
    def __init__(self,id):
        self.Unite=Unite(id,6,6,3,6,position(0,0),(102, 0, 153))
        self.DisruptingFire=True       
        self.DejaUtiliserDisruptingFire=False
        self.Attaquer=False

class Legionnaire_ArmeLourde:
    def __init__(self,id):
        self.Unite=Unite(id,10,10,2,4,position(0,0),(201, 160, 220))
        self.DisruptingFire=True       
        self.DejaUtiliserDisruptingFire=False
        self.Attaquer=False

class Legionnaire_Commander:
    def __init__(self,id):
        self.Unite=Unite(id,4,4,3,6,position(0,0),(136, 77, 167))
        self.DisruptingFire=True       
        self.DejaUtiliserDisruptingFire=False
        #self.OpticSights=[OpticSight(position),OpticSight(position)]
        self.Attaquer=False

class Colanial_Miner:
    def __init__(self,id):
        self.Unite=Unite(id,3,2,1,2,position(0,0),(255, 0, 255))
        self.Attaquer=False

class Irdan_Rebels:
    def __init__(self,id):
        self.Unite=Unite(id,0,3,4,3,position(0,0))
        self.Attaquer=False

class Irdan_Rebels_Leader:
    def __init__(self,id):
        self.Unite=Unite(id,0,0,1,3,position(0,0))
        self.Attaquer=False

class Irdan_Rebels_Shooter:
    def __init__(self,id):
        self.Unite=Unite(id,3,4,2,3,position(0,0))
        self.Attaquer=False

class OpticSight:
    def __init(self,position):
        self.position=position

class EnergyStorm:
    def __init__(self,position,rayon):
        self.position=position
        self.rayon=rayon

