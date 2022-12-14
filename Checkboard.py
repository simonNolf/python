import pygame as pg
from Windows import Screen

window = Screen()


class Checkboard:
    def __init__(self, window):
        self.__pictures = ["pb", "pn"]
        self.__colors = [pg.Color("white"), pg.Color("black")]
        self.__data = {
            "size": 800,
            "square": 10
        }
        self.__screen = window().set_screen
        self.__size = window().width() // 10
        self.__first_run = True
        self.__board = [
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"],
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"]
        ]

    @property
    def board(self):
        return self.__board

    @property
    def first_run(self):
        return self.__first_run

    @property
    def screen(self):
        return self.__screen

    @property
    def pictures(self):
        return self.__pictures

    @property
    def colors(self):
        return self.__colors

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return self.__size

    def dessinerplateau(self):
        for i in range(self.data["square"]):
            for j in range(self.data["square"]):
                color = self.colors[((i + j) % 2)]
                draw.rect(self.screen, color, Rect(i * self.size, j * self.size, self.size, self.size))

    def dessinerpiece(self, img):
        for i in range(self.data["square"]):
            for j in range(self.data["square"]):
                piece = self.board[j][i]
                if piece != '--':
                    self.screen.blit(img[piece], Rect(i * self.size, j * self.size, self.size, self.size))

    def chargement(self):
        picture_load = {}
        for i in self.pictures:
            picture_load[i] = transform.scale(image.load("pictures/" + i + ".png"), (self.size, self.size))
        return picture_load

    def dessinerstatut(self, img):
        self.dessinerplateau()
        self.dessinerpiece(img)

    def run(self):
        game = True
        clock = time.Clock()
        img = self.chargement()
        clickjoueur = []
        carreselectionne = ()
        while game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game = False
                if event.type == MOUSEBUTTONDOWN:
                    if carreselectionne == (mouse.get_pos()[0] // self.size, mouse.get_pos()[1] // self.size):
                        carreselectionne = ()
                        clickjoueur = []
                    else:
                        carreselectionne = (mouse.get_pos()[0] // self.size, mouse.get_pos()[1] // self.size)
                        clickjoueur.append(carreselectionne)
                    if len(clickjoueur) == 2:
                        self.modifierboard(clickjoueur[0], clickjoueur[1])
                        carreselectionne = ()
                        clickjoueur = []
            self.dessinerstatut(img)
            display.flip()
            clock.tick(15)
        return 0

    def modifierboard(self, coorinitial, coorfinale):
        x1 = coorinitial[1]
        y1 = coorinitial[0]
        x2 = coorfinale[1]
        y2 = coorfinale[0]

        pion_init = str(self.board[x1][y1])
        cible = str(self.board[x2][y2])

        if pion_init == 'pb':
            inter = str(self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)])

            if x2 == x1 + 1 and y2 == y1 and cible not in ['pn', 'pb']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = pion_init
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and cible == '--' and inter == 'pn':
                self.board[x1][y1] = '--'
                self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = pion_init
        elif pion_init == 'pn':
            inter = str(self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)])

            if x2 == x1 - 1 and y2 == y1 and cible not in ['pn', 'pb']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = pion_init
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and cible == '--' and inter == 'pb':
                self.board[x1][y1] = '--'
                self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = pion_init
            else:
                print("dd")

        return self.dessinerplateau()

    def affichercouleur(self):
        mousepos = pg.mouse.get_pos()
        col = mousepos[0] // self.size
        row = mousepos[1] // self.size

        rect = pg.Rect(col * self.size, row * self.size, self.size, self.size)
        pg.draw.rect(self.screen, (200, 50, 0), rect)

        if self.board[row][col] == "pb":
            if self.board[row + 1][col - 1] == "pn" and self.board[row + 2][col - 2] == "--":
                rect = pg.Rect(col * self.size - 2 * self.size, row * self.size + 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row + 1][col + 1] == "pn" and self.board[row + 2][col + 2] == "--":
                rect = pg.Rect(col * self.size + 2 * self.size, row * self.size + 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row + 1][col] == "--":
                rect = pg.Rect(col * self.size, row * self.size + self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

        if self.board[row][col] == "pn":
            if self.board[row - 1][col + 1] == "pb" and self.board[row - 2][col + 2] == "--":
                rect = pg.Rect(col * self.size + 2 * self.size, row * self.size - 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row - 1][col - 1] == "pb" and self.board[row - 2][col - 2] == "--":
                rect = pg.Rect(col * self.size - 2 * self.size, row * self.size - 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row - 1][col] == "--":
                rect = pg.Rect(col * self.size, row * self.size - self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)
