import pygame as pg

from scripts.textures import txt

class Player:
    def __init__(self, fscreen, pos) -> None:
        self.fscreen = fscreen
        self.pos = pos
        self.moving = False
        self.aniC = 0
        self.aniI = 0
        self.direction = ""
        self.sx, self.sy = 0, 0
        self.rect = pg.Rect(self.get_pos()[0], self.get_pos()[1], self.sx, self.sy)
    def draw(self) -> None:
        self.pos = (self.get_pos()[0], self.get_pos()[1]+1)
        if pg.key.get_pressed()[pg.K_d]:
            self.moving = True
            self.direction = "d"
        elif pg.key.get_pressed()[pg.K_a]:
            self.moving = True
            self.direction = "a"
        if not pg.key.get_pressed()[pg.K_d] and not pg.key.get_pressed()[pg.K_a]:
            self.moving = False        
        if not self.moving:
                self.direction = ""
                self.aniC += 1
                idle = [pg.transform.scale(txt.player.idle._0, (64, 88)), pg.transform.scale(txt.player.idle._1, (64, 88)), pg.transform.scale(txt.player.idle._2, (64, 88)), pg.transform.scale(txt.player.idle._3, (64, 88)), pg.transform.scale(txt.player.idle._4, (64, 88))]
                if self.aniI == len(idle)-1:
                    self.aniI = 0
                if self.aniC == 15:
                    if self.aniI == len(idle)-1:
                        self.aniI = 0
                    else:
                        self.aniI += 1
                    self.aniC = 0
                self.sx, self.sy = idle[self.aniI].get_size()
                self.fscreen.blit(idle[self.aniI], self.pos)
        if self.moving:
            if self.direction == "d":
                self.aniC += 1
                d = [pg.transform.scale(txt.player.walk._0, (64, 88)), pg.transform.scale(txt.player.walk._1, (64, 88)), pg.transform.scale(txt.player.walk._2, (64, 88)), pg.transform.scale(txt.player.walk._3, (64, 88)), pg.transform.scale(txt.player.walk._4, (64, 88))]
                if self.aniI == len(d)-1:
                    self.aniI = 0
                if self.aniC == 15:
                    if self.aniI == len(d)-1:
                        self.aniI = 0
                    else:
                        self.aniI += 1
                    self.aniC = 0
                x, y = list(self.pos)
                self.pos = (x+5, y)
                self.sx, self.sy = d[self.aniI].get_size()
                self.fscreen.blit(d[self.aniI], self.pos)
            if self.direction == "a":
                self.aniC += 1
                #pg.transform.scale(pg.transform.flip(txt.player.walk._0, (64, 88), True, False))
                a = [
                    pg.transform.scale(pg.transform.flip(txt.player.walk._0,True, False), (64, 88)), 
                    pg.transform.scale(pg.transform.flip(txt.player.walk._1,True, False), (64, 88)), 
                    pg.transform.scale(pg.transform.flip(txt.player.walk._2,True, False), (64, 88)), 
                    pg.transform.scale(pg.transform.flip(txt.player.walk._3,True, False), (64, 88)), 
                    pg.transform.scale(pg.transform.flip(txt.player.walk._4,True, False), (64, 88))
                    ]
                if self.aniI == len(a)-1:
                    self.aniI = 0
                if self.aniC == 15:
                    if self.aniI == len(a)-1:
                        self.aniI = 0
                    else:
                        self.aniI += 1
                    self.aniC = 0
                x, y = list(self.pos)
                self.pos = (x-5, y)
                self.sx, self.sy = a[self.aniI].get_size()
                self.fscreen.blit(a[self.aniI], self.pos)
    def get_size(self):
        return [self.sx, self.sy]
    def get_pos(self):
        return list(self.pos)