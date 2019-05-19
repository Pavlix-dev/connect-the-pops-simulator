import random


class Board:
    boardSize = 0
    board = []

    def __init__(self, boardSize):
        self.boardSize = boardSize

        for i in range(boardSize):
            self.board.insert(i, [])
            for j in range(boardSize):
                self.board[i].append(random.randint(1, 6))

    def print(self):
        cellSize = 4  #even numbers only

        for line in self.board:
            print('\n' + ('-'*cellSize + '-') * self.boardSize + '-')

            for element in line:
                elementStr = str(2**element)
                leftSpaces = ' '*((cellSize-len(elementStr))//2)
                rightSpaces = ' '*(((cellSize-len(elementStr))//2)+len(elementStr) % 2)
                print('|' + leftSpaces + elementStr + rightSpaces, end='')

            print('|', end='')

        print('\n' + ('-'*cellSize + '-') * self.boardSize + '-')
