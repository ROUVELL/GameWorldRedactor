import pygame as pg


class BasePanel:
    def __init__(self, engine, size, pos):
        self.engine = engine
        self._sc = pg.display.get_surface()
        self._rect = pg.Rect((0, 0), size)
        self._rect.center = pos

    @property
    def is_hover(self):
        return self._rect.collidepoint(pg.mouse.get_pos())

    def draw(self):
        pg.draw.rect(self._sc, 'black', self._rect, border_radius=20)
        pg.draw.rect(self._sc, (120, 120, 120), self._rect, 1, border_radius=20)