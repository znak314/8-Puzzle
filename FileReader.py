

class FileReader:
    def __init__(self,filename):
        self.filename = filename

    def read_puzzle_from_file(self):
        puzzle = []
        with open(self.filename, 'r') as file:
            for line in file:
                row = [int(num) for num in line.split(' ')]
                puzzle.append(row)
        return puzzle
