# 🧪 Malzeme Özellikleri (Material Properties)

> **Mühendislik Verisi:** Analizlerde (ANSYS/OpenRocket) **BU DEĞERLERİ KULLANIN.** İnternetten rastgele değer almayın.

## 1. Metaller (Metals)

| Malzeme | Yoğunluk (g/cm³) | Yield Strength (MPa) | Young's Modulus (GPa) | Kullanım Alanı |
| :--- | :--- | :--- | :--- | :--- |
| **Alüminyum 6061-T6** | 2.70 | 276 | 68.9 | Motor Kovanı, Bulkhead, Avionics Bay |
| **Alüminyum 7075-T6** | 2.81 | 503 | 71.7 | Nozzle Tutucu, Yüksek Stresli Vidalar |
| **Çelik 304 (Paslanmaz)** | 8.00 | 215 | 193 | Cıvatalar, U-Boltlar, Yaylar |
| **Titanyum Grade 5** | 4.43 | 880 | 113.8 | SRAD Motor Parçaları (Çok pahalı/zor işlenir) |

## 2. Kompozitler (Composites)

| Malzeme | Yoğunluk (g/cm³) | Çekme Dayanımı (MPa) | Modulus (GPa) | Notlar |
| :--- | :--- | :--- | :--- | :--- |
| **Fiberglas (G10/FR4)** | 1.80 | 270 | 17 | Elektronik plakalar, Finler (Düşük Mach) |
| **Karbon Fiber (Pre-preg)**| 1.55 | 600 - 800* | 70 - 130* | *Lif yönüne göre değişir.* Gövde boruları. |
| **Karbon Fiber (Wet Layup)**| 1.45 | 300 - 500 | 50 - 70 | El üretimi. Hava kabarcığı riski yüksek. |

## 3. 3D Baskı (Plastics)

| Malzeme | Doluluk (%) | Dayanım (MPa) | Sıcaklık Dayanımı (HDT) | Kullanım Alanı |
| :--- | :--- | :--- | :--- | :--- |
| **PLA+** | %100 | 45 | 55°C | **ASLA KULLANMA** (Güneşte erir). |
| **PETG** | %40-100 | 50 | 75°C | Avionics Kızağı, Kamera Tutucu. |
| **ABS/ASA** | %100 | 40 | 95°C | Dış parçalar (UV dayanımı). |
| **Nylon (PA12)** | %100 | 60 | 140°C | Mekanik parçalar, Yüksek darbe emilimi. |

> **NOT:** Cıvata tork değerleri için `docs/03_Safety_&_SRAD/Checklists/01_Assembly.md` dosyasına bakınız.
