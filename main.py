from Windows import *
from Checkboard import Checkboard
from Windows import Screen
from Game import Game
import sys

g = Game()


if __name__ == "__main__":
    pg.init()
    pg.font.init()
    g.run()
    pg.quit()
    sys.exit()
