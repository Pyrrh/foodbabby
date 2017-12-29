
class Utilities:

    def validate_selection(self, num):

        if num.isalpha() or int(num) < 1 or int(num) > 6:
            return False
        else:
            return True
