# Joshua Chan
# 1588459
class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0,item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
# The arguments are defined above
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $'+str(cost))
# The item cost is calculated above
    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)
# A description of the item is printed above
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_list=None):
        if cart_list is None:
            cart_list = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_list
# A new class called 'ShoppingCart' is defined above
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
# a function to add items to the cart above
    def remove_item(self, it_name):
        for object in self.cart_items:
            if object.item_name == it_name:
                self.cart_items.remove(object)
                return
        print("\nItem not found in cart. Nothing removed.")
# a function to remove items from the cart above
    def modify_item(self, ItemToPurchase):
        item_found = False
        for object in self.cart_items:
            if object.item_name == ItemToPurchase.item_name:
                item_found = True
                print("Enter the new quantity:")
                item_quantity = int(input())
                ItemToPurchase = object
                ItemToPurchase.item_quantity = item_quantity
                if ItemToPurchase.item_description != "none":
                    object.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0:
                    object.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    object.item_quantity = ItemToPurchase.item_quantity
        if not item_found:
            print("\nItem not found in cart. " + "Nothing modified.")
# The function above will modify item quantity or if nothing is modified a statement will be printed

    def get_num_items_in_cart(self):
        total_quantity = 0
        for object in self.cart_items:
            total_quantity = total_quantity + object.item_quantity
        return total_quantity
# the function above returns the number of items in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        for object in self.cart_items:
            total_cost = total_cost + (object.item_price * object.item_quantity)
        return total_cost
# The function above returns the full cost in the cart
    def print_total(self):
        if len(self.cart_items) != 0:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: " + str(self.get_num_items_in_cart()))
            print()
            for obj in self.cart_items:
                obj.print_item_cost()
            print("\nTotal: $" + str(self.get_cost_of_cart()))
        else:
            print("\nSHOPPING CART IS EMPTY")
# The function above will print the customer name, number of items, and total cost
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("\nItem Descriptions")
        for obj in self.cart_items:
            obj.print_item_description()
# The function above will print the customer name, current date, and item descriptions
def menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")
# The options presented to the user are shown above
def print_menu(self):
    choice = menu()
    choice = input("Choose an option: ")
# the function will accept an input from the menu function before
    while choice != 'q':
        if choice == 'a':
            print("\nADD ITEM TO CART")
            print("Enter the item name:")
            item_name = input()
            print("Enter the item description:")
            item_description = input()
            print("Enter the item price:")
            item_price = int(input())
            print("Enter the item quantity:")
            item_quantity = int(input())
            item = ItemToPurchase(item_name, item_price,item_quantity, item_description)
            self.add_item(item)
# Adding an item to the cart
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            item_name = input()
            self.remove_item(item_name)
# Removing an item from the cart
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()
            item = ItemToPurchase(item_name)
            self.modify_item(item)
# Changing the quantity of an item in the cart
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()
# Printing the descriptions of items in the cart
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            self.print_total()
# Print the shopping cart
        else:
            print("\nInvalid choice! Please enter " + "a valid choice:")
# If no valid option was entered
        menu()
        choice = input("Choose an option: ")
def main():
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    shopping_cart = ShoppingCart(customer_name, current_date)
    print("\nCustomer name: " + shopping_cart.customer_name)
    print("Today's date: " + shopping_cart.current_date)
    print_menu(shopping_cart)
# Main function will record and print customers name and today's date
main()