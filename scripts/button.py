#importing packages
import pygame as pg
import sys
import os
import shutil

#button class
def click(x, y, sx, sy):
    #screen.blit(image, (x, y))
    mx, my = pg.mouse.get_pos()
    if (mx in range(x, x+sx)) and (my in range(y, y+sy)):
        if pg.mouse.get_pressed()[0]:
            return True

def hover(x, y, sx, sy):
    #screen.blit(image, (x, y))
    mx, my = pg.mouse.get_pos()
    if (mx in range(x, x+sx)) and (my in range(y, y+sy)):
        return True