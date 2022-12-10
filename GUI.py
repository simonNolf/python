import sys
import pygame as pg

height = 800
width = 800
size = 800 // 10
new_color = (200, 200, 200)
screen = pg.display.set_mode((800, 950))

textX = 50
texteY = 810
board = [
    ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
    ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
    ["--", "pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb"],
    ["pb", "--", "pb", "--", "pb", "--", "pb", "--", "pb", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],
    ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"],
    ["--", "pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn"],
    ["pn", "--", "pn", "--", "pn", "--", "pn", "--", "pn", "--"]]


def compter_pions():
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


def bas(mouse_pos):
    return mouse_pos[0], mouse_pos[1] + size


def ecrire_score(x, y):
    a = compter_pions()
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


def modifierboard(coorinitial, coorfinale):
    x1 = coorinitial[1]
    y1 = coorinitial[0]
    x2 = coorfinale[1]
    y2 = coorfinale[0]
    valeur1 = str(board[x1][y1])
    # pionennemi1 = board[x1 + 1][y1 - 1]
    # pionennemi2 = board[x1 + 1][y1 + 1]
    if valeur1 == 'pb':
        if x1 == x2 - 1:
            board[x1][y1] = '--'
            board[x2][y2] = str(valeur1)
        if x1 == x2 - 2 and y1 == y2 + 2 or x1 == x2 - 2 and y1 == y2 - 2:
            board[x1][y1] = '--'
            board[x2][y2] = str(valeur1)
    else:
        if x1 == x2 + 1:
            board[x1][y1] = '--'
            board[x2][y2] = str(valeur1)
    if x1 == x2 + 2 and y1 == y2 + 2 or x1 == x2 + 2 and y1 == y2 - 2:
        board[x1][y1] = '--'
        board[x2][y2] = str(valeur1)
    return dessinerplateau()


def chargement():
    images = ["pb", "pn"]
    image_charge = {}
    for i in images:
        image_charge[i] = pg.transform.scale(pg.image.load("pictures/" + i + ".png"), (size, size))
    return image_charge


def dessinerplateau():
    screen.fill((0, 0, 0))
    couleurs = [pg.Color("white"), pg.Color("black")]
    for i in range(10):
        for j in range(10):
            couleur = couleurs[((i + j) % 2)]
            pg.draw.rect(screen, couleur, pg.Rect(i * size, j * size, size, size))


def dessinerpiece(board, img):
    for i in range(10):
        for j in range(10):
            piece = board[j][i]
            if piece != '--':
                screen.blit(img[piece],
                            pg.Rect(i * size, j * size, size, size))


def dessinerstatut(board, img):
    # dessinerplateau()
    dessinerpiece(board, img)
    ecrire_score(textX, texteY)


def affichercouleur():
    mousepos = pg.mouse.get_pos()
    col = mousepos[0] // size
    row = mousepos[1] // size

    rect = pg.Rect(col * size, row * size, size, size)
    pg.draw.rect(screen, (200, 50, 0), rect)

    if board[row][col] == "pb":
        if board[row + 1][col - 1] == "pn" and board[row + 2][col - 2] == "--":
            rect = pg.Rect(col * size - 2 * size, row * size + 2 * size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)

        if board[row + 1][col + 1] == "pn" and board[row + 2][col + 2] == "--":
            rect = pg.Rect(col * size + 2 * size, row * size + 2 * size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)

        if board[row + 1][col] == "--":
            rect = pg.Rect(col * size, row * size + size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)

    if board[row][col] == "pn":
        if board[row - 1][col + 1] == "pb" and board[row - 2][col + 2] == "--":
            rect = pg.Rect(col * size + 2 * size, row * size - 2 * size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)

        if board[row - 1][col - 1] == "pb" and board[row - 2][col - 2] == "--":
            rect = pg.Rect(col * size - 2 * size, row * size - 2 * size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)

        if board[row - 1][col] == "--":
            rect = pg.Rect(col * size, row * size - size, size, size)
            pg.draw.rect(screen, (0, 200, 55), rect)


def main():
    dessinerplateau()
    clock = pg.time.Clock()
    img = chargement()
    clickjoueur = []
    # carreselectionne = ()
    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pos()
                row = click[0] // size
                col = click[1] // size
                # if carreselectionne == (row, col):
                #     carreselectionne = ()
                #     clickjoueur = []
                # else:
                #     carreselectionne = (row, col)
                #     clickjoueur.append(carreselectionne)
                carreselectionne = (row, col)
                clickjoueur.append(carreselectionne)
                if len(clickjoueur) == 1:
                    print(row, col)
                    affichercouleur()
                    # print(clickjoueur)
                if len(clickjoueur) == 2:
                    # print(clickjoueur)
                    modifierboard(clickjoueur[0], clickjoueur[1])
                    # carreselectionne = ()
                    clickjoueur = []
                    dessinerplateau()

                    print(row, col)
                    for item in board:
                        print(item)

        dessinerstatut(board, img)
        pg.display.flip()
        clock.tick(15)


if __name__ == '__main__':
    chargement()
    pg.init()
    pg.font.init()
    main()
    pg.quit()
    sys.exit()
