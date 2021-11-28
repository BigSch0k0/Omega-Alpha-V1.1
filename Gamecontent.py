

gameContent:list = []

def updateContent(object:list, append=True):
    pass

def initGameContent(fileContent:list) -> int:

    try:
        for content in fileContent:
            gameContent.append(content)

        return 1

    except Exception:

        return 1

def getContent(type:str, contentID:str):
    pass