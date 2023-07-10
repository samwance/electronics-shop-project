import pytest


def test_add_items(testing_item, testing_phone):
    assert testing_item + testing_phone == 7
    assert testing_phone + testing_phone == 4


def test_add_different_types(testing_phone, testing_fail):
    with pytest.raises(TypeError):
        testing_phone + testing_fail
