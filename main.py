import pygame as pg

from engine import Engine
from settings import SCREEN


def main():
    pg.init()
    pg.event.clear()
    pg.event.set_blocked(None)
    pg.event.set_allowed([pg.KEYUP, pg.MOUSEWHEEL])
    pg.display.set_mode(SCREEN, pg.NOFRAME)

    clock = pg.time.Clock()
    engine = Engine(clock)

    while True:
        clock.tick(0)

        engine.process_events()
        engine.update()
        engine.draw()

        pg.display.flip()


if __name__ == '__main__':
    main()
