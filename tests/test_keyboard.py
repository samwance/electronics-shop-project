import pytest


def test_keyboard_attributes(testing_keyboard):
    assert str(testing_keyboard) == "Dark Project KD87A"
    assert str(testing_keyboard.language) == "EN"


def test_change_lang(testing_keyboard):
    testing_keyboard.change_lang()
    assert testing_keyboard.language == "RU"
    
    
def test_set_unsupported_language(testing_keyboard):
    with pytest.raises(AttributeError) as e:
        testing_keyboard.language = 'CH'

    assert str(e.value) == "property 'language' of 'KeyBoard' object has no setter"
