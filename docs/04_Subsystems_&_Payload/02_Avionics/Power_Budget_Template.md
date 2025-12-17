# 🔋 Avionics Power Budget (Güç Bütçesi)

> **KURAL:** Piller, hesaplanan tüketimin en az **2.5 katı (Safety Factor > 2.5)** kapasiteye sahip olmalıdır.

## 1. Tüketim Tablosu (Consumption Table)

| Bileşen (Component) | Voltaj (V) | Çekilen Akım (mA) | Adet | Toplam Güç (mW) | Notlar |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flight Computer** | 3.3V | 150 mA | 1 | 495 mW | CPU Full Load |
| **GPS Modülü** | 3.3V | 70 mA | 1 | 231 mW | Lock Mode |
| **Telemetri (LoRa)** | 5.0V | 500 mA | 1 | 2500 mW | @ 1 Watt Tx |
| **Servo Motor 1** | 7.4V | 1200 mA | 1 | 8880 mW | Stall Current |
| **Buzzer** | 5.0V | 30 mA | 1 | 150 mW | - |
| **Status LEDs** | 3.3V | 20 mA | 3 | 198 mW | - |
| **TOPLAM (Peak)** | - | **~2.0 A** | - | **~12.5 W** | - |

## 2. Pil Seçimi (Battery Selection)
*   **Pil Tipi:** Li-Po 2S (7.4V)
*   **Kapasite:** 2200 mAh
*   **C-Rating:** 25C (Max Anlık Akım: 55A) - *Yeterli*

## 3. Ömür Hesabı (Runtime Calculation)
*   **Ortalama Akım:** 600 mA (Servo beklemede)
*   **Teorik Ömür:** $2200 mAh / 600 mA = 3.66 Saat$
*   **Güvenli Ömür (x0.7):** **2.56 Saat**

> **SONUÇ:** Fırlatma penceresi 1 saat olduğu için bu pil YETERLİDİR.
