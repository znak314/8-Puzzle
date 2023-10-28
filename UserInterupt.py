class UserInteraption:
    @staticmethod
    def get_yes_or_no_input(message):
        while True:
            user_input = input(message).strip().lower()
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            else:
                print("Please, enter y or n\n")

    @staticmethod
    def get_binary_input(message):
        while True:
            user_input = input(message).strip()
            if user_input in ['0', '1']:
                return int(user_input)
            else:
                print("Please, enter 0 or 1.")

    @staticmethod
    def get_user_limitation():
        while True:
            try:
                lim = int(input("Enter number beetwen 1 and 31: "))
                if 1 <= lim <= 31:
                    return lim
                else:
                    print("Number is out of range, try again")
            except ValueError:
                print("Not a number, try again")