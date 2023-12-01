import chess
from pygame.locals import *
def getSquare(x, y,square_size):
    file = x // square_size
    rank = 7 - (y // square_size)  # Invert for correct chess board orientation
    return chess.square(file, rank)