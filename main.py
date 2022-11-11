from classes.Checkboard import *
from classes.Items import *
from classes.Windows import *
from classes.usefull_functions import *

if __name__ == "__main__":
    main = Window().create
    Window().rename(main, f'Jeu de dame - {get_data("version")}')
    can = Checkboard().create(main)
    Checkboard().draw(can)
    Items().draw(can)
    main.mainloop()
    Canvas.create_oval(0,0,50,50)