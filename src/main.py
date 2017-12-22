#imports
from .Recipe import Recipe
import Utilities


if __name__ == "__main__":
    a_recipe = Recipe()

    isValid = False


    print("MAIN MENU\n\n")
    print("Select an option: \n")

    print("""
    1. Add a recipe (NOT IMPLEMENTED)
    2. Find a recipe (NOT IMPLEMENTED)
    3. Build a shopping list (NOT IMPLEMENTED)
    4. Save and Quit (SAVE NOT IMPLEMENTED, QUITTING IS EASY)
    
    """)
    #refactor to have menu display during a single function call

    while isValid != True:
        isValid = Utilities.validate(input())


