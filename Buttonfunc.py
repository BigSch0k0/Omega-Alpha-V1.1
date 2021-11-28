from Renderer import updateEntityInfo
from Screenobject import *
from TKInter import *
import time
from Editorhandle import *


selectedProperty = []

def buttonFunction():

    ID:int = -1

    buttonID:str = collide()
    #print(buttonID)
    if buttonID == "s_Hyrarchie_NewByStats":
        createWindow("ENTITY")

    elif buttonID == "New":
        pass

    else:
       for entity in engineButtons:
           if entity[-2] == "type_Entity":
                if entity[ID] == buttonID:
                    engineEntityInfo.clear()
                
                    for current in engineButtons:   
                        if current[5] == red:
                            current[5] = darkgrey
                            updateSelected([], False)
                            preRenderEntities.clear()
                            engineEntityInfo.clear()
                    if entity[ID] not in selectedProperty:
                        selectedProperty.clear()
                        selectedProperty.append(entity[ID])

                        entity[5] = red
                        for e in entities:
                            if e[5] == entity[ID]:
                                preRenderEntities.append(e)
                                updateEntityInfo(e)
                    else:
                        selectedProperty.clear()
                    time.sleep(0.12)

def getSelected() -> list:

    return selectedProperty

                

