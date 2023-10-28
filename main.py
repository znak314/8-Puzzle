import time

from puzzle import Puzzle
from Solver import AStar_Solver
from Solver import LDS_Solver
from UserInterupt import UserInteraption
from FileReader import FileReader
from Validator import MyCustomException
from Validator import Validator


try:
    ReadFile = UserInteraption.get_yes_or_no_input("Read from file? (y/n): ")
    if ReadFile:
        fileName = input("Enter name of the file: ")
        Validator.is_file_exist(fileName)
        file = FileReader(fileName)

        Validator.is_correct_file_format(fileName)
        board = file.read_puzzle_from_file()
    else:
        #board = [[2, 1, 3], [4, 5, 6], [7, 8, 0]]  # no solution
        #board = [[4, 3, 1], [5, 0, 8], [7, 6, 2]]
        board = [[1, 2, 3],[ 4, 5, 0], [6, 7, 8]]

    puzzle = Puzzle(board)
    print("\n0 - LDS (Limited depth search)\n1 - A* (Manhattan distance)\n")
    inform_algo = UserInteraption.get_binary_input("Choose algorithm: ")

    if inform_algo:
        #    A*
        ast_start = time.perf_counter()
        sol = AStar_Solver(puzzle)
        path = sol.solve()
        ast_end = time.perf_counter()
        solving_time = ast_end - ast_start
    else:
        #    LDS
        limit = UserInteraption.get_user_limitation()
        lds_start = time.perf_counter()
        sol = LDS_Solver(puzzle)
        path = sol.solve(limit)
        lds_end = time.perf_counter()
        solving_time = lds_end - lds_start

    # If there is no solution in this depth / at all
    if path is None:
        print("There is no solution for this puzzle", end=" ")
        if not inform_algo:
            print("in this depth")

    # If time or memory limit was exceeded
    if not path:
        print("The time or memory limit was exceeded")

    # If path is finded
    if path:
        steps = 0
        for node in path:
            print(node.action)
            node.puzzle.pprint()
            steps += 1
        print("Total number of steps: " + str(steps - 1))

    # print statics
    print("Total amount of time in search: " + str(solving_time) + " second(s)")
    print("Max amount of nodes saved at once: " + str(sol.max_nodes_saved))
    print("Number of generated states: " + str(sol.generated_states))

except MyCustomException as e:
    print(f"Error occurs: {e}")

