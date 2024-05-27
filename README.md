# Vatandaş Randevu Sistemi Projesi

Bu proje, vatandaşların devlet yetkililerinden randevu almasını sağlayan bir platform geliştirmeyi amaçlamaktadır. Proje, modern web teknolojileri ve çeşitli yazılım mimarisi prensipleri kullanılarak geliştirilmiştir. Bu dökümantasyon, projenin her katmanını ve kullanılan teknolojileri ayrıntılı bir şekilde açıklamaktadır.

![1image](https://github.com/OGskrrt/Akilli-Randevu-Sistemi/assets/90643276/2e13b66a-72e5-4b8e-bc00-17c76c742483)
<div align="center">
  <img src="https://github.com/OGskrrt/Akilli-Randevu-Sistemi/assets/90643276/b9e6ce9d-3c74-4738-ab48-4ca418b32539" alt="Açıklama" width="400" height="400">
</div>

## Docker
Proje Docker ile uyumlu olarak çalışmaktadır. Güncel olarak containerized haldedir. 
   ```shell
       docker-compose up
   ```
komutu ile direkt olarak docker üzerinden projeyi çalıştırabilirsiniz. 
# Branch Özgür : 
### --- Presentation Layer: UI Framework Kullanımı ---

**İster:** Vatandaşlar, kişisel bilgilerini ve tercihlerini yönetebilecekleri ve devlet yetkililerinden randevu alabilecekleri bir UI Framework kullanılarak oluşturulmuş sunum katmanına sahip bir platform geliştirilecek.

**Uygulama:**
- **Kullanılan Teknolojiler:** Bootstrap ve Django Templates.
- **UI Özellikleri:** Vatandaşlar, kayıt olduktan sonra kişisel profil sayfalarına erişebilirler. Profil sayfalarında kişisel bilgilerini güncelleyebilir, randevularını görüntüleyebilir ve yeni randevular alabilirler.
- **Responsive Tasarım:** Bootstrap kullanılarak mobil ve masaüstü cihazlarda sorunsuz çalışan, duyarlı bir arayüz tasarlandı.

### --- Cloud Service (AI) Using ---

**İster:** Bulut tabanlı hizmetler, yapay zeka kullanarak öneriler sunacak ve vatandaşların hedeflerine ulaşmalarına yardımcı olacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Gemini API.
- **Yapay Zeka:** Vatandaşların randevu alım sürecini iyileştirmek için yapay zeka entegre edildi. Gemini API kullanılarak NLP (Doğal Dil İşleme) ile vatandaşlarla etkileşim sağlandı ve öneriler sunuldu.

###  --- Web Security Implementation ---

**İster:** Web güvenliği implementasyonu, kullanıcı verilerinin gizliliği ve güvenliği için SSL şifrelemesi, veri doğrulama ve diğer güvenlik önlemlerini sağlayacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Django, SSL/TLS.
- **Güvenlik Önlemleri:** Kullanıcı verilerinin korunması için SSL şifrelemesi, veri doğrulama, güçlü parola politikaları ve diğer güvenlik önlemleri uygulandı.
# Branch Onur : 
### --- Business Layer: OOP Bileşenleri ---

**İster:** OOP bileşenleriyle desteklenen iş katmanı, vatandaşların randevu almasını ve devlet yetkililerinin bu randevuları yönetmesini sağlayacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Python ve Django.
- **OOP Prensipleri:** Sınıflar, metodlar ve arayüzler kullanılarak modüler ve sürdürülebilir bir yapı oluşturuldu.
- **İş Mantığı:** Vatandaşlar için randevu oluşturma, yönetme ve devlet yetkilileri için randevuları onaylama ve düzenleme işlevleri OOP bileşenleri ile yönetildi.

### --- Data Layer: ORM / Migrations Kullanımı ---

**İster:** Veri katmanında, ORM ve migrations kullanılarak vatandaş bilgileri ve randevular güvenli bir şekilde saklanacak ve yönetilecek.

**Uygulama:**
- **Kullanılan Teknolojiler:** Django ORM ve SQLite.
- **Veritabanı Yönetimi:** Vatandaş bilgileri, randevular ve devlet yetkililerinin bilgileri ORM kullanılarak yönetildi.
- **Migrations:** Veritabanı şemasındaki değişiklikler için Django migrations kullanıldı.

### --- Web Service Implementation ---

**İster:** Web servisleri implementasyonunda, vatandaşlar ve devlet yetkilileri arasında iletişimi sağlayacak ve randevu işlemlerini güvenli bir şekilde gerçekleştirebilecekleri bir sistem oluşturulacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Django Rest Framework (DRF).
- **RESTful API:** Vatandaşlar ve devlet yetkilileri arasında iletişim sağlamak için RESTful API'ler geliştirildi. API'ler, vatandaşların randevularını yönetmelerine ve yetkililerin bu randevuları onaylamalarına olanak tanır.

### --- Authorization Implementation ---

**İster:** Oturum ve çerez yönetimi, kullanıcıların oturumlarını güvenli bir şekilde yönetmelerini ve site üzerindeki etkileşimlerini takip etmelerini sağlayacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** JWT (JSON Web Tokens).
- **Oturum Yönetimi:** Kullanıcıların güvenli bir şekilde oturum açmaları ve kapatmaları için JWT kullanıldı.
- **Çerez Yönetimi:** Kullanıcı etkileşimlerini izlemek ve kişiselleştirilmiş deneyimler sunmak için çerezler kullanıldı.

# Branch Emre :
### --- RBAC Implementation ---

**İster:** RBAC ve yetkilendirme implementasyonu, kullanıcıların erişim haklarını ve rollerini yönetmeye olanak tanıyacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Django'nun yerleşik yetkilendirme sistemi.
- **Rol ve İzin Yönetimi:** Vatandaşlar, yetkililer ve yöneticiler için farklı roller ve izinler tanımlandı. Her rol, belirli kaynaklara erişim ve işlem yapma yetkisine sahiptir.

### --- Session / Cookie Management ---

**İster:** Oturum ve çerez yönetimi, kullanıcıların oturumlarını güvenli bir şekilde yönetmelerini ve site üzerindeki etkileşimlerini takip etmelerini sağlayacak.

**Uygulama:**
- **Kullanılan Teknolojiler:** Django Sessions ve Cookies.
- **Oturum Yönetimi:** Kullanıcı oturum bilgileri Django'nun session framework'ü ile yönetildi.
- **Çerezler:** Kullanıcı tercihleri ve oturum bilgileri çerezler aracılığıyla saklandı.

### --- Extension / Third Party Library Using ---

**İster:** Uzantılar ve üçüncü taraf kütüphaneler, dosya işleme, randevu işlemleri ve diğer işlevleri destekleyecek ve geliştirecek.

**Uygulama:**
- **Kullanılan Kütüphaneler:** Faker, Pillow.
- **Dosya İşleme:** Kullanıcı profil resimleri ve diğer medya dosyaları için Pillow kullanıldı.
- **Randevu İşlemleri:** Randevuların yönetimi için Django Rest Framework kullanıldı.

## Örnek Yetkili ve Vatandaş giriş bilgileri

### Yönetici
| Username  | Password |
| ------------- | ------------- |
| onur  | 1234  |

### Yetkili
| Username  | Password |
| ------------- | ------------- |
| 308  | @g9mGw  |
| 305  | !3CQzH  |

### Vatandaş
| Username  | Password |
| ------------- | ------------- |
| 5096  | #0X_Mk  |
| 5079  | y*1Hvt  |
| 5058  | #d7K4m  |
| 5017  | (4Prj_  |

## Güvenlik Uyarısı

Proje geliştirme aşamasında bazı güvenlik ayarları kapalı tutulmuştur. Canlı ortama geçmeden önce aşağıdaki güvenlik önlemlerinin alınması gerekmektedir:

1. *DEBUG Modunun Kapatılması:* Debug modu 'True' olarak bırakılmıştır. Güvenlik için DEBUG = False olarak ayarlanmalıdır.
2. *Güçlü Parola Politikalarının Uygulanması:* Kullanıcı parolalarının güçlü ve karmaşık olmasına dikkat edilmelidir.
3. *SSL/TLS Entegrasyonu:* Kullanıcı verilerinin güvenliğini sağlamak için SSL/TLS şifrelemesi kullanılmalıdır. Bunun için aşağıdaki komut ile HTTPS protokolü kullanılabilir:
    bash
   ```shell
       python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:8000
   ```
    
    Bu komut ile çalıştırılan sertifikanın şifresi 1234 olarak ayarlanmıştır.
5. *Veri Doğrulama ve Temizleme:* Kullanıcıdan gelen verilerin doğrulanması ve temizlenmesi sağlanmalıdır.
6. *Güncel Güvenlik Yama ve Güncellemelerinin Uygulanması:* Kullanılan tüm kütüphane ve yazılımların güncel güvenlik yamalarının uygulanması gerekmektedir.
7. *İzin verilen Hostlar* ALLOWED_HOSTS = ['*'] ile tüm host isimlerine izin verilmiştir. Güvenliği arttırmak için izin verilen host isimleri değiştirilmelidir.
8. *Siber Güvenlik Saldırı Ayarları* Setting.py dosyasının içinde 234. satırdan itibaren yorum satırına alınmış güvenlik önlemleri bulunmaktadır. Her ayarın açıklaması bulunmaktadır. Buradaki ayarlar açılarak güvenlik arttırılmalıdır. Bu ayarların açılmasıyla birlikte proje dosyası 3. maddede belirtilen komut ile başlatılmalıdır.
9. *Gemini API Kullanımı:* Gemini API'nin çalışması için gemini_key.txt dosyasının içine Gemini API anahtarının yazılması gerekmektedir.

Bu proje, modern web geliştirme standartlarına uygun olarak tasarlanmış ve kullanıcı dostu bir platform sağlamayı amaçlamaktadır. Yukarıdaki yönergeler ve açıklamalar, projenin her bir katmanını ve kullanılan teknolojileri ayrıntılı olarak açıklamaktadır.
