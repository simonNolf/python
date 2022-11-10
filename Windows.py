from tkinter import Tk

class Window:
    @property
    def create(self):
        return Tk()

    def rename(self, window, sentence):
        return window.title(sentence)