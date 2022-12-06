from classes.Windows import Screen
from classes.Checkboard import Checkboard
from classes.usefull_functions import get_data

if __name__ == '__main__':
    main = Screen(get_data("checkboard", "config.json")["size"])
    main.set_name("Bienvenue sur PyDames")
    main.set_picture()
    check_board = Checkboard(main)
    check_board.run