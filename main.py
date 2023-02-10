#importing packages
import pygame as pg
import sys
import os
import shutil
from pygame.locals import *

#importing scripts
import scripts.scenes as scene
from scripts.textures import txt
#initialize pygame
pg.init()

#set the title & icon
pg.display.set_caption("Square Kings")
pg.display.set_icon(txt.icon)
#global variables
global screen
screen = pg.display.set_mode((800, 600), HWSURFACE|DOUBLEBUF|RESIZABLE)

#entry
if __name__ == "__main__":
    scene.MainMenu.main_menu(screen)