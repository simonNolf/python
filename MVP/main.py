class GameState:

    def __init__(self):

        self.board = [
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
            ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
            ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"],
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],
            ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"],
            ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"]]

        self.hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        self.ver = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        self.tour_blancs = True

        self.piece_blanc = 20
        self.piece_noir = 20

    def board(self):
        return self.board

    def drawboard(self):
        for i in range(10):
            for x in range(10):
                print(GameState.board(self)[i][x], end='  ')
            print()


def main():
    gs = GameState()
    q = ''

    print('règlement')

    print("les blancs vont commencer")

    while q != 'quit':

        if gs.tour_blancs:
            print('c\'est au tour des blancs de jouer !')
            gs.tour_blancs = False
        else:
            print('c\'est au tour des noirs de jouer !')
            gs.tour_noir = True

        gs.drawboard()

        pos = input('inserez les coordonnées d\'une case contenant l\'une de vos pièces').lower()

        while pos != 'ff' and gs.board[gs.hor.index(pos[0])][gs.ver.index(pos[1:])] == '--':
            pos = input('inserez les coordonnées correctes d\'une case contenant l\'une de vos pièces').lower()

        if pos == 'ff':
            if gs.tour_blancs:
                print('les blancs ont gagné car les noirs ont déclaré forfait')
                break
            else:
                print('les noirs ont gagné car les humains ont déclaré forfait')
                break
        else:
            deplacement = input('ou voulez vous déplacer la pièce choisis ?').lower()

            gs.board[gs.hor.index(deplacement[0])][gs.ver.index(deplacement[1:])] = gs.board[gs.hor.index(pos[0])][
                gs.ver.index(pos[1:])]

            gs.board[gs.hor.index(pos[0])][gs.ver.index(pos[1:])] = '--'

        for x in range(len(gs.board)):
            if len(set(gs.board[x])) > 1:
                break
            else:
                q = 'quit'

    print('partie terminé')


def affichage_legende():
    print()


if __name__ == "__main__":
    affichage_legende()

    main()
