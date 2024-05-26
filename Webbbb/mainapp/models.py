from django.db import models

class Vatandas(models.Model):
    Ad = models.CharField(max_length=50)
    Soyad = models.CharField(max_length=50)
    DogumTarihi = models.DateField()
    Cinsiyet = models.CharField(max_length=10)
    TelefonNumarasi = models.CharField(max_length=20)
    Adres = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Ad} {self.Soyad}"

class Yetkili(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Yonetici(models.Model):
    def __str__(self):
        return f"Yonetici {self.pk}"

class Sifreler(models.Model):
    user = models.ForeignKey(Vatandas, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user_id}"

class Fotolar(models.Model):
    vatandas = models.ForeignKey(Vatandas, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f"Fotoğraf # {self.foto} {self.vatandas}"



class Randevu(models.Model):
    Vatandas = models.ForeignKey(Vatandas, on_delete=models.CASCADE)
    Yetkili = models.ForeignKey(Yetkili, on_delete=models.CASCADE)
    Konu = models.CharField(max_length=255)
    Tarih = models.CharField(max_length=255)
    Saat = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.Vatandas.Ad} {self.Vatandas.Soyad} - {self.Konu}'


class Rapor(models.Model):
    RaporTarihi = models.DateField()
    RaporIcerigi = models.TextField()
    Vatandas = models.ForeignKey(Vatandas, on_delete=models.CASCADE)
    Yetkili = models.ForeignKey(Yetkili, on_delete=models.CASCADE)
    Yonetici = models.ForeignKey(Yonetici, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rapor {self.pk}"

class Bildirim(models.Model):
    Vatandas = models.ForeignKey(Vatandas, on_delete=models.CASCADE)
    Yetkili = models.ForeignKey(Yetkili, on_delete=models.CASCADE)
    Icerik = models.TextField()
    OkunduMu = models.BooleanField(default=False)
    Tarih = models.CharField(max_length=255)

    def __str__(self):
        return f"Bildirim {self.pk}"
