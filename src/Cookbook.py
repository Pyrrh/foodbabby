from src.Recipe import Recipe
from src.Utilities import Utilities


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
        new_recipe.recipe_name = input("Please enter recipe name")
        while again != "n":

            # get ingredient input, split it, store it
            split_input = input("""Please enter ingredient quantity, unit, and name. For example: 
                '2 cups flour'""").split(" ")
            if len(split_input) == 3:
                new_recipe.add_ingredient(split_input[0], split_input[1], split_input[2])

            again = input("Are there more ingredients? Y/N").lower()
        new_recipe.directions = input("Please enter all recipe directions")
        new_recipe.notes = input("Please enter any notes for this recipe. If there are none, just press Enter")
        new_recipe.synopsis = input("Please enter any recipe synopsis you would like to have. This may include"
                              " prep time, cook time, baking temperature, or more. If there is none, "
                              "just press Enter")
        new_recipe.source = input("Please enter the recipe source. If you don't want to add one, just press Enter")
        more_labels = "y"
        while more_labels != "n":
            new_recipe.labels.append(input("Enter a label to tag this recipe with. "
                                     "If you don't want to add one, just press Enter"))
            more_labels = input("Is there another label to add? Y/N").lower()
        return

    def edit_recipe(self):
        return

    def delete_recipe(self):
        return

    def display_recipe(self):
        return

        # we also will want a 'display all recipes' method
        # same for searching for recipes