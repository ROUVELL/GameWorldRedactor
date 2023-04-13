import pygame as pg

from canvas import Canvas
from renderer import Renderer
from panels import InfoPanel, ItemsPanel
from settings import *


class Engine:
    def __init__(self, clock: pg.time.Clock):
        self.sc = pg.display.get_surface()
        self.clock = clock
        # components
        self.canvas = Canvas(self)
        self.renderer = Renderer(self)
        self.info_panel = InfoPanel(self)
        self.items_panel = ItemsPanel(self)
        # flags
        self.is_preview = False

    @property
    def hover_on_canvas(self):
        return not (self.info_panel.is_hover or self.items_panel.is_hover)

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    exit()
                elif event.key == pg.K_p:
                    self.is_preview = not self.is_preview
                    # self.canvas.draw_grid = not self.is_preview
                elif event.key == pg.K_g:
                    self.canvas.draw_grid = not self.canvas.draw_grid
            self.items_panel.process_events(event)

    def update(self):
        self.canvas.update()

    def draw(self):
        self.sc.fill(BG)
        self.canvas.draw()
        if not self.is_preview:
            self.renderer.hovered_cell()
            self.info_panel.draw()
            self.items_panel.draw()
        self.renderer.fps()

