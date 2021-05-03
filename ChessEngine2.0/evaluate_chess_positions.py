
# imports all functions for testing (includes chess
from evalFuncs import *

# imports all test positions
from test_positions import *

all_tests = BK_test + sbd_test
all_sols = BK_sols + sbd_sols


depth = 4
solved = 0
for i, pos in enumerate(all_tests):
    movehistory = []
    board = chess.Board()
    board.set_epd(pos)
    boardvalue = init_evaluate_board(board)

    mov = selectmove(depth, board)
    movehistory.append(mov)

    print("Test Position problem " + str(i+1) + " " + board.san(mov) + " / Solution: " + all_sols[i])

    if str(board.san(mov)) in str(all_sols[i]) or str(all_sols[i]) in str(board.san(mov)):
        solved = solved + 1
        print("Correct")
    else:
        print("Incorrect")

print("Number of correct solved: " + str(solved))

