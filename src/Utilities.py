
class Utilities:

    @staticmethod
    def validate_menu_selection(num):

        if num.isalpha() or int(num) < 1 or int(num) > 6:
            print("""Invalid option. Please choose a number (1-6) from the menu: 
            1. Add a recipe (NOT IMPLEMENTED)
            2. Find a recipe (NOT IMPLEMENTED)
            3. Display a recipe (NOT IMPLEMENTED)
            4. Delete a recipe (NOT IMPLEMENTED)
            5. Build a shopping list (NOT IMPLEMENTED)
            6. Save and Quit (LOAD FROM FILE NOT IMPLEMENTED)
            """)
            return False
        else:
            return True

    def print_main_menu(self):

        is_valid = False

        print("\nMAIN MENU\n\n")
        print("Select an option: \n")

        print("""
            1. Add a recipe
            2. Find a recipe (NOT IMPLEMENTED)
            3. Display a recipe
            4. Delete a recipe (NOT IMPLEMENTED)
            5. Build a shopping list (NOT IMPLEMENTED)
            6. Save and Quit (LOAD FROM FILE NOT IMPLEMENTED)

            """)

        selection = input()
        while not is_valid:
            is_valid = Utilities.validate_menu_selection(selection)
            if not is_valid:
                selection = input()
        return selection

    def again(self):
        print("Okay, what's next?\n")
        return Utilities.print_main_menu(self)

    @staticmethod
    def recipe_to_dict(cookbook):
        cookbook_dict = {'recipes': []}

        # iterate and add each recipe to the dictionary
        for r in cookbook.recipes:
            cookbook_dict['recipes'].append(r.recipe_to_dict())
        return cookbook_dict

    def ask_load_from_file(self):
        # is_valid = False
        response = input("Do you wish to load a cookbook? y/n")
        if Utilities.validate_yes_no(self, response):
        # maybe this is circular and bad, idk my bff jill
        # bugs? gotta fix'em all
            return response

    def pause(self):
        pause = input("Press <ENTER> to continue")

    def validate_yes_no(self, response):
        valid = False
        if response.lower() == "n" or response.lower() == "y":
            valid = True
        return valid
