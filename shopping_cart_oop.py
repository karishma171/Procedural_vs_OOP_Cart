# Object-oriented approach

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, name, price):
        item = Item(name, price)
        self.cart.append(item)
        print(f"Added {item}")

    def remove_item(self, name):
        for product in self.cart:
            if product.name == name:
                self.cart.remove(product)
                print(f"Removed {name}")
                return
        print(f"{name} not found in the cart")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty")
            return
        print("Shopping Cart:")
        total = 0
        for product in self.cart:
            print(product)
            total += product.price
        print(f"Total: ${total}")

# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 999)
cart.add_item("Mouse", 25)
cart.remove_item("Laptop")
cart.view_cart()
