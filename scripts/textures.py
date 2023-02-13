import pygame as pg
import os

class txt:
    class buttons:
        play = pg.image.load("textures/buttons/play.png")
        exit = pg.image.load("textures/buttons/exit.png")
        create = pg.image.load("textures/buttons/create.png")
        new = pg.image.load("textures/buttons/new.png")
        back = pg.image.load("textures/buttons/back.png")
        load = pg.image.load("textures/buttons/load.png")
    class player:
        class crouch:
            _0 = pg.image.load("textures/player/crouch/0.png")
        class idle:
            _0 = pg.image.load("textures/player/idle/0.png")
            _1 = pg.image.load("textures/player/idle/1.png")
            _2 = pg.image.load("textures/player/idle/2.png")
            _3 = pg.image.load("textures/player/idle/3.png")
            _4 = pg.image.load("textures/player/idle/4.png")
        class walk:
            _0 = pg.image.load("textures/player/walk/0.png")
            _1 = pg.image.load("textures/player/walk/1.png")
            _2 = pg.image.load("textures/player/walk/2.png")
            _3 = pg.image.load("textures/player/walk/3.png")
            _4 = pg.image.load("textures/player/walk/4.png")
    cours_1 = pg.image.load("textures/cours_1.png")
    cours_2 = pg.image.load("textures/cours_2.png")
    icon = pg.image.load("textures/plant_man_icon.png")
    bg = pg.image.load("textures/bg.png")