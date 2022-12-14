import pygame as pg
from Windows import Screen

window = Screen()


class Checkboard:
    def __init__(self, window):
        self.__pictures = ["wp", "bp"]
        self.__colors = [pg.Color("white"), pg.Color("black")]
        self.square = 10
        self.__screen = pg.display.set_mode((1100, 800))
        self.__size = window.width // self.square
        self.__first_run = True
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
    def size(self):
        return self.__size

    def drawboard(self):
        self.screen.fill((0, 0, 0))

        for i in range(self.square):
            for j in range(self.square):
                color = self.colors[((i + j) % 2)]
                pg.draw.rect(self.screen, color, pg.Rect(i * self.size, j * self.size, self.size, self.size))

    def drawpawns(self, img):
        for i in range(self.square):
            for j in range(self.square):
                piece = self.board[j][i]
                if piece != '--':
                    self.screen.blit(img[piece], pg.Rect(i * self.size, j * self.size, self.size, self.size))

    def loadpawns(self):
        picture_load = {}
        for i in self.pictures:
            picture_load[i] = pg.transform.scale(pg.image.load("pictures/" + i + ".png"), (self.size, self.size))
        return picture_load

    def drawstatus(self, img):
        self.drawpawns(img)
        self.display_score(810, 50)

    def run(self):
        self.drawboard()
        clock = pg.time.Clock()
        img = self.loadpawns()
        clicks = []
        game = True
        while game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = pg.mouse.get_pos()
                    row = click[0] // self.size
                    col = click[1] // self.size
                    carreselectionne = (row, col)
                    clicks.append(carreselectionne)
                    if len(clicks) == 1:
                        self.colorizesquare()
                    if len(clicks) == 2:
                        self.modifyboard(clicks[0], clicks[1])
                        clicks = []
                        self.drawboard()

            self.drawstatus(img)

            pg.display.flip()
            clock.tick(15)

    def modifyboard(self, coorinitial, coorfinale):
        x1 = coorinitial[1]
        y1 = coorinitial[0]
        x2 = coorfinale[1]
        y2 = coorfinale[0]

        init_pawn = str(self.board[x1][y1])
        target = str(self.board[x2][y2])

        if init_pawn == 'wp':
            if self.board[x1][y1] != self.board[x1][9]:
                inter = str(self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)])

            if x2 == x1 + 1 and y2 == y1 and target not in ['bp', 'wp']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = init_pawn
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and target == '--' and inter == 'bp':
                self.board[x1][y1] = '--'
                self.board[x2 - 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = init_pawn
        elif init_pawn == 'bp':
            if self.board[x1][y1] != self.board[x1][9]:
                inter = str(self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)])
            if x2 == x1 - 1 and y2 == y1 and target not in ['bp', 'wp']:
                self.board[x1][y1] = '--'
                self.board[x2][y2] = init_pawn
            elif y2 in range(y1 - 3, y1 + 3) and y2 not in [y1 - 1, y1, y1 + 1] and x2 in range(
                    x1 + 3) and x2 not in [x1 - 1, x1, x1 + 1] and target == '--' and inter == 'wp':
                self.board[x1][y1] = '--'
                self.board[x2 + 1][(y1 - 1) if y2 < y1 else (y1 + 1)] = '--'
                self.board[x2][y2] = init_pawn
        return self.drawboard()

    def countpawns(self):
        score = []
        white_pawns = 0
        black_pawns = 0
        for i in range(len(self.board)):
            white_value = self.board[i].count("wp")
            white_pawns += white_value
            black_value = self.board[i].count("bp")
            black_pawns += black_value
        score.append(white_pawns)
        score.append(black_pawns)
        return score

    def display_score(self, x, y):
        a = self.countpawns()
        font = pg.font.Font('StalshineRegular.ttf', 20)
        white_score = font.render("vous avez " + str(a[0]) + " pions blancs sur le plateau", True, (255, 255, 255))
        elim_white = font.render("vous avez " + str(20 - a[0]) + " pions blancs éliminés", True, (255, 255, 255))
        if a[0] == 19 or 20:
            elim_white = font.render("vous avez " + str(20 - a[0]) + " pion blanc éliminé", True, (255, 255, 255))
        self.screen.blit(white_score, (x, y))
        self.screen.blit(elim_white, (x, y + 35))
        black_score = font.render("vous avez " + str(a[1]) + " pions noirs sur le plateau", True, (255, 255, 255))
        self.screen.blit(black_score, (x, y + 600))
        elim_black = font.render("vous avez " + str(20 - a[1]) + " pions noirs éliminés", True, (255, 255, 255))
        if a[1] == 19 or 20:
            elim_black = font.render("vous avez " + str(20 - a[1]) + " pion noir éliminé", True, (255, 255, 255))
        self.screen.blit(elim_black, (x, y + 635))
        pg.display.flip()

    def colorizesquare(self):
        mousepos = pg.mouse.get_pos()
        col = mousepos[0] // self.size
        row = mousepos[1] // self.size
        if self.board[row][col] == "bp" or self.board[row][col] == "wp":
            rect = pg.Rect(col * self.size, row * self.size, self.size, self.size)
            pg.draw.rect(self.screen, (200, 50, 0), rect)

        if self.board[row][col] == "wp":
            if self.board[row + 1][col - 1] == "bp" and self.board[row + 2][col - 2] == "--":
                rect = pg.Rect(col * self.size - 2 * self.size, row * self.size + 2 * self.size, self.size, self.size)
                pg.draw.rect(self.screen, (0, 200, 55), rect)

            if self.board[row][col] != self.board[row][9]:
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
