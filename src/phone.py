from src.item import Item


class Phone(Item):


    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Cannot add `Phone` or `Item` with instances not of `Phone` or `Item` classes")

    def __radd__(self, other):
        return self.__add__(other)
