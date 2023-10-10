class Animsaticilar:
    def __init__(self, kisi_veya_kurum, yer, gun, saat):
        self.kisi_veya_kurum = kisi_veya_kurum
        self.yer = yer
        self.gun = gun
        self.saat = saat

    def info(self):
        print("Animsatici Bilgileri:")
        print("Kişi veya Kurum:", self.kisi_veya_kurum)
        print("Yer:", self.yer)
        print("Gün:", self.gun)
        print("Saat:", self.saat)

class KullaniciGirisi(Animsaticilar):
    def __init__(self, kisi_veya_kurum, yer, gun, saat):
        super().__init__(kisi_veya_kurum, yer, gun, saat)

    def bilgi_gir(self):
        self.kisi_veya_kurum = input("Kişi veya Kurum: ")
        self.yer = input("Yer: ")
        self.gun = input("Gün: ")
        self.saat = input("Saat: ")

    def olay_sil(self, kisi=None, gun=None):
        if kisi is not None and self.kisi_veya_kurum == kisi:
            self.kisi_veya_kurum = ""
            self.yer = ""
            self.gun = ""
            self.saat = ""
        elif gun is not None and self.gun == gun:
            self.kisi_veya_kurum = ""
            self.yer = ""
            self.gun = ""
            self.saat = ""

# programın başladığı yer
print("Kişisel Ajandam")
kullanici_giris = KullaniciGirisi("", "", "", "")

while True:
    print("Yapabileceğiniz işlemler: ")
    print("1. Olay Girişi Yap")
    print("2. Olay Sil")
    print("3. Olayları Göster")
    print("4. Çıkış için 'q' yazınız.")
    secim = input("Hangi işlemi yapmak istiyorsunuz? : ")

    if secim.lower() == 'q':
        break

    elif secim == "1":
        kullanici_giris = KullaniciGirisi("", "", "", "")
        kullanici_giris.bilgi_gir()
        kullanici_giris.info()


    elif secim == "2":

        kullanici_giris = KullaniciGirisi("", "", "", "")

        kullanici_giris.olay_sil()

        print("Olay bilgileri silindi.")

    elif secim == "3":

        kullanici_giris.info()



