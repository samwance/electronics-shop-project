from src.item import Item


class Phone(Item):


    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0 and value % 1 == 0:
            raise ValueError("ValueError: the amount of sim-cards are must be integer and above zero.")
        self.__number_of_sim = value


    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Cannot add `Phone` or `Item` with instances not of `Phone` or `Item` classes")

    def __radd__(self, other):
        return self.__add__(other)
