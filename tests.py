import unittest
import time
import inspect

from Validator import Validator
from Validator import MyCustomException
from AStar import AStar_Node
from LDS import LDS_Node
from Solver import AStar_Solver
from Solver import LDS_Solver
from puzzle import Puzzle

class MyTestCase(unittest.TestCase):
    def test_file_not_exist(self):
        some_file = "not_existed"
        with self.assertRaises(MyCustomException):
            Validator.is_file_exist(some_file)
        print("✔ - Non existing-file test passed")

    def test_invalid_file_format(self):
        invalid_file = "invalid_format"
        with self.assertRaises(MyCustomException):
            Validator.is_correct_file_format(invalid_file)
        print("✔ - Invalid file-format test passed")

    def test_limit_exceeded_AStar(self):
        board = [[2, 1, 3], [4, 5, 6], [7, 8, 0]]  # no solution
        puzzle = Puzzle(board)
        sol = AStar_Solver(puzzle)
        path = sol.solve()
        self.assertEqual(path,False)
        print("✔ - Time or memory limit exceed in A* test passed")

    def test_limit_exceeded_LDS(self):
        board = [[1, 2, 3],[ 4, 5, 0], [6, 7, 8]]
        puzzle = Puzzle(board)
        sol = LDS_Solver(puzzle)
        path = sol.solve(5)
        self.assertEqual(path, None)
        print("✔ - No solution in depth limit in LDS test passed")

    def test_no_solution_in_depth_LDS(self):
        board = [[2, 1, 3], [4, 5, 6], [7, 8, 0]]  # no solution
        puzzle = Puzzle(board)
        sol = LDS_Solver(puzzle)
        path = sol.solve(31)
        self.assertEqual(path, False)
        print("✔ - No solution  in LDS test passed")

    def test_find_solution_in_depth_LDS(self):
        board = [[1, 2, 3],[ 4, 5, 0], [6, 7, 8]]
        puzzle = Puzzle(board)
        sol = LDS_Solver(puzzle)
        path = sol.solve(15)
        self.assertTrue(inspect.isgenerator(path))
        print("✔ - Solution finded in depth limit  in LDS test passed")

    def test_find_solution_in_AStar(self):
        board = [[1, 2, 3],[ 4, 5, 0], [6, 7, 8]]
        puzzle = Puzzle(board)
        sol = AStar_Solver(puzzle)
        path = sol.solve()
        self.assertTrue(inspect.isgenerator(path))
        print("✔ - Solution finded  in A* test passed")

if __name__ == '__main__':
    unittest.main()
