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

    # needs ... reformatting. Not very nice to look at while running
    def get_recipe_content(self):
        again = "y"
        self.recipe_name = input("Please enter recipe name: ")
        while again != "n":

            # get ingredient input, split it, store it
            split_input = input("\nPlease enter ingredient quantity, unit, and name. For example,"
                                "'2 cups flour': ").split(" ")
            if len(split_input) == 3:
                self.add_ingredient(split_input[0], split_input[1], split_input[2])

            again = input("\nAre there more ingredients? Y/N: ").lower()
        self.directions = input("\nPlease enter all recipe directions: ")
        self.notes = input("\nPlease enter any notes for this recipe. If there are none, just press Enter: \n")
        self.synopsis = input("\nPlease enter any recipe synopsis you would like to have. This may include"
                                    " prep time, cook time, baking \ntemperature, or more. If there is none, "
                                    "just press Enter: \n")
        self.source = input(
            "\nPlease enter the recipe source. If you don't want to add one, just press Enter: \n")
        more_labels = "y"
        while more_labels != "n":
            self.labels.append(input("\nEnter a label to tag this recipe with. "
                                           "If you don't want to add one, just press Enter: \n"))
            more_labels = input("\nIs there another label to add? Y/N: ").lower()
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

    def recipe_to_dict(self):
        recipe_dict = {'ingredients': [], 'directions': "", 'notes': "", 'recipe_name': "",
                       'synopsis': "", 'uses': 0, 'source': "", 'labels': []}

        for x in self.ingredients:
            recipe_dict.keys()
        return recipe_dict