# Python 3.11 görüntüsünü kullan
FROM python:3.12

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Portu aç
EXPOSE 8000

# Django komutları
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Uygulama sunucusunu çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
