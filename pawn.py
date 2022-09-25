
class Pawn:
    def __init__(self, color, from_, to_) -> None:
        self.from_ = from_
        self.to_ = to_
        self.color = color

    def setFromToColor(self, from_, to_, color):
        ...
