# 🚀 İtki Sistemi (Propulsion) Bilgi Bankası

## 1. Temel Kavramlar & Formüller
Motor tasarımında kullanılan "Kutsal" denklemler.

### 1.1. Toplam İtki (Total Impulse)
Roketin sınıfını belirleyen temel değer.
$$ I_{total} = \int_{0}^{t_{burn}} F(t) dt $$
*   **M-Class:** 5,120 - 10,240 Ns
*   **L-Class:** 2,560 - 5,120 Ns

### 1.2. Özgül İtki (Specific Impulse - $I_{sp}$)
Motor verimliliğinin ölçüsü.
$$ I_{sp} = \frac{F}{\dot{m} g_0} $$
*   **Katı Yakıt (APCP):** 200-260 sn
*   **Hibrit (N2O/Paraffin):** 220-290 sn

## 2. Motor Seçimi (Trade-off Analizi)

| Tip | Avantaj | Dezavantaj | IREC Önerisi |
| :--- | :--- | :--- | :--- |
| **COTS (Hazır)** | %99 Güvenilirlik, Kolay montaj. | Puan getirisi düşük, Pahalı (Cesaroni L2200 gibi). | **10k feet için** ideal. Riski minimize eder. |
| **SRAD (Katı)** | Yüksek puan, Tam kontrol. | Üretim tesisi/izni gerekir. Patlama riski. | Zorunlu değilse **kaçının**. |
| **SRAD (Hibrit)** | "Mühendislik Harikası", Güvenli (Patlamaz). | Vana/Tank sistemleri çok karmaşık. Yer testi zordur. | **30k için** en iyi seçenek. |

## 3. Üretim & Test Kontrol Listesi
### Katı Motor (Varsa)
1.  [ ] Grain Casting: Vakum altında döküm yapıldı mı? (Baloncuk = Patlama)
2.  [ ] Liner Bonding: İzolasyon ile yakıt yapıştı mı?
3.  [ ] Nozzle Erosion: Grafit kalitesi yeterli mi?

### Hibrit Motor
1.  [ ] Hidrotest: Tank basınca dayanıyor mu? (Çalışma basıncının 1.5 katı)
2.  [ ] Soğuk Akış (Cold Flow): Oksitleyici akışı düzgün mü?
3.  [ ] Ateşleme Sistemi: Uzaktan (100m) kontrol çalışıyor mu?

## 4. Referans Kaynaklar
*   **Nakka Rocketry:** [Richard Nakka's Solid Rocket Motor Theory](https://www.nakka-rocketry.net/)
*   **Rocket Propulsion Elements (Sutton):** Roketçilerin İncil'i.
