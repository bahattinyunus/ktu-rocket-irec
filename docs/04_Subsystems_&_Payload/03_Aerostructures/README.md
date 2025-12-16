# 🏗️ Yapısal Tasarım (Aerostructures) Bilgi Bankası

## 1. Malzeme Seçimi
Roket gövdesi için "Strength-to-Weight" (Mukavemet/Ağırlık) oranı her şeydir.

| Malzeme | Özellik | Kullanım Yeri | Notlar |
| :--- | :--- | :--- | :--- |
| **Fiberglass** | RF geçirgen, orta mukavemet, ucuz. | Burun konisi, Aviyonik Bay. | GPS sinyali geçer, boyanması kolaydır. |
| **Karbon Fiber** | Çok yüksek mukavemet, çok hafif. | Motor gövdesi, Kanatçıklar. | **RF Sinyalini Bloklar!** (Antenleri dışarı almalısınız). |
| **Alüminyum (6061-T6)** | İşlemesi kolay, dayanıklı. | Motor mount, Bulkheadler. | Metal işleme atölyesi gerektirir. |
| **Blue Tube 2.0** | Vulkanize fiber, çok dayanıklı. | Gövde tüpleri. | COTS roketler için standart. |

## 2. Kanatçık (Fin) Tasarımı
### 2.1. Stabilite (Static Margin)
Roketin ağırlık merkezi (CG), basınç merkezinin (CP) **önünde** olmalıdır.
$$ Margin = \frac{X_{cp} - X_{cg}}{D_{body}} $$
*   **Hedef:** 1.5 - 2.5 Kalibre arası.
*   **Aşırı Stabil (>4):** Rüzgara karşı dönme (Weather Cocking) riski artar.
*   **Düşük Stabil (<1):** Takla atma riski.

### 2.2. Flutter Analizi (Kritik!)
Kanatçıkların ses üstü hızlarda rezonansa girip parçalanması.
*   **Fin Thickness:** Yeterince kalın malzeme seçin.
*   **Fin Shape:** Tapered (sivrilen) kanatçıklar flutter'a daha dirençlidir.
*   **Tool:** AeroFinSim veya OpenRocket'in dahili analizini kullanın.

## 3. Üretim Teknikleri
*   **Vakum İnfüzyon:** Karbon fiber boru üretimi için en temiz yöntem.
*   **Fillet:** Kanatçık köklerine epoksi fillet atmak, yüzey alanını artırır ve kopmayı önler.
