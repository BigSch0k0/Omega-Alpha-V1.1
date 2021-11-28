import pygame


def createScreen(title:str, width:int, height:int, fullscreen:bool) -> pygame.display:

    screen:pygame.display = pygame.display.set_mode([width,height])

    return screen