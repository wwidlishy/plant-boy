import pygame as pg

from scripts.textures import txt

class Platform:
    def __init__(self, fscreen, pos, size) -> None:
        self.fscreen = fscreen
        self.pos = pos
        self.size = size
        self.dead = False
        self.sx, self.sy = list(size)
        self.x, self.y = list(pos)
        self.rect = pg.Rect(self.x, self.y, self.sx, self.sy)
    def draw(self) -> None:
        x, y = list(self.pos)
        sx, sy = list(self.size)
        pg.draw.rect(self.fscreen, (255, 255, 255), pg.Rect(x, y, sx, sy))
    def get_size(self):
        return [self.sx, self.sy]
    def get_pos(self):
        return list(self.pos)
    def get_rect(self):
        return self.rect