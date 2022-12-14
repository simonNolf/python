import pygame as pg

class Screen:
    def __init__(self):
        self.__screen = pg.display
        self.__width = 800
        self.__height = 950

    @property
    def screen(self):
        return self.__screen
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def set_screen(self):
        self.screen.set_mode((self.width, self.height))

    def set_name(self, title):
        return self.screen.set_caption(f"{title}")

    def set_picture(self, path='pictures/pn.png'):
        return self.screen.set_icon(pg.image.load(f"{path}"))

