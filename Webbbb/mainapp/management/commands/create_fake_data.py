from django.core.management.base import BaseCommand
from faker import Faker
from mainapp.models import Vatandas, Yetkili, Yonetici, Sifreler, Randevu, Rapor
import random

class Command(BaseCommand):
    help = 'Create fake data'

    def handle(self, *args, **kwargs):
        fake = Faker('tr_TR')

        # Mevcut verileri sil
        Vatandas.objects.all().delete()
        Yetkili.objects.all().delete()
        Yonetici.objects.all().delete()
        Sifreler.objects.all().delete()
        Randevu.objects.all().delete()
        Rapor.objects.all().delete()

        # Yönetici oluştur
        yonetici = Yonetici.objects.create()

        for _ in range(100):
            vatandas = Vatandas.objects.create(
                Ad=fake.first_name(),
                Soyad=fake.last_name(),
                DogumTarihi=fake.date_of_birth(minimum_age=18, maximum_age=100),
                Cinsiyet=random.choice(["Erkek", "Kadın"]),
                TelefonNumarasi=fake.phone_number()[:20],
                Adres=fake.address()
            )

            Sifreler.objects.create(
                user_id=vatandas.id,
                password=fake.password(6)
            )

        for _ in range(10):
            yetkili = Yetkili.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                specialization=fake.job(),
                department=fake.company()
            )

            Sifreler.objects.create(
                user_id=yetkili.id,
                password=fake.password(6)
            )

        konular = [
            'Vize Başvuru Formu Doldurma Yardımı',
            'Pasaport Yenileme İşlemleri',
            'Vize Başvuru Ücreti Ödeme Talimatları',
            'Pasaport Fotoğrafı Çekimi ve Standartları',
            'Vize Görüşmesine Hazırlık',
            'Pasaport Teslim Alma ve Teslim Etme Süreçleri',
            'Online Vize Başvurusu İçin Teknik Destek',
            'Vize Randevu Tarihi ve Saati Değişikliği',
            'Pasaport Kaybı ve Yeniden Çıkarma İşlemleri',
            'Vize Başvuru Belgeleri Doğrulama',
            'Pasaport Yenileme İçin Gerekli Belgeler',
            'Vize Başvurusu İçin Ek Belgeler Temini',
            'Pasaport Ücret İadesi ve İptali',
            'Vize Başvurusu İçin Sağlık Sigortası Bilgilendirmesi',
            'Pasaport Başvurusu İçin Biyometrik Veri Toplama',
            'Vize Başvurusu İçin Konsolosluk Görüşmeleri',
            'Pasaport Başvuru Sürecinin Takibi',
            'Vize Başvuru Formu Kontrol ve Onayı',
            'Pasaport Çıkarma İşlemleri İçin Randevu',
            'Vize Başvurusu İçin Dil Testi Bilgilendirmesi',
            'Pasaport Teslim Alma İçin Randevu',
            'Vize Başvurusu İçin Davet Mektubu Hazırlama',
            'Pasaport Çıkış Süresi Hakkında Bilgi',
            'Vize Başvurusu İçin Banka Dekontu Hazırlama',
            'Pasaport Başvuru Ücretleri ve Ödeme Yöntemleri'
        ]

        for _ in range(100):
            randevu_tarihi = fake.date_between(start_date='today', end_date='+1y')
            randevu_saati = fake.time_object()

            Randevu.objects.create(
                Vatandas=random.choice(Vatandas.objects.all()),
                Yetkili=random.choice(Yetkili.objects.all()),
                Konu=random.choice(konular),  # Rastgele bir konu seç
                Tarih=randevu_tarihi,
                Saat=randevu_saati
            )

        for _ in range(100):
            Rapor.objects.create(
                RaporTarihi=fake.date_between(start_date='-1y', end_date='today'),
                RaporIcerigi=fake.text(),
                Vatandas=random.choice(Vatandas.objects.all()),
                Yetkili=random.choice(Yetkili.objects.all()),
                Yonetici=yonetici
            )

        self.stdout.write(self.style.SUCCESS('Successfully created fake data'))
