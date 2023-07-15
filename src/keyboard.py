from src.item import Item


class LanguageMixin:

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_language):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


    def change_lang(self):
        self._language = "RU" if self.language == "EN" else "EN"
        return self

class Keyboard(Item, LanguageMixin):


    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)


    def __str__(self):
        return self.name


    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"
