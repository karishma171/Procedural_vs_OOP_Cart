# Procedural approach

# Global shopping cart list
cart = []

def add_item(item, price):
    cart.append({'item': item, 'price': price})
    print(f"Added {item} for ${price}")

def remove_item(item):
    for product in cart:
        if product['item'] == item:
            cart.remove(product)
            print(f"Removed {item}")
            return
    print(f"{item} not found in the cart")

def view_cart():
    if not cart:
        print("Cart is empty")
        return
    print("Shopping Cart:")
    total = 0
    for product in cart:
        print(f"{product['item']} - ${product['price']}")
        total += product['price']
    print(f"Total: ${total}")

# Example usage
add_item("Laptop", 999)
add_item("Mouse", 25)
remove_item("Laptop")
view_cart()
