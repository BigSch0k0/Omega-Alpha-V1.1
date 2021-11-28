

currentScene:str = "0000x0"
currentObjects:list = []

def scene_getCurrentObjects() -> list:
    pass

def scene_load(id:str) -> None:
    #-> File
    pass

def scene_close() -> bool:
    
    currentScene = "0000x0"
    currentObjects.clear()

def overrideScene(sceneID:str,entities:list) -> None:

    currentScene = sceneID
    currentObjects = entities