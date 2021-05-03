# imports all functions for testing (includes chess
from evalFuncs import *

import chess.pgn
import datetime
import chess.uci

engine = chess.uci.popen_engine("./stockfish.exe")
engine.uci()
# engine.name

movehistory = []
game = chess.pgn.Game()
game.headers["Event"] = "Depth ___"
game.headers["Site"] = "local"
game.headers["Date"] = str(datetime.datetime.now().date())
game.headers["Round"] = 1
game.headers["White"] = "AlphaBeta and quiescence"
game.headers["Black"] = "Stockfish12"
board = chess.Board()
boardvalue = init_evaluate_board(board)

while not board.is_game_over(claim_draw=True):
    if board.turn:
        move = selectmove(5, board)
        board.push(move)
    else:
        engine.position(board)
        move = engine.go(movetime=1000).bestmove
        movehistory.append(move)
        board.push(move)

game.add_line(movehistory)
game.headers["Result"] = str(board.result(claim_draw=True))
print(game)
print(game, file=open("test_d3.pgn", "w"), end="\n\n")

# SVG(chess.svg.board(board=board, size=400))