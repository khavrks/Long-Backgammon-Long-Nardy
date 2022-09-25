from re import S
import pygame
import neat
import random
import sys

from player import Player
from board import Board
from pawn import Pawn

pygame.font.init()

GAME_SCREEN_WIDTH = 640
GAME_SCREEN_HEIGHT = 480
STAT_FONT = pygame.font.SysFont('arial', 25)
NUM_FONT = pygame.font.SysFont('arial', 17)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN_left_hand = (0, 255, 102)
PURPLE_right_hand = (255, 0, 205)
YELLOW_left_leg = (255, 239, 0)
SEA_right_leg = (0, 222, 255)
FPS = 60
VEL = 1


POS_1 = [465, 68]
POS_2 = [431, 68]
POS_3 = [397, 68]
POS_4 = [363, 68]
POS_5 = [329, 68]
POS_6 = [295, 68]
POS_7 = [238, 68]
POS_8 = [204, 68]
POS_9 = [170, 68]
POS_10 = [136, 68]
POS_11 = [102, 68]
POS_12 = [68, 68]
POS_13 = [68, 409]
POS_14 = [102, 409]
POS_15 = [136, 409]
POS_16 = [170, 409]
POS_17 = [204, 409]
POS_18 = [238, 409]
POS_19 = [295, 409]
POS_20 = [329, 409]
POS_21 = [363, 409]
POS_22 = [397, 409]
POS_23 = [431, 409]
POS_24 = [465, 409]

list_to_pos_pawns = { 0: POS_1, 1: POS_2, 2: POS_3, 3: POS_4, 4: POS_5, 5: POS_6, 6: POS_7, 7: POS_8, 8: POS_9, 9: POS_10, 10: POS_11, 11: POS_12, 12: POS_13, 13: POS_14, 14: POS_15, 15: POS_16, 16: POS_17,  17: POS_18, 18: POS_19, 19: POS_20, 20: POS_21, 21: POS_22, 22: POS_23, 23: POS_24
}


class Game:

    def __init__(self) -> None:
        self.white = Player("w", 1, [0, 15])
        self.black = Player("b", 2, [12, 15])
        self.board = Board()
        self.board.doska[0] = [self.white.color, self.white.pawns]
        self.board.doska[12] = [self.black.color, self.black.pawns]
        self.turn = self.white.color
        self.your_turn = False
        self.win = False
        self.kost1 = ""
        self.kost2 = ""
        self.save_kosty = False
        self.from_ = ""
        self.to_ = ""
        self.new_turn = True

    def run(self, run: bool):
       ...
    
    def draw_b(self):
        ...

    def draw(self, genome1, genome2):
       ...

    def _cheack_the_board_b(self, board: Board):
        ...

    def _cheack_the_board(self, board: Board, genome1, genome2):
        ...

    def MakeMove(self, tworandnumbers: list, player: Player, board: Board, pawn: Pawn):
        ...

    def _getRandom2Numbers(self):
        ...

    def _sort_kosty(self, k1, k2):
       ...

    def _allowedMove(self, tworandnumbers: list, player: Player, board: Board, pawn: Pawn):
        """
        pawn = [0, "black"]
        place on the board, color
        """
        ...

    def _allAllowedMoves(self, tworandnumbers: list, player: Player, board: Board):
       ...

    def _ReturnSteps(self, pawn: Pawn):
        ...

    def _checkifplayerisinhouse(self, player: Player, board: Board):
        ...

    def _makeADecision(self, net, allowed_moves: list, tworandnumbers: list):
        ...

    def _makeADecisionReturnOut(self, net, allowed_moves: list, tworandnumbers: list):
        ...

    def _desideMove(self, allowed_moves: list, decdion):
       ...

    def _getBestMoves(self, out: list):
        ...

    def play(self, genome1, genome2, config):
        ...

    def _pygame_cheack_the_board(self, board: Board):
       ...

    def _your_turn_advice(self):
        ...

    def _draw_all_pawns(self, pawns: list):
        ...

    def _check_if_active(self, active, rect):
        ...

    def _draw_any_text(self, text, x, y):
        ...

    def _see_whos_turn_in_the_begining(self, you):
       ...

    def _draw_kosty_you_have(self, kosty):
        ...

    def _enum_board_pawns(self):
        ...

    def _change_turn(self, kosty, you):
        ...
        
    def pygame_play(self, you, SCREEN, CLOCK, IMG): #gen, config
        ...

    def pygame_play_AI_helper(self, you, SCREEN, CLOCK, IMG, gen, config):
        ...

from screen import GameScreen
from board_pygame import Board_Game
from pawn_draw import PawnDraw
from pygame_func import newTextBox
import pickle, os

pygame.init()

def eval_genomes(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = Game()
            game.play(genome1, genome2, config)

def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1012')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10))
    winner = p.run(eval_genomes, 100000000)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)
    print("done")

def run_game(config):
    game = Game()
    with open("best.pickle", "rb") as f:
        gen = pickle.load(f)
    game.pygame_play_AI_helper("w", SCREEN, CLOCK, IMG_BOARD, gen, config)
    

pygame.display.set_caption("Нарды")
pygame.display.set_icon(pygame.image.load("backgammongame_backgammo_6195.ico"))
SCREEN = pygame.display.set_mode((840, 480), vsync=1)
CLOCK = pygame.time.Clock()
IMG_BOARD = pygame.image.load('nardi_board.png')
game = Game()


local_dir = os.path.dirname(__file__)
config_file = os.path.join(local_dir, "config.txt")
config_neat = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     config_file)
    
run_game(config_neat)
# game.pygame_play_AI_helper("w", SCREEN, CLOCK, IMG_BOARD)
# game.play(genome1, genome2, config)
