import pygame as pg

def collides(o1, o2):
    o1rect = pg.Rect(o1.get_pos()[0], o1.get_pos()[1], o1.get_size()[0], o1.get_size()[1])
    o2rect = pg.Rect(o2.get_pos()[0], o2.get_pos()[1], o2.get_size()[0], o2.get_size()[1])
    if o1rect.colliderect(o2rect):
        if o1rect.bottom >= o2rect.top and (o1rect.right in range(o2.x, o2.x+o2.sx) or o1rect.left in range(o2.x, o2.x+o2.sx)):
            if o1rect.y >= o2rect.y:
                if o2rect.y + 10 <= o1rect.y:
                    o1rect.bottom = o2rect.top
                else:
                    pass
            else:
                o1rect.bottom = o2rect.top
        o1.pos = (o1rect.x, o1rect.y)

def colide(o1, o2):
    o1rect = pg.Rect(o1.get_pos()[0], o1.get_pos()[1], o1.get_size()[0], o1.get_size()[1])
    o2rect = pg.Rect(o2.get_pos()[0], o2.get_pos()[1], o2.get_size()[0], o2.get_size()[1])
    if o1rect.colliderect(o2rect):
        return True
    return False