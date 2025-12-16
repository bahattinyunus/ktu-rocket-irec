# 🪂 Kurtarma Sistemi (Recovery) Bilgi Bankası

## 1. Dual Deployment (Çift Aşamalı Kurtarma)
Yüksek irtifa roketlerinde standarttır. Tek paraşütle inerseniz roket rüzgarla kilometrelerce sürüklenir.

1.  **Drogue (Sürüklenme) Paraşütü:** Apogee'de (tepe noktası) açılır. Roketi stabilize eder ve hızlı (tercihen 20-30 m/s) düşüş sağlar.
2.  **Main (Ana) Paraşüt:** Belirlenen irtifada (örn. 1,000 ft) açılır. Yumuşak iniş (5-7 m/s) sağlar.

## 2. Paraşüt Boyutlandırma
İniş hızı hesabı:
$$ V_{descent} = \sqrt{\frac{2 m g}{\rho C_d A}} $$
*   **m:** Roket kütlesi
*   **Cd:** Sürüklenme katsayısı (Düz paraşüt için ~1.5, Eliptik için ~2.2)
*   **A:** Paraşüt alanı

## 3. Barut Miktarı Hesabı (Ejection Charge)
Ayrılma için ne kadar barut (Black Powder) gerekir?
$$ F (lbs) = P (psi) \times Area (in^2) $$
*   Genel kural: İç basıncı **15-20 PSI** yapacak kadar barut.
*   **Hesaplayıcı:** [NASA Ejection Charge Calculator](https://www.nakka-rocketry.net/eject.html) kullanın.
*   **UYARI:** Mutlaka yer testi (Ground Test) yapın!

## 4. Shear Pins (Kesme Pimleri)
Burnun erken açılmasını (Drag Separation) engellemek için naylon vidalar kullanılır. Barut patlayınca bu vidalar kesilir.
*   **2-56 Nylon Screw:** Genelde 3-4 adet yeterlidir.
