import pygame as pg
from pygame.gfxdraw import vline, hline

from settings import *


class Canvas:
    def __init__(self, engine):
        self.engine = engine
        self._sc = engine.sc
        self._origin = pg.Vector2(CENTER)
        # flags
        self.draw_grid = True

    def mapping(self, x, y):
        """Переводить координати в позицію верхнього лівого кутка відповідної клітинки"""
        return (x // GRID_SIZE) * GRID_SIZE, (y // GRID_SIZE) * GRID_SIZE

    @property
    def origin(self):
        return int(self._origin.x), int(self._origin.y)

    @property
    def offset(self):
        ox, oy = self.origin
        mapx, mapy = self.mapping(ox, oy)
        return ox - mapx, oy - mapy

    @property
    def mouse_pos(self):
        """Індекс квадрата на який наведено мишкою"""
        mx, my = pg.mouse.get_pos()
        ox, oy = self.origin
        x = (mx - ox) // GRID_SIZE
        y = (my - oy) // GRID_SIZE
        return x, y

    def update(self):
        rel = pg.mouse.get_rel()
        if pg.mouse.get_pressed()[1]:
            self._origin += pg.Vector2(rel)

    def draw(self):
        if self.draw_grid:
            offsetx, offsety = self.offset
            [vline(self._sc, dx, 0, HEIGHT, GRID_COLOR) for dx in range(offsetx, WIDTH, GRID_SIZE)]
            [hline(self._sc, 0, WIDTH, dy, GRID_COLOR) for dy in range(offsety, HEIGHT, GRID_SIZE)]

            ox, oy = self.origin
            if -1 < ox < WIDTH:
                vline(self._sc, ox, 0, HEIGHT, ORIGIN_COLOR)
            if -1 < oy < HEIGHT:
                hline(self._sc, 0, WIDTH, oy, ORIGIN_COLOR)

