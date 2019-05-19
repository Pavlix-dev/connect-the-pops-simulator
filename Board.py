from Tree import Tree
from Node import Node
import random


class Board:
    board_size = 0
    board = []

    def __init__(self, board_size):
        self.board_size = board_size

        for i in range(board_size):
            self.board.insert(i, [])
            for j in range(board_size):
                self.board[i].append(random.randint(1, 6))

    def print(self):
        cell_size = 4  # even numbers only

        for line in self.board:
            print('\n' + ('-' * cell_size + '-') * self.board_size + '-')

            for element in line:
                element_str = str(2 ** element)
                left_spaces = ' ' * ((cell_size - len(element_str)) // 2)
                right_spaces = ' ' * (((cell_size - len(element_str)) // 2) + len(element_str) % 2)
                print('|' + left_spaces + element_str + right_spaces, end='')

            print('|', end='')

        print('\n' + ('-' * cell_size + '-') * self.board_size + '-')

    def find_best_path_for_cell(self, x, y):
        tree = Tree()

        tree.value = self.board[x][y]
        tree.root = self.add_node(tree, x, y)

        print(tree.get_longest_path_length())
        print(tree.longestPath)

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
