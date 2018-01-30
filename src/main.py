# imports
from src.Cookbook import Cookbook
from src.Utilities import Utilities
import json

if __name__ == "__main__":
    main_utils = Utilities()
    a_cookbook = Cookbook()

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
    # refactor to have menu display during a single function call

    selection = input()
    while not isValid:
        isValid = Utilities.validate_selection(selection)

    # do menu things!
    if selection == 1:
        a_cookbook.add_recipe()

    if selection == 2:
        print()

    if selection == 3:
        print()

    if selection == 4:
        print()

    if selection == 5:
        print()

    if selection == 6:
        print()

    testJson = [a_cookbook]

    with open('testcookbook.txt', 'w') as out:
        json.dump(testJson, out)
