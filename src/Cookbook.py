from src.Recipe import Recipe
import json
# from src.Utilities import Utilities


class Cookbook(object):
    def __init__(self):
        self.recipes = []
        self.name = input("Please name your cookbook: ")
        # define name of cookbook; TODO: allow load from a list of existing books

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

    def save_cookbook(self):
        # TODO: add saving a 'backup' copy of cookbook as default behavior
        cookbook_dict = {'recipes': []}

        # iterate and add each recipe to the dictionary
        for r in self.recipes:
            cookbook_dict['recipes'].append(r.recipe_to_dict())

        with open(self.name + '.txt', 'w') as out:
            json.dump(cookbook_dict, out)
        return

    def load_cookbook(self):
        return
