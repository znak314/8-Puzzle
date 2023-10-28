from puzzle import Puzzle

class AStar_Node:
    def __init__(self, puzzle, parent=None, action="Start"):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent):
            self.g = parent.g + 1
        else:
            self.g = 0

    # get path from start state to goal state
    @property
    def path(self):
        cur_node, parents = self, []
        while cur_node:
            parents.append(cur_node)
            cur_node = cur_node.parent
        yield from reversed(parents)

    # check if current state is the goal state
    @property
    def is_solved(self):
        return self.puzzle.is_solved

    # get child stated
    @property
    def actions(self):
        return self.puzzle.actions

    # heuristic function
    @property
    def h(self):
        return self.puzzle.manhattan_dist


    @property
    def f(self):
        return self.h + self.g

    @property
    def state(self):
        return str(self)

    def __str__(self):
        return str(self.puzzle)