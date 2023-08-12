import pygame as pg


class Screen:
    def __init__(self):
        """
        Set la longueur et la largeur de la fenêtre ainsi que l'écran en instance pygame
        """
        self.__screen = pg.display
        self.__width = 800
        self.__height = 950

    @property
    def screen(self):
        """

        :return: renvoie le screen
        """
        return self.__screen

    @property
    def width(self):
        """

        :return: renvoie la valeur de width
        """
        return self.__width

    @property
    def height(self):
        """

        :return: renvoie la valeur de height
        """
        return self.__height

    def set_name(self, title):
        """

        :param title : titre de la fenêtre
        : return : met le titre à la fenêtre pygame
        """
        if type(title) != type('test'):
            raise TypeError
        return self.screen.set_caption(f"{title}")
