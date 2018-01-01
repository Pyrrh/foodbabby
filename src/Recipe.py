class Recipe(object):

    def __init__(self):
        self.ingredients = [] # need to store lots of qty & unit & ingred per recipe. will be ordered triple
        self.directions = "" # how to make this food
        self.notes = "" # personal annotations re: this recipe
        self.recipe_name = "" # what's in a name?
        self.synopsis = "" # prep time, cook time, bake temp, etc. also short note for easy ref if you want
        self.uses = 0 # track how many times a recipe has been used
        self.source = "" # where did the recipe come from?
        self.labels = [] # used in searching for recipes

# these methods should interact with the database
    # do we need these to go somewhere else? do they make sense as part of this class?

#     Database is for future iteration. For now, let's read & write to JSON
    def add_recipe(self):
        again = "y"
        self.recipe_name = input("Please enter recipe name")
        while again != "n":

            # get ingredient input, split it, store it
            split_input = input("""Please enter ingredient quantity, unit, and name. For example: 
        '2 cups flour'""").split(" ")
            if len(split_input) == 3:
                self.add_ingredient(split_input[0], split_input[1], split_input[2])

            again = input("Are there more ingredients? Y/N").lower()
        input("Please enter all recipe directions")
        input("Please enter any notes for this recipe. If there are none, just press Enter")
        input("Please enter any recipe synopsis you would like to have. This may include"
              " prep time, cook time, baking temperature, or more. If there is none, "
              "just press Enter")
        input("Please enter the recipe source. If you don't want to add one, just press Enter")
        more_labels = "y"
        while more_labels != "n":
            input("Enter a label to tag this recipe with. If you don't want to add one, just press Enter")
            more_labels = input("Is there another label to add? Y/N").lower()
        return

    def get_ingredients(self):

        return

    def edit_recipe(self):
        # maybe I just call add_recipe again and force-overwrite it????? probably a bad idea
        return

    def delete_recipe(self):
        return

    def display_recipe(self):
        return

    # we also will want a 'display all recipes' method but this belongs elsewhere
    # same for searching for recipes

    def add_ingredient(self, qty, unit, name):
        self.ingredients.append((qty, unit, name))
        return
