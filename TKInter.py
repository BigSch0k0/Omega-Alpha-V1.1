from tkinter import *
from Screenobject import createButton
from color import *
from Entity import *
from functools import partial
import time
from random import randint
from Renderer import updateHyrarchie


windowData = []

def initWindow():

    window  = Tk()
    window.title("New Entity")
    window.geometry("300x500")
    window.attributes("-topmost", True)

    window.config(bg = "darkgrey")

    windowData.append(window)

    labelX = Label(window, text = "X Position : ")
    entryX = Entry(window, text = "X Position : ")
    entryX.insert(END, '400')

    windowData.append(labelX)
    windowData.append(entryX)

    labelY = Label(window, text = "Y Position : ")
    entryY = Entry(window, text = "Y Position : ")
    entryY.insert(END, '400')

    windowData.append(labelY)
    windowData.append(entryY)

    labelW = Label(window, text = "Width : ")
    entryW = Entry(window, text = "Width : ")
    entryW.insert(END, str(50))

    windowData.append(labelW)
    windowData.append(entryW)

    labelH = Label(window, text = "Height : ")
    entryH = Entry(window, text = "Height : ")
    entryH.insert(END, str(50))

    windowData.append(labelH)
    windowData.append(entryH)

    labelIdent = Label(window, text = "Ident : ")
    entryIdent = Entry(window, text = "Ident : ")
    entryIdent.insert(END, "Entity" + str(len(entities)))

    windowData.append(labelIdent)
    windowData.append(entryIdent)


def createWindow(type:str) -> None:

    initWindow()
  
    if type == "ENTITY":

        windowData[1].place(x=20,y=50,w=70,h=30)        #labelX
        windowData[2].place(x=100,y=50,w=100,h=30)      #entryX

        windowData[3].place(x=20,y=100,w=70,h=30)       #labelY
        windowData[4].place(x=100,y=100,w=100,h=30)     #entryY

        windowData[5].place(x=20,y=150,w=70,h=30)       #labelW
        windowData[6].place(x=100,y=150,w=100,h=30)     #entryW

        windowData[7].place(x=20,y=200,w=70,h=30)       #labelH
        windowData[8].place(x=100,y=200,w=100,h=30)     #entryH

        windowData[9].place(x=20,y=250,w=70,h=30)       #labelPhy
        windowData[10].place(x=100,y=250,w=100,h=30)    #entryPhy

        buttonSave = Button(windowData[0], text = "Save Entity", command = saveEntity)
        buttonSave.place(x=100, y=350, w=100, h=50)

        windowData[0].mainloop()


def saveEntity() -> None:
    
    x = int(windowData[2].get())        #entryX
    y = int(windowData[4].get())        #entryY
    w = int(windowData[6].get())        #entryW
    h = int(windowData[8].get())        #entryH
    ident = str(windowData[10].get())     #entryPhy

    entities.append([x,y,w,h,darkgrey, ident])

    updateHyrarchie()

    #print(entities)
    windowData[0].destroy()
    windowData.clear()