# imports
from src.Cookbook import Cookbook
from src.Utilities import Utilities

if __name__ == "__main__":
    main_utils = Utilities()
    a_cookbook = Cookbook()  # TODO: fill with existing cookbook (Load from file)

# TODO: "Select a cookbook to load" prompt

    selection = main_utils.print_main_menu()

    while selection != 6:
        # do menu things!
        if selection == 1:
            a_cookbook.add_recipe()
            selection = main_utils.again()

        if selection == 2:
            selection = main_utils.again()

        if selection == 3:
            selection = main_utils.again()

        if selection == 4:
            selection = main_utils.again()

        if selection == 5:
            selection = main_utils.again()

    if selection == 6:
        a_cookbook.save_cookbook()
