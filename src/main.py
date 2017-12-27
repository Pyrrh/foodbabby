

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

#imports
from src.Recipe import Recipe
from src.Utilities import Utilities

if __name__ == "__main__":
    a_recipe = Recipe()

    isValid = False


    print("MAIN MENU\n\n")
    print("Select an option: \n")

    print("""
    1. Add a recipe (NOT IMPLEMENTED)
    2. Find a recipe (NOT IMPLEMENTED)
    3. Display a recipe (NOT IMPLEMENTED, DEPENDS ON 2. ABOVE)
    4. Delete a recipe (NOT IMPLEMENTED, DEPENDS ON 2. ABOVE)
    5. Build a shopping list (NOT IMPLEMENTED)
    6. Save and Quit (SAVE NOT IMPLEMENTED, QUITTING IS EASY)
    
    """)
    #refactor to have menu display during a single function call

    while isValid != True:
        isValid = Utilities.validate(input())


