from abc import ABC, abstractmethod

class Odeme(ABC):
    @abstractmethod
    def odeme(self, miktar):
        pass

class Kredikartiodeme(Odeme):
    def odeme(self, miktar):
        print(f"kredi karti odeme {miktar}")

class paypalodeme(Odeme):
    def odeme(self, miktar):
        print("paypal odeme")

odeme1 = Kredikartiodeme()
odeme1.odeme(300)