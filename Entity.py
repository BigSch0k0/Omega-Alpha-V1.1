from color import *
from Scene import *
import pygame


entities:list = []
editorBorders:list = [[0,0,1800,200], [0,0,400,1000], [0,800,1800,200], [1400,0,400,1000]]

entityIndex = {

            "xPos" : 0,
            "yPos" : 1,
            "width" : 2,
            "height" : 3,
            "color" : 4,
            "ID" : 5

}


def newEntity(xPos:int = 0, yPos:int = 0, width:int = 50, height:int = 50, col:str = "red", ident:str = "Entity" + str(len(entities))) -> None:
    entities.append([xPos, yPos, width, height, colors[col], ident])


def getEntities_current() -> list:

    return entities


def drawEntity_all(screen, borders:list = [0,0,1800,1000]) -> None:

    x,y,w,h = 0,1,2,3
    col = black

    for entity in entities:

        xPos = int(borders[x] + entity[x])
        yPos = int(borders[y] + entity[y])
        pygame.draw.rect(screen,col,(xPos,yPos,entity[w],entity[h]))

    for border in editorBorders:
        pygame.draw.rect(screen,col,(border[x],border[y],border[w],border[h]))

def editData(entity:list, x:int, y:int, w:int = 0, h:int = 0):
    
    entity[0], entity[1] = x, y
