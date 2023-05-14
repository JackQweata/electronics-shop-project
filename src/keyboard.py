from src.item import Item


class KeyBoard(Item):
    LANGUAGES = ["EN", "RU"]

    def __init__(self, name, price, qwt, language="EN"):
        super().__init__(name, price, qwt)
        self._language = language

    def __str__(self):
        return self.name

    def change_lang(self):
        self._language = self.LANGUAGES[
            (self.LANGUAGES.index(self._language) + 1) % len(self.LANGUAGES)
        ]
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
