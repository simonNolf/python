import sys
import pygame as pg

height = 800
width = 800
size = height // 10
new_color = (200, 200, 200)


def bas_droite(mouse_pos):
    return mouse_pos[0], mouse_pos[1] + 80


def main():
    screen = pg.display.set_mode((800, 800))
    clock = pg.time.Clock()
    color = (255, 255, 255)

    rectangles = []
    for y in range(10):
        for x in range(10):
            rect = pg.Rect(x * (size + 1), y * (size + 1), size, size)
            if y % 2 == 0:
                if x % 2 == 1:
                    color = (0, 0, 0)
                    rectangles.append((rect, color))
                else:
                    color = (255, 255, 255)
                    # The grid will be a list of (rect, color) tuples.
                    rectangles.append((rect, color))
            else:
                if x % 2 == 0:
                    color = (0, 0, 0)
                    rectangles.append((rect, color))
                else:
                    color = (255, 255, 255)
                    # The grid will be a list of (rect, color) tuples.
                    rectangles.append((rect, color))
    done = False
    print(rectangles[0][1])

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        if pg.mouse.get_pressed()[0]:
            mouse_pos = pg.mouse.get_pos()
            print(pg.mouse.get_pos())
            b = bas_droite(mouse_pos)
            print(b)
            # Enumerate creates tuples of a number (the index)
            # and the rect-color tuple, so it looks like:
            # (0, (<rect(0, 0, 20, 20)>, (255, 255, 255)))
            # You can unpack them directly in the head of the loop.
            for index, (rect, color) in enumerate(rectangles):

                if rect.collidepoint(b):
                    # Create a tuple with the new color and assign it.
                    rectangles[index] = (rect, new_color)

        screen.fill((30, 30, 30))

        # Now draw the rects. You can unpack the tuples
        # again directly in the head of the for loop.
        for rect, color in rectangles:
            pg.draw.rect(screen, color, rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
