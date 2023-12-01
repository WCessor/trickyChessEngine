import pygame
from pygame.locals import *

turn_changed = False  # Initialize a toggle variable

def handleButton(event, turn, x, y, width, height):
    global turn_changed

    if event.type == MOUSEBUTTONUP and event.button == 1:
        if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height and not turn_changed:
            turn = not turn
            turn_changed = True  # Set the toggle to True to prevent further turn changes

    elif event.type == MOUSEBUTTONDOWN:
        turn_changed = False  # Reset the toggle when the mouse button is down

    return turn


