from pygame import display, image

class Screen:
    def __init__(self, size):
        self.screen = display
        self.size = size

    @property
    def set_screen(self):
        return self.screen.set_mode((self.size, self.size))

    def set_name(self, title):
        return self.screen.set_caption(f"{title}")

    def set_picture(self, path='pictures/pn.png'):
        return self.screen.set_icon(image.load(f"{path}"))
