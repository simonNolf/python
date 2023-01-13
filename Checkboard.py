import pygame as pg
from Windows import Screen

window = Screen()


class Checkboard:
    def __init__(self):
        """
        Initialise une instance Checkboard avec des images correspondantes aux pions.
        Des couleurs afin de mettre le plateau en couleur.
        Des carrés pour savoir combien de carrés doivent être présent sur une ligne.
        Un screen pour la dimension de la fenêtre.
        Une size pour la taille des cases.
        Un turn pour savoir à qui s'est le tour de jouer.
        Un score pour avoir un score qui s'enregistre à la fin de la partie.
        Et un board qui est une liste de liste sue lequel le plateau est basé.

        """
        self.__pictures = ["wp", "bp", "wc", "bc"]
        self.__colors = [pg.Color("white"), pg.Color("brown")]
        self.square = 10
        self.__screen = pg.display.set_mode((1200, 800))
        self.__size = window.width // self.square
        self.__turn = True
        self.__score = {'blancs': 0, 'noirs': 0}
        self.__board = [
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]
        ]

    @property
    def board(self):
        """

        :return : la variable privée board
        """
        return self.__board

    @property
    def screen(self):
        """

        :return: la variable privé screen
        """
        return self.__screen

    @property
    def pictures(self):
        """

        :return : la variable privée pictures qui contient les images des pions
        """
        return self.__pictures

    @property
    def colors(self):
        """

        :return : les ifférentes couleurs
        """
        return self.__colors

    @property
    def size(self):
        """

        :return: la taille
        """
        return self.__size

    @property
    def turn(self):
        """

        :return : le tour, si c'est Tru, c'est au tour des blancs
        """
        return self.__turn

    @property
    def score(self):
        """

        : return : le score actuel
        """
        return self.__score

    def changeturn(self):
        """

        :return: l'inverse de l'actuel turn
        """
        self.__turn = not self.__turn



    def update_score(self, item, value):
        """

        : param item : la couleur
        : param value : le nombre de points gagné
        : return : ajoute le nombre de points gagné à la couleur correspondante
        """
        self.__score[item] += value

    def drawboard(self):
        """

        : return : renvoie le tbleau dessiné dans la fenêtre pygame
        """
        for i in range(self.square):
            for j in range(self.square):
                color = self.colors[((i + j) % 2)]
                pg.draw.rect(self.screen, color, pg.Rect(i * self.size, j * self.size, self.size, self.size))

    def drawpawns(self, img):
        """

        :param img : contient les images des pions
        : return : dessine les pions aux endroits où ils se trouvent dans board
        """
        for i in range(self.square):
            for j in range(self.square):
                piece = self.board[j][i]
                if piece != '--':
                    self.screen.blit(img[piece], pg.Rect(i * self.size, j * self.size, self.size, self.size))

    def loadpawns(self):
        """

        : return : charge les images dans pictures
        """
        picture_load = {}
        for i in self.pictures:
            picture_load[i] = pg.transform.scale(pg.image.load("pictures/" + i + ".png"), (self.size, self.size))
        return picture_load

    def drawstatus(self, img):
        """

        :param img : contients les images des pions
        : return : met à jour les messages dans la fenêtre pygame et redessine tout le tableau
        """
        self.drawpawns(img)
        self.display_score(810, 50)
        self.display_message(810, 350)
        self.pawn_to_cheek()

    def modifyboard(self, coorinitial, coorfinale):
        """
        :param coorinitial : contient un tuple de la case sélectionnée en premier.
        :param coorfinale : contient un tuple de la case sélectionnée où on veut que le pion se trouve.
        : return : met à jour le board si le mouvement est correct sinon, redemane la coordonnée initiale.
        """
        x1 = coorinitial[1]
        y1 = coorinitial[0]
        x2 = coorfinale[1]
        y2 = coorfinale[0]

        init_pawn = str(self.board[x1][y1])
        target = str(self.board[x2][y2])
        inter = ''

        if coorinitial == coorfinale and init_pawn == target:
            print("Vous devez jouer votre pion !")
            return False

        if init_pawn == 'wp' and self.turn:
            if y1 != len(self.board[x1]) - 1 and x1 != len(self.board) - 1 and x2 != len(self.board) - 1:
                inter = str(self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)])
            elif y1 == len(self.board[x1]) - 1:
                inter = str(self.board[x2 + 1][y1 - 1])
                self.update_score("blancs", 20)
            elif x1 != len(self.board) - 1:
                inter = str(self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)])
                self.update_score("blancs", 20)

            if x2 == x1 + 1 and y2 == y1 and target not in ['bp', 'wp']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = init_pawn
                self.changeturn()
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and target == '--' and inter == 'bp':
                self.board[x1][y1] = '--'
                self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = init_pawn
                self.update_score("blancs", 20)
                self.changeturn()
            else:
                return False

        elif init_pawn == 'bp' and not self.turn:
            if y1 != len(self.board[x1]) - 1 and x2 != len(self.board) - 1:
                inter = str(self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)])
            elif y1 == len(self.board[x2]) - 1 or x1 != len(self.board) - 1:
                inter = str(self.board[x2 + 1][y1 - 1])
                self.update_score("noirs", 20)

            if x2 == x1 - 1 and y2 == y1 and target not in ['bp', 'wp']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = init_pawn
                self.update_score("noirs", 20)
                self.changeturn()
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and target == '--' and inter == 'wp':
                self.board[x1][y1] = '--'
                self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = init_pawn
                self.update_score("noirs", 20)
                self.changeturn()
            else:
                return False

        else:
            self.warning_message(810, 400)
        return self.drawboard()

    def countpawns(self):
        """

        : return : met à jour l'information des pions présents sur le plateau
        """
        score = []
        white_pawns = 0
        black_pawns = 0
        white_cheek = 0
        black_cheek = 0
        for i in range(len(self.board)):
            white_value = self.board[i].count("wp")
            white_pawns += white_value
            black_value = self.board[i].count("bp")
            black_pawns += black_value
            wc_value = self.board[i].count("wc")
            white_cheek += wc_value
            bc_value = self.board[i].count("bc")
            black_cheek += bc_value

        score.append(white_pawns)
        score.append(black_pawns)
        score.append(white_cheek)
        score.append(black_cheek)
        return score

    def display_score(self, x, y):
        """

        :param x: coordonnée X.
        :param y : cordonnée Y
        : return : affiche les différents messages dans la fenêtre pygame
        """
        a = self.countpawns()
        font = pg.font.Font('StalshineRegular.ttf', 20)
        white_score = font.render("vous avez " + str(a[0]) + " pions blancs sur le plateau", True, (255, 255, 255),
                                  (0, 0, 0))
        elim_white = font.render("vous avez " + str(20 - a[0]) + " pions blancs éliminés", True, (255, 255, 255),
                                 (0, 0, 0))
        if str(a[2]) != 0:
            elim_white = font.render("vous avez " + str(20 - a[0] + a[2]) + " pions blancs éliminés", True,
                                     (255, 255, 255),
                                     (0, 0, 0))
        if a[0] == 19 or 20:
            elim_white = font.render("vous avez " + str(20 - a[0]) + " pion blanc éliminé", True, (255, 255, 255),
                                     (0, 0, 0))
        white_cheek = font.render("vous avez " + str(a[2]) + " dame blanches sur le plateau", True, (255, 255, 255),
                                  (0, 0, 0))
        self.screen.blit(white_score, (x, y))
        self.screen.blit(elim_white, (x, y + 70))
        self.screen.blit(white_cheek, (x, y + 35))
        black_score = font.render("vous avez " + str(a[1]) + " pions noirs sur le plateau", True, (255, 255, 255),
                                  (0, 0, 0))
        self.screen.blit(black_score, (x, y + 600))
        elim_black = font.render("vous avez " + str(20 - a[1]) + " pions noirs éliminés", True, (255, 255, 255),
                                 (0, 0, 0))
        if a[1] == 19 or 20:
            elim_black = font.render("vous avez " + str(20 - a[1]) + " pion noir éliminé", True, (255, 255, 255),
                                     (0, 0, 0))
        self.screen.blit(elim_black, (x, y + 635))
        pg.display.flip()

    def display_message(self, x, y):
        """

        :param x: coordonnée X
        :param y : coordonnée Y
        : return : affiche à qui s'est le tour de jouer
        """
        font = pg.font.Font('StalshineRegular.ttf', 30)
        turn = self.turn
        if turn:
            play = "blanc"
        else:
            play = "noir"
        message = font.render("c'est le tour des " + play + "             ", True, (0, 255, 0), (0, 0, 0))
        self.screen.blit(message, (x, y))
        pg.display.flip()

    def warning_message(self, x, y):
        """

        :param x: coordonnée X
        :param y: coordonnée Y
        : return : affiche un message si c'est pas le bon pion sélectionné
        """
        font = pg.font.Font('StalshineRegular.ttf', 30)
        turn = self.turn
        if turn:
            play = "blanc"
        else:
            play = "noir"
        message = font.render("sélectionnez un pion " + play + "   ", True, (255, 0, 0), (0, 0, 0))
        self.screen.blit(message, (x, y))
        pg.display.flip()

    def colorizesquare(self):
        """

        :return: met en couleur les coses sur lesquelles le pion sélectionné peut se déplacer
        """
        mousepos = pg.mouse.get_pos()
        col = mousepos[0] // self.size
        row = mousepos[1] // self.size
        if self.board[row][col] == "bp" or self.board[row][col] == "wp":
            rect = pg.Rect(col * self.size, row * self.size, self.size, self.size)
            pg.draw.rect(self.screen, (200, 50, 0), rect)

        if self.board[row][col] == "wp":
            if self.board[row][col] != self.board[8][col]:
                if self.board[row + 1][col - 1] == "bp" and self.board[row + 2][col - 2] == "--":
                    rect = pg.Rect(col * self.size - 2 * self.size, row * self.size + 2 * self.size, self.size,
                                   self.size)
                    pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row][col] != self.board[row][9] and self.board[row][col] != self.board[8][col]:
                if self.board[row + 1][col + 1] == "bp" and self.board[row + 2][col + 2] == "--":
                    rect = pg.Rect(col * self.size + 2 * self.size, row * self.size + 2 * self.size, self.size,
                                   self.size)
                    pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row + 1][col] == "--":
                rect = pg.Rect(col * self.size, row * self.size + self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

        if self.board[row][col] == "bp":
            if self.board[row][col] != self.board[row][9]:
                if self.board[row - 1][col + 1] == "wp" and self.board[row - 2][col + 2] == "--":
                    rect = pg.Rect(col * self.size + 2 * self.size, row * self.size - 2 * self.size, self.size,
                                   self.size)
                    pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row - 1][col - 1] == "wp" and self.board[row - 2][col - 2] == "--":
                rect = pg.Rect(col * self.size - 2 * self.size, row * self.size - 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row - 1][col] == "--":
                rect = pg.Rect(col * self.size, row * self.size - self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

    def pawn_to_cheek(self):
        for i in range(len(self.board[0])):
            if self.board[0][i] == "bp":
                self.board[0][i] = "bc"
        for i in range(len(self.board[9])):
            if self.board[9][i] == "wp":
                self.board[9][i] = "wc"
