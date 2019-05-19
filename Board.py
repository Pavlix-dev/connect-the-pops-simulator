from Tree import Tree
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
        cellSize = 4  # even numbers only

        for line in self.board:
            print('\n' + ('-' * cellSize + '-') * self.boardSize + '-')

            for element in line:
                elementStr = str(2 ** element)
                leftSpaces = ' ' * ((cellSize - len(elementStr)) // 2)
                rightSpaces = ' ' * (((cellSize - len(elementStr)) // 2) + len(elementStr) % 2)
                print('|' + leftSpaces + elementStr + rightSpaces, end='')

            print('|', end='')

        print('\n' + ('-' * cellSize + '-') * self.boardSize + '-')

    def findBestPathForCell(self, cell):
        tree = Tree()

        self.addNodes(tree, self.board[cell[0]][cell[1]], cell)

    def addNodes(self, tree, value, address):
        currentValue = self.board[address[0]][address[1]]

        if not 0 <= address[0] < self.boardSize:
            return None
        if not 0 <= address[1] < self.boardSize:
            return None

        if currentValue is not value:
            return None

        tree.value = currentValue
        tree.address = address

        tree.top = self.addNodes()
