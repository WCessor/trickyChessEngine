import pygame
import chess
from pygame.locals import *
from backend.printLegalMoves import printLegalMoves
from frontend.getSquare import getSquare
from frontend.makeButton import makeButton
def displayBoard(board,turn):
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    clock = pygame.time.Clock()

    square_size = 60  # Adjust the square size as needed
    colors = [(255, 206, 158), (209, 139, 71)]  # Light and dark square colors
    selected_square = None  # Initialize selected_square variable
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Closing Game...")
                running = False
            if event.type == MOUSEBUTTONDOWN:
                # Get the square from mouse coordinates
                x, y = pygame.mouse.get_pos()
                print(x,y)
                if event.button == 1 and (0<x<480 and 0<y<480):  #Left mouse button
                    square = getSquare(x, y,square_size)
                    print(square)
                    if selected_square is None:
                        # Select the piece to move
                        selected_square = square if board.piece_at(square) and board.piece_at(square).color == turn else None
                        print("White" if turn else "Black")
                    else:
                        # Move the piece
                        move = chess.Move(selected_square, square)
                        print(move)
                        if move in board.legal_moves:
                            print(move," is a Legal move")
                            board.push(move)
                            turn = not turn
                            print("White" if turn else "Black")
                        else:
                            print("Illegal move")
                            print("Legal moves are as follows:")
                            printLegalMoves(board)
                        selected_square = None
                elif event.button == 1 and 480 <= x <= 600 and 0 <= y <= 60:  # Button click
                    move = chess.Move.null()
                    board.push(move)
                    turn = not turn
                    print("Change turn button clicked")
                    print("White" if turn else "Black")
                    #selected_square = None
                else:
                    print("something else happened")
        
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
