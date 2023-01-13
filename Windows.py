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

    def set_name(self, title):
        return self.screen.set_caption(f"{title}")


