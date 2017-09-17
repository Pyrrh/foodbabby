class Recipe(object):

    def __init__(self):
        #self.quantity = 0
        #self.unit = ""
        #self.ingredient = ""
        self.ingredients = [(0, "", "")] #need to store lots of qty & unit & ingred per recipe
        self.directions = "" #how to make this food
        self.notes = "" #personal annotations re: this recipe
        self.recipe_name = "" #what's in a name?
        self.synopsis = "" #prep time, cook time, bake temp, etc. also short note for easy ref if you want
        self.uses = 0 #track how many times a recipe has been used
        self.source = "" #where did the recipe come from?
        
#these methods should interact with the database
    #do we need these to go somewhere else? do they make sense as part of this class?
    def add_recipe(self):
        return

    def edit_recipe(self):
        return

    def delete_recipe(self):
        return

    def display_recipe(self):
        return

    #we also will want a 'display all recipes' method but this belongs elsewhere
    #same for searching for recipes


