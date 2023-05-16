import csv
import os


class Item:
    pay_rate = None
    all = []

    def __init__(self, name, price, qwt):
        self._name = name
        self.price = price
        self.qwt = qwt
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.qwt})"

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self):
        return self.price * self.qwt

    def apply_discount(self):
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, name_file='items.csv'):
        file_path = os.path.join(os.path.dirname(__file__), name_file)
        Item.dir_csv = os.path.abspath(file_path)

        if not os.path.isfile(Item.dir_csv):
            raise FileNotFoundError("Отсутствует файл items.csv")

        try:
            with open(Item.dir_csv, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row.get('name')
                    price = row.get('price')
                    quantity = row.get('quantity')
                    if name and price is not None and quantity is not None:
                        Item(name, cls.string_to_number(price), cls.string_to_number(quantity))
                    else:
                        raise InstantiateCSVError(f"Файл {name_file} поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Файл не обнаружен")

    @staticmethod
    def string_to_number(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError("Invalid number format")


class InstantiateCSVError(Exception):
    pass
