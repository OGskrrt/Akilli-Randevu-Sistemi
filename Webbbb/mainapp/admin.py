# mainapp/admin.py

from django.contrib import admin
from .models import Vatandas, Yetkili, Yonetici, Sifreler, Randevu, Rapor, Bildirim, Fotolar

admin.site.register(Vatandas)
admin.site.register(Yetkili)
admin.site.register(Yonetici)
admin.site.register(Sifreler)
admin.site.register(Fotolar)
admin.site.register(Randevu)
admin.site.register(Rapor)
admin.site.register(Bildirim)


class VatandasAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

class YetkiliAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'department')
    search_fields = ('first_name', 'last_name', 'specialization', 'department')

class SifrelerAdmin(admin.ModelAdmin):
    list_display = ('user', 'password')
    search_fields = ('user',)

class RandevuAdmin(admin.ModelAdmin):
    list_display = ('id', 'vatandas', 'yetkili', 'tarih', 'saat', 'konu')
    search_fields = ('vatandas__first_name', 'vatandas__last_name', 'yetkili__first_name', 'yetkili__last_name', 'tarih', 'konu')

class TibbiRaporAdmin(admin.ModelAdmin):
    list_display = ('id', 'rapor_tarihi', 'rapor_icerigi', 'vatandas', 'yetkili')
    search_fields = ('vatandas__first_name', 'vatandas__last_name', 'yetkili__first_name', 'yetkili__last_name', 'rapor_icerigi')