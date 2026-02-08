class Urun:
    def __init__(self, isim, fiyat, stok):
        self.isim = isim
        self.fiyat = fiyat
        self.stok = stok

    def urun_bilgisi(self):
        print(f"İsim: {self.isim}, Fiyat: {self.fiyat} TL, Stok: {self.stok}")

    def stok_azaltma(self):
        sayi = int(input("Stok eksiltme sayısı: "))
        if sayi <= self.stok:
            self.stok -= sayi
            print(f"Yeni stok: {self.stok}")
        else:
            print("Yetersiz stok!")

    def stok_arttirma(self):
        sayi = int(input("Stok artırma sayısı: "))
        self.stok += sayi
        print(f"Yeni stok: {self.stok}")

    def fiyat_guncelle(self):
        yeni = float(input("Yeni fiyat: "))
        self.fiyat = yeni
        print(f"Güncel fiyat: {self.fiyat} TL")


def menu():
    print("CARSAMBA PAZARINA HOSGELDİNİZ!!!!")

    # Ürünler bir kere oluşturuluyor
    domates = Urun("Domates", 5, 10)
    patates = Urun("Patates", 7, 3)

    while True:
        print("\nÜrün seçin:")
        print("1- Domates")
        print("2- Patates")
        print("3- Çıkış")

        giris = input("-> ")

        if giris == "1":
            urun = domates
        elif giris == "2":
            urun = patates
        elif giris == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")
            continue

        print("\nYapılacak işlemi seçin:")
        print("1- Stok güncelleme")
        print("2- Ürün bilgisi")
        print("3- Fiyat güncelleme")

        islem = input("-> ")

        if islem == "1":
            print("1- Stok azaltma")
            print("2- Stok artırma")
            stok_giris = input("-> ")

            if stok_giris == "1":
                urun.stok_azaltma()
            elif stok_giris == "2":
                urun.stok_arttirma()
            else:
                print("Geçersiz işlem!")

        elif islem == "2":
            urun.urun_bilgisi()

        elif islem == "3":
            urun.fiyat_guncelle()

        else:
            print("Geçersiz işlem!")


menu()
