#importing packages
import pygame as pg
import sys
import os
import shutil
from pygame.locals import *
from win32api import GetSystemMetrics

#import scripts
import scripts.button as button
from scripts.textures import txt
import scripts.filemanager as fm
from scripts.player import Player
from scripts.platform import Platform
from scripts.collide import *
import scripts.settingsmanager as sman

def display_text(text, font_size, font_color, position, screen):
    font = pg.font.Font(None, font_size)
    text = font.render(text, 1, font_color)
    screen.blit(text, position)

def mstart():
    pg.mouse.set_visible(False)
def mend(fscreen, mt, mx, my):
    fscreen.blit(mt, (mx, my))

#Main menu screenss
class MainMenu:
    def main_menu(screen):
        fscreen = screen.copy()
        if sman.load()['fullscreen']:
            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
        else:
            screen = pg.display.set_mode((800, 600))
        while True:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_F11:
                        if not sman.load()['fullscreen']:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'True').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
                        else:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'False').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((800, 600))

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
        running = True
        fscreen = pg.surface.Surface((800, 600))
        if sman.load()['fullscreen']:
            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
        else:
            screen = pg.display.set_mode((800, 600))
        while running:
            if cback != 10: cback += 1
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_F11:
                        if not sman.load()['fullscreen']:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'True').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
                        else:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'False').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((800, 600))

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
            if button.hover(0, 550, 100, 50):
                mt = pg.transform.scale(txt.cours_2, (25, 25))
                if button.click(0, 550, 100, 50): #load button function
                    MainMenu.load(screen)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)
    def new(screen):
        fscreen = pg.surface.Surface((800, 600))
        name = ""
        if sman.load()['fullscreen']:
            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
        else:
            screen = pg.display.set_mode((800, 600))
        while True:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        if len(name) != 0:
                            name = name[:-1]
                    elif event.key == pg.K_RETURN:
                        save = fm.new(name)
                        if save == 1:
                            #TODO Name error popup
                            pass
                        else:
                            Game.game(screen, fm.load(name), name) 
                    elif event.key == pg.K_F11:
                        if not sman.load()['fullscreen']:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'True').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
                        else:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'False').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((800, 600)) 
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
                        pass
                    else:
                        Game.game(screen, fm.load(name), name)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)
    def load(screen):
        fscreen = pg.surface.Surface((800, 600))
        name = ""
        if sman.load()['fullscreen']:
            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
        else:
            screen = pg.display.set_mode((800, 600))
        while True:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        if len(name) != 0:
                            name = name[:-1]
                    elif event.key == pg.K_RETURN:
                        save = fm.load(name)
                        if save == 1:
                            #TODO Name error popup
                            pass
                        else:
                            Game.game(screen, fm.load(name), name)  
                    elif event.key == pg.K_F11:
                        if not sman.load()['fullscreen']:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'True').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
                        else:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'False').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((800, 600))
                    else:
                        if len(name) != 27:
                            name += event.unicode

            fscreen.blit(pg.transform.scale(txt.bg, (800, 600)), (0, 0)) #background
            fscreen.blit(pg.transform.scale(txt.buttons.back, (100, 50)), (0, 0)) #back button
            fscreen.blit(pg.transform.scale(txt.buttons.load, (100, 50)), (0, 550)) #load button

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
                if button.click(0, 550, 100, 50): #load button function
                    save = fm.load(name)
                    if save == 1:
                        #TODO Name error popup
                        pass
                    else:
                        Game.game(screen, fm.load(name), name)

            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)
class Game:
    def game(screen, saveData, name):
        load = saveData[0]
        tosave = saveData[1]
        sname = name.replace(' ', "_")
        fscreen = pg.surface.Surface((800, 600))
        running = True
        x, y = load['player_stats']['pos']
        player = Player(fscreen, (x, y))
        platform = Platform(fscreen, (100, 400), (500 ,50))
        if sman.load()['fullscreen']:
            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
        else:
            screen = pg.display.set_mode((800, 600))
        while running:
            mstart()
            mt = pg.transform.scale(txt.cours_1, (25, 25))
            mx, my = pg.mouse.get_pos()
            pg.mouse.set_visible(False)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_F11:
                        if not sman.load()['fullscreen']:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'True').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)), pg.FULLSCREEN)
                        else:
                            sman.write(sman.settingstosave.replace('__FULLSCREEN__', 'False').replace('__AUTOSAVE__', f"{sman.load()['autosave']}"))
                            screen = pg.display.set_mode((800, 600))

            fscreen.fill((100, 100, 100))
            player.draw()
            platform.draw()
            collides(player, platform)
            mend(fscreen, mt, mx, my)
            screen.blit(pg.transform.scale(fscreen, screen.get_rect().size), (0, 0))
            pg.display.flip()
            pg.time.Clock().tick(60)