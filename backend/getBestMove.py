import chess
import chess.engine

def get_top_move(board):
    with chess.engine.SimpleEngine.popen_uci(r"C:\Users\sonny\Downloads\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern.exe") as engine:
        result = engine.analyse(board, chess.engine.Limit(time = 1))
        return result