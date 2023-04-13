import pygame as pg

from panels.base_panel import BasePanel
from settings import *


class InfoPanel(BasePanel):
    def __init__(self, engine):
        super().__init__(engine, INFO_PANEL_SIZE, INFO_PANEL_POS)
        self._text_pos = pg.Vector2(self._rect.topleft) + pg.Vector2(15, 8)
        self._termius24 = pg.font.Font(f'./data/terminus.ttf', 24)

    def draw(self):
        super().draw()
        if self.engine.hover_on_canvas:
            render = self._termius24.render(f'Mouse position: {self.engine.canvas.mouse_pos}', False, 'white')
            self._sc.blit(render, self._text_pos)