class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price} x {self.quantity}"

class DigitalItem(Item):
    def __init__(self, name, price, license_key, quantity=1):
        super().__init__(name, price, quantity)
        self.license_key = license_key
    
    def __str__(self):
        return super().__str__() + f" - License Key: {self.license_key}"

class PerishableItem(Item):
    def __init__(self, name, price, expiration_date, quantity=1):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    def __str__(self):
        return super().__str__() + f" - Expiration Date: {self.expiration_date}"
