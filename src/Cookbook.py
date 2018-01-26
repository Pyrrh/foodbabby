from src.Recipe import Recipe
# from src.Utilities import Utilities


class Cookbook(object):
    def __init__(self):
        self.recipes = []

        # these methods should interact with the database
        # do we need these to go somewhere else? do they make sense as part of this class?

    #     Database is for future iteration. For now, let's read & write to JSON

    @staticmethod  # it told me to. TODO: research this & learn what it's about in python vs c/java
    def add_recipe():
        new_recipe = Recipe()
        again = "y"
        new_recipe.recipe_name = input("Please enter recipe name: ")
        while again != "n":

            # get ingredient input, split it, store it
            split_input = input("\nPlease enter ingredient quantity, unit, and name. For example," 
                                "'2 cups flour': ").split(" ")
            if len(split_input) == 3:
                new_recipe.add_ingredient(split_input[0], split_input[1], split_input[2])

            again = input("\nAre there more ingredients? Y/N: ").lower()
        new_recipe.directions = input("\nPlease enter all recipe directions: ")
        new_recipe.notes = input("\nPlease enter any notes for this recipe. If there are none, just press Enter: \n")
        new_recipe.synopsis = input("\nPlease enter any recipe synopsis you would like to have. This may include"
                                    " prep time, cook time, baking \ntemperature, or more. If there is none, "
                                    "just press Enter: \n")
        new_recipe.source = input("\nPlease enter the recipe source. If you don't want to add one, just press Enter: \n")
        more_labels = "y"
        while more_labels != "n":
            new_recipe.labels.append(input("\nEnter a label to tag this recipe with. "
                                     "If you don't want to add one, just press Enter: \n"))
            more_labels = input("\nIs there another label to add? Y/N: ").lower()
        return

    def edit_recipe(self):
        return

    def delete_recipe(self):
        return

    def find_recipe_by_name(self, name):
        return

    def find_recipe_by_label(self, label):
        return

    def display_cookbook(self):
        for r in self.recipes:
            r.display_recipe()
        return
