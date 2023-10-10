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
            # Tarihi yıl, ay ve gün olarak bölüp sıralamak için kullanın
            tarih_obj = datetime.strptime(self.gun, "%d/%m/%Y")
            return tarih_obj
        except (ValueError, TypeError):
            return datetime.max  # Geçerli bir tarih yoksa, en büyük tarihi kullan


# Alt Sınıf (Subclass)
class KullaniciGirisi(Animsaticilar):
    def __init__(self):
        self.girisler = []  # Tüm girişleri saklamak için bir liste oluşturun

    def tarih_gir(self):
        gun = int(input("Gün: "))  # Günü tamsayıya çevirin
        ay = int(input("Ay: "))  # Ayı tamsayıya çevirin
        yil = int(input("Yıl: "))  # Yılı tamsayıya çevirin

        # Kullanıcının girdiği tarih bilgisini otomatik olarak formatlayın
        tarih_str = f"{gun:02d}/{ay:02d}/{yil:04d}"

        try:
            # Kullanıcının girdiği tarihi datetime nesnesine çevirin
            tarih_obj = datetime.strptime(tarih_str, "%d/%m/%Y")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'Gün Ay Yıl' formatında girin.")
            return

        saat = input("Saat: ")
        kisi_veya_kurum = input("Kişi veya Kurum: ")
        yer = input("Yer: ")

        giris = Animsaticilar(kisi_veya_kurum, yer, tarih_obj.strftime("%d/%m/%Y"), saat)
        self.girisler.append(giris)

    def olay_sil(self, kisi=None, gun=None):
        # Olay silme işlemini güncelleyin (isteğe bağlı)
        pass

    def info(self):
        # Hatırlatıcıları tarihe göre sıralayın
        sirali_girisler = sorted(self.girisler, key=lambda x: x.tarih() or datetime.max)

        print("Hatırlatıcılar:")
        for giris in sirali_girisler:
            print("- " + giris.info())


# Ana program
print("Kişisel Ajandam")
kullanici_giris = KullaniciGirisi()  # KullaniciGirisi nesnesini başlangıçta oluşturun

while True:
    print("Yapabileceğiniz işlemler: ")
    print("1. Olay Girişi Yap")
    print("2. Olay Sil (Kişi veya Tarih ile silme)")
    print("3. Olayları Göster")
    print("4. Çıkış için 'q' yazınız.")
    secim = input("Hangi işlemi yapmak istiyorsunuz? : ")

    if secim.lower() == 'q':
        break

    if secim == "1":
        kullanici_giris.tarih_gir()

    elif secim == "2":
        kisi_sil = input("Silmek istediğiniz kişi veya kurumu giriniz: ")
        tarih_sil = input("Silmek istediğiniz tarihi (Gün Ay Yıl) giriniz: ")
        kullanici_giris.olay_sil(kisi_sil, tarih_sil)
        print("Olay bilgileri silindi.")

    elif secim == "3":
        kullanici_giris.info()

    # To do in to do list:
    # inputs will be changeable and the date will be formatted automatically
    # search would be fine even with a single word