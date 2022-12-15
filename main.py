from Windows import *
from Checkboard import Checkboard
from Windows import Screen
import sys

w = Screen()
c = Checkboard(w)

if __name__ == "__main__":
    c.loadpawns()
    pg.init()
    pg.font.init()
    c.run()
    pg.quit()
    sys.exit()
