class Pawn:
    def __init__(self, pawn, data):
        self.pawn = pawn
        self.data = data
        self.size = self.data["size"] // self.data["square"]

    def bas(self, mouse_pos):
        return mouse_pos[0], mouse_pos[1] + self.size