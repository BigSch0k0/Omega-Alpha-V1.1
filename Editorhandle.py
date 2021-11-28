import pygame
from color import*
from Entity import *
import time
from Renderer import *

global selected
selected:bool = False

global selectedEntity
selectedEntity:list = []

global selectedEntity_ID
selectedEntity_ID:list = []


def runEditor(screen):
    global selected
    global selectedEntity_ID
    #print(entities)

    if(len(entities)) > 0:
        pos = pygame.mouse.get_pos()
        if isInRange(pos, [400,200,1000,600], 0):
            if pygame.mouse.get_pressed()[0]:
                if not selected:
                    for button in engineButtons:
                        button[5] = darkgrey
                    preRenderEntities.clear()
                    try:
                        for entity in entities:
                            if isInRange(pos, entity, 0, True):
                                getID(entity)
                                for button in engineButtons:
                                    if button[-1] == entity[5]:
                                        button[5] = red
                                preRenderEntities.append(entity)
                                updateSelected(entity, True)

                        if(len(selectedEntity_ID)) > 0:
                            if isInRange(pos, entities[selectedEntity_ID[1]], 10, True):
                                updateEntityPos(pos)
                    
                    except AttributeError:
                        updateSelected([], False)
            
                if selected:
                    
                    updateEntityInfo(entities[selectedEntity_ID[1]])
                    setData(pos)
            else:
                updateSelected([], False)


def updateSelected(entity:list, mode:bool = True) -> None:
    global selected
    global selectedEntity
    global selectedEntity_ID

    selected = mode
    if mode:
        selectedEntity = entity
        #time.sleep(0.15) 
    else:
        selected = False 
        selectedEntity = []
        selectedEntity_ID.clear()
        #time.sleep(0.15) 


def isInRange(mouse:list, obj:list, incr:int, editorEntity:bool = False) -> bool:

    x,y = 0,0

    if editorEntity:
        x,y = 400,200

    if mouse[0] <= obj[0] + x + obj[2] + incr and mouse[0] >= obj[0] + x - incr:
        if mouse[1] <= obj[1] + y + obj[3] + incr and mouse[1] >= obj[1] + y - incr:
            #print("here2")
            return True
    return False 

def updateEntityPos(pos):
    entities[selectedEntity_ID[1]] [entityIndex["xPos"]]  = (pos[0] - 400 - entities[ selectedEntity_ID[1]] [entityIndex["width"]] / 2)
    entities[selectedEntity_ID[1]] [entityIndex["yPos"]]  = (pos[1] - 200 - entities[ selectedEntity_ID[1]] [entityIndex["height"]] / 2)

def setData(pos:list):
    global selectedEntity_ID
    if pygame.mouse.get_pressed()[0]:

        try:
            if isInRange(pos, entities[selectedEntity_ID[1]], 10, True):
                updateEntityPos(pos)
        
        except AttributeError:
                pass
    
        

def getID(entity:list) -> None:
    global selectedEntity_ID
    for i in range(len(entities)):
        if entities[i][-1] == entity[-1]: 
            selectedEntity_ID = [entities[i][-1], i]
        