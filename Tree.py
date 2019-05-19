class Tree:
    root = None

    value = 0
    longestPath = []

    def get_longest_path_length(self):
        return len(self.longestPath) - 1
