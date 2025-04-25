# Skyscanner Scraper (GPT Uyumlu)

Bu proje, Playwright kullanarak Skyscanner uçuş arama sonuçlarını çekmek için hazırlanmıştır.
Flask üzerinden çalışan bir API sunar ve GPT gibi sistemlerle entegre çalışmak üzere tasarlanmıştır.

## Kullanım

1. Gerekli kütüphaneleri kurun:
```
pip install -r requirements.txt
playwright install
```

2. Sunucuyu başlatın:
```
python app.py
```

3. API endpoint:
```
http://localhost:5000/ucus-bilgisi?from=DXB&to=IST&date=15/05/2025
```