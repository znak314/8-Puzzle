import os

class MyCustomException(Exception):
    pass


class Validator:
    @staticmethod
    def is_file_exist(filename):
        if not os.path.isfile(filename):
            raise MyCustomException("There is no files with this name in program's directory")

    @staticmethod
    def is_correct_file_format(filename):
        with open(filename, 'r') as file:
            content = file.read().strip()
            numbers = content.split()
            if len(numbers) == 9:
                for number in numbers:
                    try:
                        float(number)
                    except ValueError:
                        raise MyCustomException("Invalid file format")
            else:
                raise MyCustomException("Invalid file format")