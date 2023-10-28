import random
import itertools

class Puzzle:
    def __init__(self, board):
        self.size = len(board[0])
        self.board = board

    # create a list of possible moves
    @property
    def actions(self):

        def create_move(at, to):
            return lambda: self._move(at, to)

        result = []
        for i in range(self.size):
            for j in range(self.size):

                directions = {
                    "UP ↑": (i - 1, j),
                    "RIGHT →": (i, j + 1),
                    "DOWN ↓": (i + 1, j),
                    "LEFT ←": (i, j - 1)
                }

                for action, (i2, j2) in directions.items():
                    if i2 >= 0 and j2 >= 0 and i2 < self.size and j2 < self.size and self.board[i2][j2] == 0:
                        move = create_move((i,j), (i2,j2)), action
                        result.append(move)
        return result

    # check if current state is the goal state
    @property
    def is_solved(self):
        return str(self) == "123456780"


    # heuristic function
    @property
    def manhattan_dist(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance


    def copy_board(self):
        board = []
        for row in self.board:
            board.append([k for k in row])
        return Puzzle(board)


    # create a new state, where 'at' and 'to' have been swapped
    def _move(self, at, to):
        copy = self.copy_board()
        i, j = at
        i2, j2 = to
        copy.board[i][j], copy.board[i2][j2] = copy.board[i2][j2], copy.board[i][j]
        return copy

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row