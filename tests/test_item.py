"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


def test_item_init(testing_item):
    """Когда мы создаем экземпляр класса со значениями 'Тестовый образец', 100, 5, то вызов атрибутов
    вернет соответствующие значения"""
    assert testing_item.name == 'Testing file'
    assert testing_item.price == 100
    assert testing_item.quantity == 5


def test_calculate_total_price(testing_item):
    assert testing_item.calculate_total_price() == 500


def test_apply_discount(testing_item):
    testing_item.pay_rate = 0.5
    testing_item.apply_discount()
    assert testing_item.price == 50


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_property(testing_item):
    """Проверяем работу геттера и сеттера для атрибута name"""
    assert testing_item.name == 'Testing file'

    testing_item.name = 'Персональный компьютер'
    assert testing_item.name == 'Персональн'

    testing_item.name = 'Ноутбук'
    assert testing_item.name == 'Ноутбук'

def test_repr(testing_item):
    assert repr(testing_item) == "Item('Testing file', 100, 5)"
    assert str(testing_item) == 'Testing file'


def test_instantiate_from_wrong_csv_link():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("items1.csv")


def test_instantiate_from_damaged_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("C:\\Users\\odint\\PycharmProjects\\electronics-shop-project\\src\\fail_items.csv")
