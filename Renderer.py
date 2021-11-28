from sys import int_info, intern
from time import perf_counter
import pygame
from Entity import drawEntity_all
from Entity import entities
from Scene  import *
from color import *
from Screenobject import *
#from Buttonfunc import *


engineElements:list = []
engineBorders:list = [400,200,1000,600]

gameElements:list = []


preRenderEntities:list = []

entityRender:list = [0, ""]

global currentHyrarchieCount

currentHyrarchieCount = 0

def initEngine() -> int:

    #engineField = [300,300,1000,600]

    createLabel(0,0,1800,200,"",grey, "type_Edges")
    createLabel(0,0,400,1000,"",grey, "type_Edges")
    createLabel(0,800,1800,200,"",grey, "type_Edges")
    createLabel(1400,0,400,1000,"",grey, "type_Edges")

    #createLabel(10,10,300,10,"OMEGA Game Engine", grey, "type_Title_OMEGA")


    engineElements.append([400,200,1000,600,white]) #Editorfield
    engineBorders = [1000,600]                      #Editorfield borders

    createButton(400,0,70,30, "File", darkgrey, "type_file", "f_File")
    createButton(530,0,70,30, "Project", darkgrey, "type_file", "f_Project")

    createButton(10,100,250,30,"Scene",darkgrey, "type_scene", "s_Scene")
    createButton(270,100,30,30, "New", darkgrey, "type_scene", "s_NewScene")

    createLabel(10,150,250,30,"Hyrarchie",darkgrey, "type_Hyrarchie")
    createButton(270,150,30,30, "+", darkgrey, "type_hyrarchie", "s_Hyrarchie_NewByStats")
    createButton(310,150,30,30, "*", darkgrey, "type_hyrarchie", "s_Hyrarchie_NewByDraw")


    return 0

def updateHyrarchie() -> None:

    global currentHyrarchieCount

    entity = entities[-1]
    createButton(80, 200 + currentHyrarchieCount * 40, 100, 30, entity[-1], entity[4], "type_Entity", entity[-1])
    currentHyrarchieCount += 1


def updateEntityInfo(entity) -> None: 

    engineEntityInfo.clear()
    createEntityInfoLabel(entity)

def preRender(screen) -> None:
    
    for entity in preRenderEntities:
        pygame.draw.rect(screen,green,(entity[0] - 5 + 400, entity[1] - 5 + 200, entity[2] + 10, entity[3] + 10))


def runDisplay():
    pass

def render_EngineDisplay(screen:pygame.display) -> None:

    screen.fill(grey)

    for box in engineElements:
        pygame.draw.rect(screen,white,(box[0],box[1],box[2],box[3]))

    preRender(screen)
    drawEntity_all(screen, engineBorders)
    drawScreenObject_all(screen)
    #drawEntity_all(screen, engineBorders)

    




def render_ReleaseDiplay() -> None:
    pass
