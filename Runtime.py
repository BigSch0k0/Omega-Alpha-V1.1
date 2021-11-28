import pygame
from color import *
from Renderer import *
from Buttonfunc import *
from Editorhandle import *

gameComponents:list = []
clock = pygame.time.Clock()


def initData() -> None:
    pass


def runtime(screen:pygame.display, gameMode:str = "") -> int:

    if gameMode == "ENGINE":

        initEngine()
        running:bool = True

        while running:
            gameloop(screen)

    if gameMode == "RELEASE":
        pass
    return 0


#------------------------------------------------------------------------------------------------
#Entry Point
#------------------------------------------------------------------------------------------------

def gameloop(screen:pygame.display) -> None:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        buttonFunction()
        render_EngineDisplay(screen)
        runEditor(screen)
        clock.tick(144)
        pygame.display.update()

#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------