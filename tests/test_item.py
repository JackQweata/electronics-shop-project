"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Apple", 10, 2)
    Item.pay_rate = 0.2
    assert item.price == 10


def test_instances():
    item1 = Item("Apple", 10, 10)
    item2 = Item("Ноут", 20, 20)
    assert len(Item.all) == 2
    assert Item.all[0] == item1
    assert Item.all[1] == item2


def test_set_name():
    item = Item("Apple", 10, 10)
    item.name = "Samsung"
    assert item.name == "Samsung"


def test_set_name_exceeding_length():
    item = Item("Apple", 10, 10)
    with pytest.raises(ValueError):
        item.name = "SamsungSamsungSamsung"


def test_string_to_number():
    assert Item.string_to_number("1.0") == 1.0
    assert Item.string_to_number("10") == 10.0
    assert Item.string_to_number("0.5") == 0.5
    with pytest.raises(ValueError):
        Item.string_to_number("be12")


def test_item_addition_with_phone():
    item = Item("Телефон", 49, 3)
    phone = Phone("iPhone", 999, 10, 2)
    result = item + phone
    assert result == 13


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
