import sys
import pygame as pg

height = 800
width = 800
size = height // 10
new_color = (200, 200, 200)
screen = pg.display.set_mode((800, 800))
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


def bas(mouse_pos):
    return mouse_pos[0], mouse_pos[1] + size


def modifierboard(coorinitial, coorfinale):
    x1 = coorinitial[1]
    y1 = coorinitial[0]
    x2 = coorfinale[1]
    y2 = coorfinale[0]
    print(coorinitial)
    print(coorfinale)
    valeur1 = str(board[x1][y1])
    pionennemi1 = board[x1 - 1][y1 + 1]
    pionennemi2 = board[x1 + 1][y1 + 1]
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
    dessinerplateau()
    dessinerpiece(board, img)


def main():
    clock = pg.time.Clock()
    img = chargement()
    clickjoueur = []
    carreselectionne = ()
    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pos()
                row = click[0] // size
                col = click[1] // size
                if carreselectionne == (row, col):
                    carreselectionne = ()
                    clickjoueur = []
                else:
                    carreselectionne = (row, col)
                    clickjoueur.append(carreselectionne)
                if len(clickjoueur) == 2:
                    modifierboard(clickjoueur[0], clickjoueur[1])
                    carreselectionne = ()
                    clickjoueur = []

        dessinerstatut(board, img)
        pg.display.flip()
        clock.tick(15)


if __name__ == '__main__':
    chargement()
    pg.init()
    main()
    pg.quit()
    sys.exit()
