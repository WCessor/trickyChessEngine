import chess
def printLegalMoves(board):
    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        print(move)