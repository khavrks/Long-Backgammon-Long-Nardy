

class Board:
    def __init__(self) -> None:
        self.doska = [['', 0] for i in range(24)]

    def setPawn(self, player, number):
        ...

    def removePawn(self, player, number):
        ...

    def checkIfCanMakeMove(self, player, number):
        ...

