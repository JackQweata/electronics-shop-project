from src.item import Item


class Phone(Item):
    def __init__(self, name, price, qwt, sim_cards):
        super().__init__(name, price, qwt)
        if sim_cards <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = sim_cards

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.qwt}, {self._number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.qwt + other.qwt
        elif isinstance(other, Item):
            return self.qwt + other.qwt
        else:
            raise TypeError("Нельзя складывать экземпляры класса Phone или Item с объектами других классов.")

    def __radd__(self, other):
        return self.__add__(other)
