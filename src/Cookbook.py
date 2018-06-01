from src.Recipe import Recipe
import json
from src.Utilities import Utilities


class Cookbook(object):
    def __init__(self):
        self.recipes = {}
        self.name = input("Please name your cookbook: ")
        #TODO: don't initialize with input every time because it doesn't make sense when loading existing recipes
        self.utilities = Utilities()
        # define name of cookbook; TODO: allow load from a list of existing books

    #     Database is for future iteration. For now, let's read & write to JSON

    def add_recipe(self):
        new_recipe = Recipe()
        new_recipe.get_recipe_content()
        self.recipes[new_recipe.recipe_name] = new_recipe
        return

    def edit_recipe(self):
        return

    def delete_recipe(self):
        return

    def find_recipe_by_name(self, name):
        for key in self.recipes:
            if key == name:
                self.recipes[name].display_recipe()
        return

    def find_recipe_by_label(self, label):
        return

    def display_cookbook(self):
        for key in self.recipes:
            self.recipes[key].display_recipe()
        return

    def save_cookbook(self):
        # TODO: add saving a 'backup' copy of cookbook as default behavior
        cookbook_dict = Utilities.recipe_to_dict(self)

        with open(self.name + '.txt', 'w') as out:
            json.dump(cookbook_dict, out)
        return

    def load_cookbook(self):
        with open(input("Please enter filename, without extension (e.g. '.txt'): ") + ".txt", 'r') as read_file:
            cookbook_content = json.load(read_file)

        self.recipes = cookbook_content
        return
