import pygame as pg
from os import listdir

from panels.base_panel import BasePanel
from settings import *


class ItemsPanel(BasePanel):
    def __init__(self, engine):
        super().__init__(engine, ITEMS_PANEL_SIZE, ITEMS_PANEL_POS)
        self._items: dict[str, pg.Surface] = self.__load_items()
        self._surf = pg.Surface(self._rect.inflate(-40, -38).size)
        self._surf_rect = self._surf.get_rect(center=self._rect.center)
        self._yoffset = 0
        self.need_redraw = True

    def __load_items(self):
        tileset = pg.image.load('./data/tileset.png').convert_alpha()
        w, h = tileset.get_size()
        return {(x, y): tileset.subsurface((x, y, GRID_SIZE, GRID_SIZE))
                for y in range(0, h, GRID_SIZE) for x in range(0, w, GRID_SIZE)}

    def process_events(self, event: pg.event.Event):
        if not self.is_hover:
            return
        if event.type == pg.MOUSEWHEEL:
            self._yoffset += event.y * GRID_SIZE
            self.need_redraw = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self._yoffset += GRID_SIZE * 10
                self.need_redraw = True
            elif event.key == pg.K_DOWN:
                self._yoffset -= GRID_SIZE * 10
                self.need_redraw = True

    def draw(self):
        super().draw()
        if self.need_redraw:
            self._surf.fill('black')

            posx = 0
            posy = self._yoffset
            for item in self._items.values():
                self._surf.blit(item, (posx, posy))
                posx += GRID_SIZE
                if posx > self._surf_rect.width + GRID_SIZE:
                    posx = 0
                    posy += GRID_SIZE
            self.need_redraw = False

        self._sc.blit(self._surf, self._surf_rect)

        mx, my = pg.mouse.get_pos()
        if self._surf_rect.collidepoint(mx, my):
            rx, ry = self._surf_rect.topleft
            sx, sy = mx - rx, my - ry
            x, y = self.engine.canvas.mapping(sx, sy)
            pg.draw.rect(self._sc, 'green', (x + rx, y + ry, GRID_SIZE, GRID_SIZE), 1)

        # pg.draw.rect(self._sc, 'orange', self._surf_rect, 1)

