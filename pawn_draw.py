import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 102)
RED = (255, 0, 0)


class PawnDraw:
    def __init__(self, screen, color, arr, amount):
        self.screen = screen
        self.color = color
        self.x = arr[0]
        self.y = arr[1]
        self.width = 30
        self.height = 30
        self.selected = False
        self.amount = amount
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, FONT):
        ...

    def move(self):
        ...
