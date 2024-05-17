from shopping_cart import ShoppingCart
from itemfactory import ItemFactory, register_item_type

def main():
    cart = ShoppingCart()
    sample_item = ItemFactory.create_item("standard", "pencil", 2, 3)
    cart.add_item(sample_item)
    
    while True:
        print("############################")
        print("\n--- Shopping Cart Menu ---")
        print("0. Exit")
        print("1. Display cart")
        print("2. Add item to the cart")
        print("3. Remove item from the cart")
        print("4. Checkout")
        
        choice = input("Please choose an option: ")
        if choice == "0":
            print("Thank you for shopping with us!")
            print(repr(cart))
            break
        elif choice == "1":
            cart.display_cart()
        elif choice == "2":
            print("Available item types: ", ItemFactory.get_item_types())
            item_type = input('Enter the item type:')
            name = input("Enter the item name:")
            price = float(input("Enter the price:"))
            quantity = int(input("Enter the quantity:"))
            if item_type == 'digital':
                license_key = input("Enter the license key:")
                item = ItemFactory.create_item(item_type, name, price, license_key, quantity)
            elif item_type == 'perishable':
                expiration_date = input("Enter the expiration date:")
                item = ItemFactory.create_item(item_type, name, price, expiration_date, quantity)
            else:
                item = ItemFactory.create_item(item_type, name, price, quantity)
            cart.add_item(item)
        elif choice == "3":
            cart.display_cart()
            item_name = input("Enter the item name to remove:")
            quantity = int(input("Enter the quantity to remove:"))
            cart.remove_item(item_name, quantity)
        elif choice == "4":
            cart.checkout()
        else:
            print("Invalid Option! Try again!")
        
if __name__ == '__main__':
    main()
