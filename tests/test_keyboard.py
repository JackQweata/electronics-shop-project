import pytest
from src.keyboard import KeyBoard


def test_keyboard():
    keyboard = KeyBoard("Mechanical Keyboard", 200, 1)
    assert str(keyboard) == 'Mechanical Keyboard'
    assert keyboard.language == "EN"


def test_keyboard_language():
    keyboard = KeyBoard("Mechanical Keyboard", 200, 1)
    keyboard.change_lang()
    assert keyboard.language == "RU"

    with pytest.raises(AttributeError):
        keyboard.language = "FR"
