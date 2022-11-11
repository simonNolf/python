from .usefull_functions import *


class Items:
    def __init__(self):
        self.size = get_data("size")
        self.squares = get_data("square_line")
        self.color_index = 0
        self.pawn_color = get_data("pawn_color")

    def draw(self, canvas, position="top", spacex=5, spacey=5):
        sum_value = self.size / self.squares
        for j in range(self.squares):  # Will browse line per line
            if 0 <= j <= 2:
                self.color_index = 0
            else:
                self.color_index = 1
            for i in range(self.squares):  # Will browse all squares of the j line
                if 0 <= j <= 2 or int(self.squares) - 3 <= j <= self.squares:
                    if j % 2 == 0:  # Allow to know which lines start with a black square
                        if i % 2 == 0:  # Help to fill 1 bloc on two with 1 square of space
                            canvas.create_oval(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j,
                                               fill=self.pawn_color[self.color_index])
                    else:
                        if i % 2 == 1:
                            canvas.create_oval(i * sum_value, (sum_value * (j + 1)), (i + 1) * sum_value, sum_value * j,
                                               fill=self.pawn_color[self.color_index])
        canvas.pack(side=position, padx=spacex, pady=spacey)
