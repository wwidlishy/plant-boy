#importing packages
import pygame as pg
import sys
import os
import shutil
from pygame.locals import *

#import scripts
import scripts.button as button
from scripts.textures import txt
import scripts.filemanager as fm

def display_text(text, font_size, font_color, position, screen):
    font = pg.font.Font(None, font_size)
    text = font.render(text, 1, font_color)
    screen.blit(text, position)

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
            pg.time.Clock().tick(60)
    def play(screen):
        cback = 0
        fscreen = screen.copy()
        running = True
        while running:
            if cback != 10: cback += 1
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
            fscreen.blit(pg.transform.scale(txt.buttons.new, (100, 50)), (0, 500)) #new button
            fscreen.blit(pg.transform.scale(txt.buttons.load, (100, 50)), (0, 550)) #load button


            if button.hover(0, 0, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 0, 100, 50) and cback == 10: #back button function
                    MainMenu.main_menu(screen)
            if button.hover(0, 500, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 500, 100, 50): #new button function
                    MainMenu.new(screen)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)
    def new(screen):
        fscreen = screen.copy()
        name = ""
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
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        if len(name) != 0:
                            name = name[:-1]
                    else:
                        if len(name) != 27:
                            name += event.unicode

            fscreen.blit(pg.transform.scale(txt.bg, (800, 600)), (0, 0)) #background
            fscreen.blit(pg.transform.scale(txt.buttons.back, (100, 50)), (0, 0)) #back button
            fscreen.blit(pg.transform.scale(txt.buttons.create, (100, 50)), (0, 550)) #create button

            pg.draw.rect(fscreen, (54,43,46), pg.Rect(100, 100, 600, 400))
            pg.draw.rect(fscreen, (255, 255, 255), pg.Rect(110, 145, 400, 45))
            display_text("Name", 40, (255, 255, 255), (100, 100), fscreen)
            display_text(f"{name}", 40, (0 ,0, 0), (110, 145), fscreen)
            if button.hover(0, 0, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 0, 100, 50): #back button function
                    MainMenu.play(screen)
            if button.hover(0, 550, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 550, 100, 50): #create button function
                    save = fm.new(name)
                    if save == 1:
                        #TODO Name error popup
                        Game.game(screen, fm.load(name))
                    else:
                        pass

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)
class Game:
    def game(screen, saveData):
        print(saveData)
        fscreen = screen.copy()
        running = True
        while running:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.VIDEORESIZE:
                    screen = pg.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

            fscreen.fill((0, 0, 0))

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)