# Import testing suite & do the things
import unittest
from src.Recipe import Recipe
from src.Utilities import Utilities
from src.Cookbook import Cookbook


# modify this base test case

class TestAddIngredient(unittest.TestCase):
    def test_add_two_ingredients(self):
        test_recipe = Recipe()

        test_recipe.add_ingredient(1, "cup", "flour")

        self.assertEqual(test_recipe.ingredients, [(1, "cup", "flour")])

        test_recipe.add_ingredient(3, "Tbsp", "cinnamon")

        self.assertEqual(test_recipe.ingredients, [(1, "cup", "flour"), (3, "Tbsp", "cinnamon")])


class TestAddRecipe(unittest.TestCase):
    def test_add_recipe(self):
        test_book = Cookbook()
        test_book.add_recipe()

        self.assertNotEqual(test_book.recipes[0].recipe_name, "")
        # can assert more things here to ensure ingredient, directions, etc are not empty
        # this test is bad and it should feel bad
        # (tests should be automated and not take user input)

class TestDisplayRecipe(unittest.TestCase):
    def test_display_one_recipe(self):
        test_recipe = Recipe()
        test_recipe.directions = ""
        test_recipe.ingredients = []
        test_recipe.labels = []
        test_recipe.notes = ""
        test_recipe.recipe_name = ""
        test_recipe.source = ""
        test_recipe.synopsis = ""
        test_recipe.uses = 0

        self.assertEqual(test_recipe.display_recipe(), "")
