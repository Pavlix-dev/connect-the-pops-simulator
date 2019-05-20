from Tree import Tree
from Node import Node
import random
import math
from copy import deepcopy


class Board:
    board_size = 0
    board = []

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []

        for i in range(board_size):
            self.board.insert(i, [])
            for j in range(board_size):
                self.board[i].append(random.randint(1, 6))

    def print(self):
        cell_size = 6  # even numbers only

        for j in range(self.board_size):
            print('\n' + ('-' * cell_size + '-') * self.board_size + '-')

            for i in range(self.board_size):
                element_str = str(2 ** self.board[i][j])
                left_spaces = ' ' * ((cell_size - len(element_str)) // 2)
                right_spaces = ' ' * (((cell_size - len(element_str)) // 2) + len(element_str) % 2)
                print('|' + left_spaces + element_str + right_spaces, end='')

            print('|', end='')

        print('\n' + ('-' * cell_size + '-') * self.board_size + '-')

    def find_best_path(self):
        board_longest_path = []

        for i in range(self.board_size):
            for j in range(self.board_size):
                element_longest_path = self.find_best_path_for_cell(i, j)
                if len(element_longest_path) > len(board_longest_path):
                    board_longest_path = element_longest_path.copy()

        return board_longest_path

    def make_move(self):
        path = self.find_best_path()

        if len(path) <= 1:
            return False

        print(path)

        position = path.pop()
        self.board[position[0]][position[1]] += math.floor(math.log(len(path)+1, 2))

        for cell in path:
            row = cell[0]
            while row > 0:
                self.board[cell[0]][row] = self.board[cell[0]][row-1]
                row -= 1
            self.board[cell[0]][0] = random.randint(1, 6)

        self.print()

        return True

    def find_best_path_for_cell(self, x, y):
        tree = Tree()

        tree.value = self.board[x][y]
        tree.root = self.add_node(tree, x, y)

        return tree.longestPath

    def add_node(self, tree, x, y, parent=None):
        if not 0 <= x < self.board_size:
            return None
        if not 0 <= y < self.board_size:
            return None

        if self.board[x][y] is not tree.value:
            return None

        node = Node()

        if parent is not None:
            if (x, y) in parent.path:
                return None

            node.path = parent.path.copy()

        node.path.append((x, y))

        if len(tree.longestPath) == len(node.path):
            if tree.longestPath[-1][1] < node.path[-1][1]:
                tree.longestPath = node.path

        if len(tree.longestPath) < len(node.path):
            tree.longestPath = node.path

        node.top = self.add_node(tree, x, y-1, node)
        node.bottom = self.add_node(tree, x, y+1, node)
        node.left = self.add_node(tree, x-1, y, node)
        node.right = self.add_node(tree, x+1, y, node)

        node.leftTop = self.add_node(tree, x-1, y-1, node)
        node.leftBottom = self.add_node(tree, x-1, y+1, node)
        node.rightTop = self.add_node(tree, x+1, y-1, node)
        node.rightBottom = self.add_node(tree, x+1, y+1, node)

        return node

    def make_wise_move(self):
        origin_board = list(map(list, self.board))

        best_path = []
        best_path_value = 0

        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board = list(map(list, origin_board))
                path = self.find_best_path_for_cell(i, j)

                self.board[i][j] += math.floor(math.log(len(path) + 1, 2))

                for cell in path:
                    row = cell[0]
                    while row > 0:
                        self.board[i][row] = self.board[i][row - 1]
                        row -= 1
                    self.board[i][0] = random.randint(1, 6)

                path_value = self.get_value_of_board()

                if len(path) > 1:
                    if path_value > best_path_value:
                        best_path_value = path_value
                        best_path = path.copy()

        self.board = list(map(list, origin_board))

        print(best_path)
        if len(best_path) <= 1:
            return False

        position = best_path.pop()
        self.board[position[0]][position[1]] += math.floor(math.log(len(best_path) + 1, 2))

        for cell in best_path:
            row = cell[0]
            while row > 0:
                self.board[cell[0]][row] = self.board[cell[0]][row - 1]
                row -= 1
            self.board[cell[0]][0] = random.randint(1, 6)

        self.print()

        return True

    def get_value_of_board(self):
        value = 0

        for i in range(self.board_size):
            for j in range(self.board_size):
                if len(self.find_best_path_for_cell(i, j)) > 1:
                    value += 1

        return value
