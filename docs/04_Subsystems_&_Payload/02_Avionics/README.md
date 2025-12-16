# 📟 Aviyonik (Avionics) Bilgi Bankası

## 1. Sistem Mimarisi
IREC kuralları gereği **yedekli (redundant)** sistem şarttır.

### 1.1. SRAD vs COTS Dengesi
*   **Birinci Bilgisayar (Primary):** **SRAD** (Kendi tasarımınız). Puan getirir.
*   **İkinci Bilgisayar (Redundant):** **COTS** (Stratologger, R-DAS, TeleMega). Güvenliği garanti eder.
*   **Güç:** Her iki sistemin pili **tamamen ayrı** olmalıdır.

## 2. PCB Tasarım Kuralları (Design Rules)
Yüksek G kuvveti ve titreşim altında çalışacak kartlar için:
1.  **Konnektörler:** Asla standart "Dupont" kablo kullanmayın. **JST-XH, Molex** veya vidalı klemens (Screw Terminal) kullanın.
2.  **Montaj:** Büyük kapasitörleri ve ağır parçaları silikonla sabitleyin.
3.  **Ground Plane:** RF gürültüsü için en az 4 katmanlı PCB ve sağlam bir GND plane kullanın.

## 3. RF Link Bütçesi (Link Budget)
Telemetri verisini 10,000 ft'den almak için hesaplama:
$$ P_{rx} = P_{tx} + G_{tx} + G_{rx} - L_{path} - L_{loss} $$
*   **Ptx:** Verici Gücü (örn. 1W = 30dBm)
*   **Gtx/Grx:** Anten Kazançları
*   **Lpath:** Mesafe Kaybı (FSPL)

> **Öneri:** LoRa modülleri (915 MHz / 433 MHz) veya XBee Pro 900HP kullanın.

## 4. Sensör Listesi (BOM)
*   **IMU:** BNO055 (Fusion algoritmaları içinde), MPU6050
*   **Barometre:** BMP280, MS5611 (Yüksek hassasiyet)
*   **GPS:** uBlox NEO-M8N (Yüksek irtifa kilitlenmesi iyi)
