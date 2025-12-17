# 🔥 SRAD Motor Tasarım Cetveli (Propulsion Design Sheet)

> **UYARI:** Motor tasarımı sadece *Lead Propulsion Engineer* onayı ile üretilir.

## 1. Hedef Performans
*   **Toplam İtki (Total Impulse):** 8500 Ns (M-Class)
*   **Ortalama İtki:** 2100 N
*   **Yanma Süresi:** 4.1 saniye
*   **Max Chamber Pressure (MEOP):** 600 psi

## 2. Yakıt Geometrisi (Grain Geometry)
*   **Tip:** BATES Grain
*   **Yakıt:** APCP (Ammonium Perchlorate Composite Propellant)
*   **Grain Sayısı:** 4
*   **Dış Çap (OD):** 98 mm
*   **Core Çapı (ID):** 24 mm
*   **Uzunluk (L):** 140 mm (her biri)

## 3. Nozzle Tasarımı
*   **Boğaz Çapı (Dt):** 28 mm
*   **Çıkış Çapı (De):** 96 mm
*   **Expansion Ratio:** 11.75
*   **Malzeme:** İnce Gözlü Grafit (Fine Grain Graphite)

## 4. Kn Hesabı (Burn Area / Throat Area)
*   **Kn Başlangıç:** 340
*   **Kn Max:** 410
*   **Kn Bitiş:** 360
*   *> Kritik Sınır: 200'ün altı sönme, 550 üstü CATO riski.*

**Validasyon:** OpenMotor simülasyon dosyası: `analysis/data/motor_sim_v3.eng`
