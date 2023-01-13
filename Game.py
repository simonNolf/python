import pygame as pg
from Checkboard import Checkboard

c = Checkboard()


class Game:
    def __init__(self):
        """
        set l'état de game a True
        """
        self.__game = True

    @property
    def game(self):
        """

        :return: renvoie l'état de la variable game
        """
        return self.__game

    def finished(self):
        """

        :return: met l'état de la variable game a False
        """
        self.__game = False

    def run(self):
        """

        : return : lance tout le programme principal
        """
        c.drawboard()
        clock = pg.time.Clock()
        img = c.loadpawns()
        clicks = []
        while self.game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sauvergarde()
                    self.finished()
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = pg.mouse.get_pos()
                    row = click[0] // c.size
                    col = click[1] // c.size
                    carreselectionne = (row, col)
                    clicks.append(carreselectionne)
                    if len(clicks) == 1:
                        c.colorizesquare()
                    if len(clicks) == 2:
                        c.modifyboard(clicks[0], clicks[1])
                        clicks = []
                        c.drawboard()

            c.drawstatus(img)
            pg.display.flip()
            clock.tick(15)

    def sauvergarde(self):
        """

        :return : souvegarde le score dans un fichier text à part
        """
        file = open("score.txt", "w")
        w = str(c.score["blancs"])
        b = str(c.score["noirs"])
        file.write("score des blancs : " + w + "\n")
        file.write("score des noirs: " + b)
        file.close()
