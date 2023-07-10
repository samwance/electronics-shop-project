import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def testing_item():
    return Item('Testing file', 100, 5)


@pytest.fixture
def testing_phone():
    return Phone("iPhone 14", 120000.0, 2, 5)


@pytest.fixture
def testing_fail():
    return None
