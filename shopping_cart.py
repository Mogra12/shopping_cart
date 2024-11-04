class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name, price):
        item = (item_name, price)
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed successfully")
    
    def get_total(self):
        total = 0
        for i in self.items:
            total += i[1]
        return total

shopping_cart = ShoppingCart()
print("-"*30)
qty_items = int(input("How much items you want add? "))
try:
    for i in range(0,qty_items):
        item_name = input(f"Enter item name {i+1}: ").rstrip()
        price = float(input(f"Enter item price {i+1}: ").replace(",","."))
        shopping_cart.add_item(item_name, price)
        print("-"*30)
except ValueError:
    print("Invalid input. Please enter a valid number.")
print(f"Was added these products: {shopping_cart.items}")
print(f"Total: R$ {shopping_cart.get_total():.2f}".replace(",","."))