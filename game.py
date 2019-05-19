from Board import Board

BOARD_SIZE = 5

board = Board(BOARD_SIZE)

board.find_best_path_for_cell(0, 0)

board.print()
