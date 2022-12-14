from Windows import *
from Checkboard import Checkboard
from Windows import Screen
import sys

w =  Screen()
c = Checkboard(w)

if __name__ == "__main__":
    main = Window().create
    Window().rename(main, f'Jeu de dame - {get_data("version")}')
    can = Checkboard().create(main)
    Checkboard().draw(can)
    Items().draw(can)
    main.mainloop()
