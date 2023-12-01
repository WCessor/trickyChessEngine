import chess.engine
import chess
from backend.printLegalMoves import printLegalMoves  # Importing the function from the printLegalMoves module
from frontend.displayBoard import displayBoard
if __name__ == "__main__":
    board = chess.Board()
    printLegalMoves(board)
    turn = chess.WHITE
    displayBoard(board,turn)