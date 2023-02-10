#importing packages
import pygame as pg
import sys
import os
import shutil
from pygame.locals import *

#import scripts
import scripts.button as button
from scripts.textures import txt

def mstart():
    pg.mouse.set_visible(False)
def mend(fscreen, mt, mx, my):
    fscreen.blit(mt, (mx, my))
class u:
    ores = (0, 0)
    fullscreen = False
    uscreen = None

#Main menu screenss
class MainMenu:
    def main_menu(screen):
        fscreen = screen.copy()
        while True:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.VIDEORESIZE:
                    u.ores = event.size
                    screen = pg.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

            fscreen.blit(pg.transform.scale(txt.bg, (800, 600)), (0, 0)) #background
            fscreen.blit(pg.transform.scale(txt.buttons.play, (100, 50)), (50, 100)) #play button
            fscreen.blit(pg.transform.scale(txt.buttons.exit, (100, 50)), (50, 175)) #exit button

            if button.hover(50, 100, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(50, 100, 100, 50): #play button function
                    MainMenu.play(screen)
            if button.hover(50, 175, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(50, 175, 100, 50): #exit button
                    sys.exit(0)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
    def play(screen):
        fscreen = screen.copy()
        while True:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.VIDEORESIZE:
                    screen = pg.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

            fscreen.blit(pg.transform.scale(txt.bg, (800, 600)), (0, 0)) #background
            fscreen.blit(pg.transform.scale(txt.buttons.back, (100, 50)), (0, 0)) #back button

            if button.hover(0, 0, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 0, 100, 50): #back button function
                    MainMenu.main_menu(screen)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()