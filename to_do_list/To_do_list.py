from datetime import datetime

# Üst Sınıf (Superclass)
class Animsaticilar:
    def __init__(self, kisi_veya_kurum, yer, gun, saat):
        self.kisi_veya_kurum = kisi_veya_kurum
        self.yer = yer
        self.gun = gun
        self.saat = saat

    def info(self):
        return f"{self.kisi_veya_kurum}, {self.yer}, {self.gun}, {self.saat}"

    def tarih(self):
        try:
            tarih_obj = datetime.strptime(self.gun, "%d/%m/%Y")
            return tarih_obj
        except (ValueError, TypeError):
            return datetime.max

# Alt Sınıf (Subclass)
class KullaniciGirisi(Animsaticilar):
    def __init__(self):
        super().__init__("Boş", "Boş", "01/01/1900", "00:00")  # Superclass'ın __init__ metodunu çağırarak giriş listesi oluşturun
        self.girisler = []
        self.giris_id_counter = 0  # Her girişin kendine ait bir ID'si olsun

    def tarih_gir(self):
        gun = int(input("Gün: "))
        ay = int(input("Ay: "))
        yil = int(input("Yıl: "))

        tarih_str = f"{gun:02d}/{ay:02d}/{yil:04d}"

        try:
            tarih_obj = datetime.strptime(tarih_str, "%d/%m/%Y")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'Gün Ay Yıl' formatında girin.")
            return

        saat = input("Saat: ")
        kisi_veya_kurum = input("Kişi veya Kurum: ")
        yer = input("Yer: ")

        giris = Animsaticilar(kisi_veya_kurum, yer, tarih_obj.strftime("%d/%m/%Y"), saat)
        self.girisler.append(giris)
        self.giris_id_counter += 1

    def olay_sil(self, kisi=None, gun=None):
        if kisi is not None:
            girisler = [giris for giris in self.girisler if kisi != giris.kisi_veya_kurum]
        elif gun is not None:
            girisler = [giris for giris in self.girisler if gun != giris.gun]
        else:
            print("Lütfen silmek istediğiniz olayın adını veya tarihini girin.")
            return

        if len(girisler) == len(self.girisler):
            print("Bu olay bulunamadı.")
        else:
            self.girisler = girisler
            print("Olay başarıyla silindi.")

    def info(self):
        sirali_girisler = sorted(self.girisler, key=lambda x: x.tarih() or datetime.max)

        print("Hatırlatıcılar:")
        for index, giris in enumerate(sirali_girisler):
            print(f"{index}. {giris.info()}")

    def olay_duzenle(self):
        try:
            giris_id = int(input("Düzenlemek istediğiniz girişin ID'sini giriniz: "))
            if giris_id < len(self.girisler):
                giris = self.girisler[giris_id]
                kisi_veya_kurum = input("Kişi veya Kurum: ")
                yer = input("Yer: ")
                tarih = input("Tarih (Gün Ay Yıl): ")
                saat = input("Saat: ")
                aciklama = input("Açıklama: ")

                giris.kisi_veya_kurum = kisi_veya_kurum
                giris.yer = yer
                giris.gun = tarih
                giris.saat = saat
                giris.aciklama = aciklama

                print("Olay başarıyla güncellendi.")
            else:
                print("Geçersiz giriş ID'si.")
        except ValueError:
            print("Geçersiz giriş ID'si.")

# Ana program
print("Kişisel Ajandam")
kullanici_giris = KullaniciGirisi()

while True:
    print("Yapabileceğiniz işlemler: ")
    print("1. Olay Girişi Yap")
    print("2. Olay Sil (Kişi veya Tarih ile silme)")
    print("3. Olayları Göster")
    print("4. Olay Düzenle")
    print("5. Çıkış için 'q' yazınız.")

    secim = input("Hangi işlemi yapmak istiyorsunuz? : ")

    if secim.lower() == 'q':
        break

    if secim == "1":
        kullanici_giris.tarih_gir()

    elif secim == "2":
        kisi_sil = input("Silmek istediğiniz kişi veya kurumu giriniz: ")
        tarih_sil = input("Silmek istediğiniz tarihi (Gün Ay Yıl) giriniz: ")
        kullanici_giris.olay_sil(kisi_sil, tarih_sil)

    elif secim == "3":
        kullanici_giris.info()

    elif secim == "4":
        kullanici_giris.olay_duzenle()

