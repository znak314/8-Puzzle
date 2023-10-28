from puzzle import Puzzle

class LDS_Node:
    def __init__(self, puzzle, parent=None, action="Start"):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent):
            self.depth = parent.depth + 1
        else:
            self.depth = 0

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

    @property
    def state(self):
        return str(self)

    def __str__(self):
        return str(self.puzzle)