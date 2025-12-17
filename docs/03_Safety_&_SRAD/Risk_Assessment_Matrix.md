# 🛡️ Tehlike Analizi ve Risk Değerlendirmesi (Hazard Analysis)

> [!IMPORTANT]
> Bu döküman, IREC kuralları gereği **Spaceport America Cup Safety Officer** tarafından incelenecektir. Ciddiyetle doldurun.

![Banner](../../assets/banner.png)

## Risk Matrisi (Risk Matrix)
Risk Skoru = (Olasılık) x (Şiddet)
*   **1-4 (Yeşil):** Kabul Edilebilir.
*   **5-9 (Sarı):** Dikkat Gerektirir (Azaltma zorunlu).
*   **10-25 (Kırmızı):** Kabul Edilemez (Tasarım değişikliği zorunlu).

| ID | Tehlike (Hazard) | Olasılık (1-5) | Şiddet (1-5) | Risk (P x S) | Azaltma Yöntemi (Mitigation) | Son Risk | Sorumlu |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **PR-01** | Motorun rampada patlaması (CATO) | 3 | 5 | **15 (Kırmızı)** | E-match süreklilik testi (Low current), Rampadan 500m uzakta olma, Motor gömleğinin (Casing) hidrostatik testi. | **5 (Sarı)** | İtki Lideri |
| **AV-01** | Uçuş bilgisayarının kilitlenmesi | 2 | 5 | **10 (Kırmızı)** | Watchdog Timer aktif, Bağımsız yedek bilgisayar (Redundancy), Yer testleri. | **2 (Yeşil)** | Aviyonik Lideri |
| **RC-01** | Paraşütün açılmaması (Ballistic Re-entry) | 2 | 5 | **10 (Kırmızı)** | Çift fünye (Dual E-match), Yedek (Backup) barut haznesi, Enerjik Testler. | **2 (Yeşil)** | Kurtarma Lideri |
| **STR-01** | Fin Flutter (Kanatçık kopması) | 2 | 4 | **8 (Sarı)** | OpenRocket ve Ansys flutter analizi, Karbon fiber kaplama, Rijitlik testi. | **2 (Yeşil)** | Yapısal Lideri |
| **PAY-01** | Faydalı yük pilinin akması | 3 | 2 | **6 (Sarı)** | LiPosuz güvenli pil kullanımı veya yanmaz kese (LiPo Bag). | **2 (Yeşil)** | Payload Sorumlusu |

## Personel Güvenliği
1.  **KKD (PPE):** Her motor montajında gözlük ve eldiven zorunludur.
2.  **Rampa Disiplini:** Rampa "ARMED" iken kimse 10m yakınına yaklaşamaz.
3.  **Sıcaklık:** Piller 60°C üzerinde doğrudan güneş ışığında bırakılmamalıdır (Çöl sıcağı).
