import sys

import pygame
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


def chargement():
    images = ["pb", "pn"]
    image_charge = {}
    for i in images:
        image_charge[i] = pg.transform.scale(pg.image.load("pictures/" + i + ".png"), (size, size))
    return image_charge


def dessinerplateau():
    couleurs = [pg.Color("white"), pg.Color("black")]
    for i in range(width):
        for j in range(width):
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
    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        dessinerstatut(board, img)
        pg.display.flip()
        clock.tick(15)


if __name__ == '__main__':
    chargement()
    pg.init()
    main()
    pg.quit()
    sys.exit()
