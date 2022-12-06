import pygame
from .usefull_functions import get_data
from pygame import Color, draw, Rect, transform, image, time, mouse, MOUSEBUTTONDOWN, QUIT, display


class Checkboard:
    def __init__(self, screen):
        self.pictures = ["pb", "pn"]
        self.colors = [Color(f"white"), Color(f"black")]
        self.data = get_data("checkboard", "config.json")
        self.size = self.data["size"] // self.data["square"]
        self.screen = screen.set_screen
        self.first_run = True
        self.game = True
        self.board = [
            # 0     1     2     3     4     5     6     7     8     9
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],  # 0
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],  # 1
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],  # 2
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],  # 3
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],  # 4
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],  # 5
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],  # 6
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"],  # 7
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],  # 8
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"]  # 9
        ]

    @property
    def dessinerplateau(self):
        for i in range(self.data["square"]):
            for j in range(self.data["square"]):
                color = self.colors[((i + j) % 2)]
                draw.rect(self.screen, color, Rect(i * self.size, j * self.size, self.size, self.size))

    @property
    def dessinerpiece(self):
        for i in range(self.data["square"]):
            for j in range(self.data["square"]):
                piece = self.board[j][i]
                if piece != '--':
                    self.screen.blit(self.img[piece], Rect(i * self.size, j * self.size, self.size, self.size))
        return 0

    @property
    def chargement(self):
        picture_load = {}
        for i in self.pictures:
            picture_load[i] = transform.scale(image.load("pictures/" + i + ".png"), (self.size, self.size))
        return picture_load

    @property
    def dessinerstatut(self):
        self.dessinerplateau
        self.dessinerpiece

    @property
    def run(self):
        clock = time.Clock()
        self.img = self.chargement
        clickjoueur = []
        carreselectionne = ()
        while self.game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = False
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
            self.dessinerstatut
            display.flip()
            clock.tick(15)
        return 0

    def modifierboard(self, coordinit, coordfinal):
        x1, y1 = coordinit[1], coordinit[0]
        x2, y2 = coordfinal[1], coordfinal[0]
        print(f"Départ X,Y:\n - {coordinit}\nFinal X,Y:\n - {coordfinal}")
        if str(self.board[x1][y1]) == 'pb':
            if x1 == x2 - 1:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = str(self.board[x1][y1])
            if x1 == x2 - 2 and y1 == y2 + 2 or x1 == x2 - 2 and y1 == y2 - 2:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = str(self.board[x1][y1])
        else:
            if x1 == x2 + 1:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = str(self.board[x1][y1])
        if x1 == x2 + 2 and y1 == y2 + 2 or x1 == x2 + 2 and y1 == y2 - 2:
            self.board[x1][y1] = '--'
            self.board[x2][y2] = str(self.board[x1][y1])
        return self.dessinerplateau
