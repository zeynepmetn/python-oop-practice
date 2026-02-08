class Arac:
    def __init__(self, marka, model):
        self._marka = marka
        self._model = model
    def bilgi_ver(self):
        return f"marka: {self._marka} model: {self._model}"
class Araba(Arac):
    def __init__(self, marka, model, vites):
        super().__init__(marka, model)
        self.vites = vites
    def info(self):
        return f"marka: {self._marka} model: {self._model} vites: {self.vites}"

araba = Araba("enes", 2004,"manuel")
print(araba.info())
