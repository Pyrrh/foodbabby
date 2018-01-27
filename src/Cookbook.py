from src.Recipe import Recipe
# from src.Utilities import Utilities


class Cookbook(object):
    def __init__(self):
        self.recipes = []

        # these methods should interact with the database
        # do we need these to go somewhere else? do they make sense as part of this class?

    #     Database is for future iteration. For now, let's read & write to JSON

    def add_recipe(self):
        new_recipe = Recipe()
        new_recipe.get_recipe_content()
        self.recipes.append(new_recipe)
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
