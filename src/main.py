# imports
from signal import pause

from src.Cookbook import Cookbook
from src.Utilities import Utilities

if __name__ == "__main__":
    main_utils = Utilities()
    load = main_utils.ask_load_from_file()
    a_cookbook = Cookbook()  # TODO: fill with existing cookbook (Load from file)
    if load == "y":
        Cookbook.load_cookbook(a_cookbook)

# TODO: "Select a cookbook to load" prompt

    selection = main_utils.print_main_menu()

    while selection != "6":  # this input is validated in print_main_menu()
        # do menu things!
        if selection == "1":
            a_cookbook.add_recipe()
            selection = main_utils.again()

        if selection == "2":
            selection = main_utils.again()

        if selection == "3":
            a_cookbook.display_cookbook()
            main_utils.pause()
            selection = main_utils.again()
        #currently has a bug where after pause 1 enter does not display again text & two errors program to exit. 

        if selection == "4":
            selection = main_utils.again()

        if selection == "5":
            selection = main_utils.again()

# separated because it doesn't need to be another conditional branch
    if selection == "6":
        a_cookbook.save_cookbook()
