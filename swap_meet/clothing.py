from .item import Item

class Clothing(Item):
    def __init__(self, condition = None):
        super().__init__(category = 'Clothing', condition = condition)


    def __str__(self):
        return "The finest clothing you could wear."