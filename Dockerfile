# 1. Python ortamını seç
FROM python:3.10

# 2. Çalışma dizinini belirle
WORKDIR /app

# 3. Tüm dosyaları kopyala
COPY . /app

# 4. Gerekli paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Flask’in kullanacağı portu belirt
EXPOSE 7860

# 6. Uygulamayı başlat (Flask + Gunicorn)
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
