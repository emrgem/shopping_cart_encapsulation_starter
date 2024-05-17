from items import Item, DigitalItem, PerishableItem

class ItemFactory:
    item_types = {
        'standard': Item,
        'digital': DigitalItem,
        'perishable': PerishableItem
    }

    @staticmethod
    def create_item(type, *args, **kwargs):
        item_class = ItemFactory.item_types.get(type)
        if item_class:
            return item_class(*args, **kwargs)
        raise ValueError("Unknown item type")
    
    @staticmethod
    def get_item_types():
        return list(ItemFactory.item_types.keys())

def register_item_type(type_name, item_class):
    ItemFactory.item_types[type_name] = item_class
