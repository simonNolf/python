from tkinter import Tk


class Window:
    def __init__(self, config_file="config.json"):
        pass

    @property
    def create(self):
        return Tk()

    def rename(self, window, sentence):
        return window.title(sentence)
