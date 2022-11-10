from tkinter import Canvas
from functions import get_data

class Checkboard:
    def __init__(self):
        self.size = get_data("size")
        self.squares = get_data("square_line")
        self.color = [get_data("color"), get_data("color2")]
    
    def create(self, window, theme="ivory"):
        return Canvas(window, width=self.size, height=self.size, bg=theme)

    def draw(self, canvas, position="top", spacex=0, spacey=0):
        sum_value = self.size / self.squares
        for j in range(self.squares): #Will browse line per line
            for i in range(self.squares): #Will browse all squares of the j line
                if j % 2 == 0: #Allow to know which lines start with a black square
                    if i % 2 == 0: #Help to fill 1 bloc on two with 1 square of space
                        canvas.create_rectangle(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j, fill=self.color[0])
                    else:
                        canvas.create_rectangle(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j, fill=self.color[1])
                else:
                    if i % 2 == 1:
                        canvas.create_rectangle(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j, fill=self.color[0])
                    else:
                        canvas.create_rectangle(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j, fill=self.color[1])
        canvas.pack(side=position, padx=spacex, pady=spacey)