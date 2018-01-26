class Recipe(object):

    def __init__(self):
        self.ingredients = []  # need to store lots of qty & unit & ingred per recipe. will be ordered triple
        self.directions = ""  # how to make this food
        self.notes = ""  # personal annotations re: this recipe
        self.recipe_name = ""  # what's in a name?
        self.synopsis = ""  # prep time, cook time, bake temp, etc. also short note for easy ref if you want
        self.uses = 0  # track how many times a recipe has been used
        self.source = ""  # where did the recipe come from?
        self.labels = []  # used in searching for recipes

    def add_ingredient(self, qty, unit, name):
        self.ingredients.append((qty, unit, name))
        return

    def display_recipe(self):
        print(self.recipe_name + "\n")
        print("Ingredients: \n")
        for i in self.ingredients:
            print(i + "\n")
        print("Directions: \n" + self.directions + "\n")
        print("Notes: \n" + self.notes + "\n")
        if self.source:
            print("Recipe obtained from " + self.source)
        return
