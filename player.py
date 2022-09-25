
class Player:
    def __init__(self, color, number, position):
        self.color = color
        self.number = number
        self.pawns = 15
        self.pawnsposition = [position]
        self.tookfromhead = False
        self.first_turn = True
        self.in_house = False
        self.you = False
