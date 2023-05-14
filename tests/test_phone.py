import pytest
from src.phone import Phone
from src.item import Item


def test_phone_creation():
    phone = Phone("iPhone", 999, 10, 2)
    assert phone.name == "iPhone"
    assert phone.price == 999
    assert phone.qwt == 10
    assert phone.number_of_sim == 2


def test_phone_creation_invalid_sim_cards():
    with pytest.raises(ValueError):
        Phone("Samsung", 799, 5, -1)


def test_phone_addition_with_phone():
    phone1 = Phone("iPhone", 999, 10, 2)
    phone2 = Phone("Samsung", 999, 10, 2)
    result = phone1 + phone2
    assert result == 20


def test_phone_addition_with_invalid_type():
    phone = Phone("iPhone", 999, 10, 2)
    invalid_object = "Invalid"
    with pytest.raises(TypeError):
        phone + invalid_object
