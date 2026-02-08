class Araba:
        def __init__(self, marka,model,yıl):
                self.marka=marka
                self.model= model
                self.yıl = yıl

        def bilgi(self):
                print(f"Araba Bilgisi: Marka: {self.marka}, Model: {self.model}, Yıl: {self.yıl}")

        def araba_yas(self):
                print(f"ARABANIN YAŞI: {2024-self.yıl}")


def menu():
        print("1- araba 1")
        print("2- araba 2")
        print("3- araba 3")
        giris = input("->")
        if giris == "1":
                araba1 = Araba("toyota", "corolla", 2020)
                araba1.bilgi()
                araba1.araba_yas()
        elif giris == "2":
                araba2 = Araba("Opel", "Astra", 2012)
                araba2.bilgi()
                araba2.araba_yas()
        elif giris=="3":
                araba3 = Araba("Peugeot", "308", 2009)
                araba3.bilgi()
                araba3.araba_yas()

        elif not giris.isdigit():
                print("Adam gibi bir şey gir")
                menu()

menu()