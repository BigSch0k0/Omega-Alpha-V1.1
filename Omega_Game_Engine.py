import pygame
from Screen import *
from Runtime import *

def main():
    
    pygame.init()
    print("Welcome to Omega!")

    engineMode = "ENGINE" #engine or release | to do: search in file
    
    screen = createScreen("Omega Game Engine", 1800, 900, False)
    runtime(screen, "ENGINE")


if __name__ == "__main__":
    main()