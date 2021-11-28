import pygame
from color import *

engineButtons = []
engineLabels = []

engineEntityInfo = []

pygame.init()
font = pygame.font.SysFont("arial", 16)
#font = pygame.font.Font(None, 72)

def createButton(xPos:int, yPos:int, width:int, height:int, title:str, color:tuple, bType:str, bID:str) -> list:

    button = [xPos, yPos, width, height, title, color, pygame.Rect((xPos,yPos,width,height)),bType,  bID]
    engineButtons.append(button)

    return button


def createLabel(xPos:int, yPos:int, width:int, height:int, title:str, color:tuple, lID:str) -> list:

    label = [xPos, yPos, width, height, title, color, pygame.Rect((xPos,yPos,width,height))]
    engineLabels.append(label)

    return label


def createEntityInfoLabel(entity):

    engineEntityInfo.append([1440, 200, 250, 400, "", darkgrey, pygame.Rect(1440, 200, 250, 400)]) #Box
    engineEntityInfo.append([1440, 220, 100, 30, "Entity Info", darkgrey, pygame.Rect(1440, 220, 100, 30)]) #TopLabel
    engineEntityInfo.append([1450,300,100,30, "Xpos :" + str(entity[0]), darkgrey, pygame.Rect((280,300,100,30))]) #Xpos
    engineEntityInfo.append([1450,350,100,30, "Ypos :" + str(entity[1]), darkgrey, pygame.Rect((280,350,100,30))]) #Ypos
    engineEntityInfo.append([1450,400,100,30, "Width :" + str(entity[2]), darkgrey, pygame.Rect((280,400,100,30))]) #Wpos
    engineEntityInfo.append([1450,450,100,30, "Height :" + str(entity[3]), darkgrey, pygame.Rect((280,450,100,30))]) #Hpos



def drawButton(screen:pygame.display, button:list) -> None:

    x,y,w,h,title,col,rec = 0,1,2,3,4,5,6

    pygame.draw.rect(screen,button[col],(button[x],button[y],button[w],button[h]))
    text = font.render(button[title],True,white)
    textrect = text.get_rect(center=(button[x] + button[w]/2, button[y] + button[h]/2))
    screen.blit(text,textrect)
    

def updatePos(title,x,y) -> int:

    for button in engineButtons:
        if button[4] == title:
            button[0] = x
            button[1] = y
            return 1

    return 0


def collide() -> str:

        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            for button in engineButtons:
                if button[6].collidepoint(pos):
                    print(button[-1])
                    return button[-1]

        return "000x0F"


def drawScreenObject_all(screen) -> None:

    for label in engineLabels:

        drawButton(screen, label)

    for button in engineButtons:

        drawButton(screen,button)

    for info in engineEntityInfo:

        drawButton(screen, info)

 