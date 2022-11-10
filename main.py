import json
from Items import *
from Movement import Movement
from Windows import Window
from Checkboard import Checkboard
from functions import *

if __name__ == "__main__":
    main = Window().create
    Window().rename(main, f'Jeu de dame - {get_data("version")}')
    can = Checkboard().create(main)
    Checkboard().draw(can)
    main.mainloop()