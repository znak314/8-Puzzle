from AStar import AStar_Node
from LDS import LDS_Node
import time

MAX_PROCESS_TIME = 10 # 30 * 60  # Program time  Execution Limitations
MAX_PROCESS_Memory = 256 * 1024  # 10 Mb memory  Execution Limitations

class AStar_Solver:
    def __init__(self, start_puzzle):
        self.start_puzzle = start_puzzle
        self.generated_states = 0
        self.max_nodes_saved = 0

    def solve(self):
        queue = []
        visited = set()
        queue.append(AStar_Node(self.start_puzzle))
        visited.add(AStar_Node(self.start_puzzle))

        start_time = time.time()
        end_time = start_time + MAX_PROCESS_TIME

        while queue:
            queue = sorted(queue, key=lambda node: node.f)
            node = queue.pop(0)
            if node.is_solved:
                return node.path

            if len(queue) > self.max_nodes_saved:
                self.max_nodes_saved = len(queue)

            for move, action in node.actions:
                child = AStar_Node(move(), node, action)
                self.generated_states += 1
                if child.state not in visited:
                    queue.append(child)
                    visited.add(child.state)

            # time limit was exceeded
            if time.time() > end_time or (len(queue) + len(visited)) > MAX_PROCESS_Memory:
                return False

        # if there is no solution
        return None




class LDS_Solver:
    def __init__(self, start_puzzle):
        self.start_puzzle = start_puzzle
        self.generated_states = 0
        self.max_nodes_saved = 0

    def solve(self, limit):
        stack = []
        start_time = time.time()
        end_time = start_time + MAX_PROCESS_TIME

        stack.append(LDS_Node(self.start_puzzle))

        while stack:
            cur_node = stack.pop()
            if cur_node.is_solved:
                return cur_node.path

            if len(stack) > self.max_nodes_saved:
                self.max_nodes_saved = len(stack)

            if cur_node.depth < limit:
                for move, action in cur_node.actions:
                    child = LDS_Node(move(), cur_node, action)
                    stack.append(child)
                    self.generated_states += 1

            # time limit was exceeded
            if time.time() > end_time or len(stack) > MAX_PROCESS_Memory:
                return False

        # if there is no solution
        return None


