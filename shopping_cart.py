class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, __item_name, __price):
        item = (__item_name, __price)
        self.__items.append(item)

    def remove_item(self, __item):
        if __item in self.__items:
            self.__items.remove(__item)
            print(f"{__item} removed successfully")
    
    def get_total(self):
        total = 0
        for i in self.__items:
            total += i[1]
        return total

__shopping_cart = ShoppingCart()
print("-"*30)
qty___items = int(input("How much __items you want add? "))
try:
    for i in range(0,qty___items):
        __item_name = input(f"Enter item name {i+1}: ").rstrip()
        __price = float(input(f"Enter item __price {i+1}: ").replace(",","."))
        __shopping_cart.add_item(__item_name, __price)
        print("-"*30)
except ValueError:
    print("Invalid input. Please enter a valid number.")
print(f"Was added these products: {__shopping_cart.__items}")
print(f"Total: R$ {__shopping_cart.get_total():.2f}".replace(",","."))
