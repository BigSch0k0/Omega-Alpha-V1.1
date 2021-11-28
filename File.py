import pathlib


def file_checkExisting() -> list:   #returns a list of file names

    content:list = list(pathlib.Path('./').glob('*.txt'))   #[WindowsPath('xxx.txt')]

    return content


def file_load(name:str, path:str = "") -> list:
    
    try:
        content:list = []
        file = open(name,"r")
        content.append(file.read())

        return content

    except ValueError:
        print("Failed to load File")
        return []
        

def file_save(name:str, content:list, path:str = "") -> bool:
    
    try:
        file = open(name,"w")
        file.write(content)

        return True

    except Exception:
        print("Failed to save File")
        return False



def file_mutate() -> bool:
    pass
