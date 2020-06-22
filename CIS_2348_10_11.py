# Joshua Chan
# 1588459
class FoodItem:
    def __int__(self, name, fat, carbohydrates, protein):
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein
# The first function will set the arguments
    def __init__(self, name=None, fat=0.0, carbohydrates=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein
# The second function will set the arguments to types
    def get_calories(self, num_of_servings):
        calories = ((self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4) * num_of_servings)
        return calories
# The function above will calculate the calories and return the answer
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbohydrates))
        print('   Protein: {:.2f} g'.format(self.protein))
# The function above will print the inputs given by the user

if __name__ == '__main__':
    food_item1 = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbohydrates = float(input())
    amount_protein = float(input())
# The inputs are shown above to fill in the functions
    food_item2 = FoodItem(item_name, amount_fat, amount_carbohydrates, amount_protein)
#The second food item will run through the class again
    num_servings = float(input())
# The servings will be recorded through the input above
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item1.get_calories(num_servings)))
# The first food item will be printed above
    print()
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item2.get_calories(num_servings)))
#The second food item will be printed above