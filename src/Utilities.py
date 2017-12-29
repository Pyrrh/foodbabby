
class Utilities:

    def validate_selection(self, num):

        if num.isalpha() or int(num) < 1 or int(num) > 6:
            print("Invalid option. Please choose a number from the menu\n")
            return False
        else:
            return True
