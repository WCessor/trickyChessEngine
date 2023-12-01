import pygame
import chess
from pygame.locals import *
from frontend.handleButton import handleButton
from frontend.makeButton import makeButton
def displayBoard(board,turn):
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    clock = pygame.time.Clock()

    square_size = 60  # Adjust the square size as needed
    colors = [(255, 206, 158), (209, 139, 71)]  # Light and dark square colors

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        turn = handleButton(event, turn,480,0,120,60)
        
        screen.fill((128, 128, 128))  # Fill the screen with black background

        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                square_color = colors[(row + col) % 2]
                pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))

        # Draw pieces on the board
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                if piece.color == chess.WHITE:
                    piece_image = pygame.image.load(f"frontend/images/white_{piece.symbol()}.png")
                else:
                    piece_image = pygame.image.load(f"frontend/images/black_{piece.symbol()}.png")
                screen.blit(piece_image, (chess.square_file(square) * square_size, (7 - chess.square_rank(square)) * square_size))
        makeButton(screen,480,0,120,60,turn)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
