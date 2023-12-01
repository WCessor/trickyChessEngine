import chess
import chess.engine

def get_top_moves(board):
    with chess.engine.SimpleEngine.popen_uci(r"C:\Users\sonny\Downloads\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern.exe") as engine:
        result = engine.play(board, chess.engine.Limit(time=0.1))
        print(result.info)
        return result.info.get('pv', [])[:5]




