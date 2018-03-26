
class Utilities:

    @staticmethod
    def validate_selection(num):

        if num.isalpha() or int(num) < 1 or int(num) > 6:
            print("Invalid option. Please choose a number from the menu\n")
            return False
        else:
            return True

    def print_main_menu(self):

        is_valid = False

        print("MAIN MENU\n\n")
        print("Select an option: \n")

        print("""
            1. Add a recipe
            2. Find a recipe (NOT IMPLEMENTED)
            3. Display a recipe (NOT IMPLEMENTED)
            4. Delete a recipe (NOT IMPLEMENTED)
            5. Build a shopping list (NOT IMPLEMENTED)
            6. Save and Quit (LOAD FROM FILE NOT IMPLEMENTED)

            """)

        selection = input()
        while not is_valid:
            is_valid = Utilities.validate_selection(selection)
        return selection
