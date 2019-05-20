from Board import Board

BOARD_SIZE = 5

board = Board(BOARD_SIZE)

while board.make_move():
    pass


# stats = [0] * 25
#
# for i in range(10000):
#     board.__init__(BOARD_SIZE)
#     stats[len(board.find_best_path())-1] += 1
#
# for i in range(25):
#     print(str(i) + ': ', end='')
#     print('-'*(stats[i]//20))

