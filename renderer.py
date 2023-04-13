import pygame as pg

from settings import *


class Renderer:
    def __init__(self, engine):
        self.engine = engine
        self._sc = pg.display.get_surface()
        # font
        self._termius32 = pg.font.Font('data/terminus.ttf', 32)


    def hovered_cell(self):
        if not self.engine.hover_on_canvas:
            return
        mx, my = pg.mouse.get_pos()
        ox, oy = self.engine.canvas.offset
        mapx, mapy = self.engine.canvas.mapping((mx - ox), (my - oy))
        x, y = mapx + ox, mapy + oy
        pg.draw.rect(self._sc, SELECTOR_COLOR, (x, y, GRID_SIZE, GRID_SIZE), 2, 3)

    def fps(self):
        fps = self._termius32.render(f'{int(self.engine.clock.get_fps())}', False, FPS_COLOR)
        self._sc.blit(fps, (4, 0))
