# imports
from src.Cookbook import Cookbook
from src.Utilities import Utilities

if __name__ == "__main__":
    main_utils = Utilities()
    a_cookbook = Cookbook()  # TODO: fill with existing cookbook (Load from file)

# TODO: "Select a cookbook to load" prompt

    selection = main_utils.print_main_menu()


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
