class Pawn:
    def __init__(self, pawn, data):
        self.__pawn = pawn
        self.__data = data
        self.__size = self.data["size"] // self.data["square"]

    @property
    def pawn(self):
        return self.__pawn

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return self.__size

    def compter_pions(self):
        score = []
        pions_blancs = 0
        pions_noirs = 0
        for i in range(len(board)):
            valeur_blanc = board[i].count("pb")
            pions_blancs += valeur_blanc
            valeur_noir = board[i].count("pn")
            pions_noirs += valeur_noir
        score.append(pions_blancs)
        score.append(pions_noirs)
        return score

    def ecrire_score(self, x, y):
        a = self.compter_pions()
        font = pg.font.Font('StalshineRegular.ttf', 20)
        scoreblanc = font.render("vous avez " + str(a[0]) + " pions blancs sur le plateau", True, (255, 255, 255))
        elim_blanc = font.render("vous avez " + str(20 - a[0]) + " pions blancs éliminés", True, (255, 255, 255))
        if a[0] == 19 or 20:
            elim_blanc = font.render("vous avez " + str(20 - a[0]) + " pion blanc éliminé", True, (255, 255, 255))
        screen.blit(scoreblanc, (x, y))
        screen.blit(elim_blanc, (x, y + 35))
        scorenoir = font.render("vous avez " + str(a[1]) + " pions noirs sur le plateau", True, (255, 255, 255))
        screen.blit(scorenoir, (x + 400, y))
        elim_noir = font.render("vous avez " + str(20 - a[1]) + " pions noirs éliminés", True, (255, 255, 255))
        if a[1] == 19 or 20:
            elim_noir = font.render("vous avez " + str(20 - a[1]) + " pion noir éliminé", True, (255, 255, 255))
        screen.blit(elim_noir, (x + 400, y + 35))
        pg.display.flip()
