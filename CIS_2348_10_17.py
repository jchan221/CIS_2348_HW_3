# Joshua Chan
# 1588459
class ItemToPurchase:

    def __init__(self,item_name='none',item_price=0.0,item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
# The arguments are defined above
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $'+str(cost))
# The item cost is calculated above


if __name__ == '__main__':
    print('Item 1')

    first_item = ItemToPurchase()
    second_item = ItemToPurchase()

    first_item.item_name = input('Enter the item name:\n')
    first_item.item_price = int(input('Enter the item price:\n'))
    first_item.item_quantity = int(input('Enter the item quantity:\n'))
    print('\nItem 2')

    second_item.item_name = input('Enter the item name:\n')
    second_item.item_price = int(input('Enter the item price:\n'))
    second_item.item_quantity = int(input('Enter the item quantity:\n'))
    print('\nTOTAL COST')
# The items to be purchased are recorded in name, price, and quantity
    first_item.print_item_cost()
    second_item.print_item_cost()

    total_cost = (first_item.item_price * first_item.item_quantity) + (second_item.item_price * second_item.item_quantity)
# The cost of both items is calculated above
    print('\nTotal: $' + str(total_cost))


