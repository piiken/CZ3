# 🐍 Używamy oficjalnego obrazu Pythona
FROM python:3.11

# 📂 Ustawiamy katalog roboczy
WORKDIR /app

# 🏗 Kopiujemy pliki aplikacji do kontenera
COPY . .

# 🛠 Instalujemy zależności z requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 🎬 Uruchamiamy aplikację
CMD ["python", "main.py"]
