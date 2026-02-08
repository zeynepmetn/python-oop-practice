
class Ogrenci:
    def __init__(self, ad, yas):
        self.__ad = ad
        self.__yas = yas

    def get_ad(self):
        return self.__ad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        self.__yas = yeni_yas


class Bolum(Ogrenci):
    def __init__(self, ad, yas, bolum):
        super().__init__(ad, yas)
        self._bolum = bolum

    def display_info(self):
        print(f"{self.get_ad()}, {self.get_yas()}, {self._bolum}")

ogrenci1 = Bolum("ahmet", 23, "bm")
ogrenci1.display_info()