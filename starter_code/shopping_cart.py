class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        self.display_cart()

    def remove_item(self, item_name, quantity=1):
        for item in self.items:
            if item.name == item_name:
                if item.quantity <= quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                self.display_cart()
                break

    def display_cart(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(item)
    
    def checkout(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            total_amount = sum(item.price * item.quantity for item in self.items)
            print(f"Total amount due: ${total_amount:.2f}")
            print("Thank you for your purchase!")
            self.items = []

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

    def __len__(self):
        return len(self.items)
