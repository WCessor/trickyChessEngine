import pygame
import chess
from pygame.locals import *

def makeButton(screen, x, y, width, height,turn):
    
    font = pygame.font.Font(None, 24)
    if (turn == chess.WHITE):
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
        text_string = "Switch to black"
        text = font.render(text_string, True, (0, 0, 0))
    else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
        text_string = "Switch to white"
        text = font.render(text_string, True, (255, 255, 255))
    
    text_width, text_height = font.size(text_string)
    screen.blit(text, (x + (width // 2) - (text_width // 2), y + (height // 2) - (text_height // 2)))
