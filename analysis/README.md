# 📂 Analysis & Simulation (Analiz ve Simülasyon)

Bu klasör, roketin uçuş dinamiği, aerodinamik ve yapısal analizleri için kullanılan araçları ve kodları içerir.

## 🛠️ Kurulum (RocketPy)

Bu repo, gelişmiş 6-DOF yörünge simülasyonları için **RocketPy** kütüphanesini kullanır.

### Gereksinimler
Python 3.8+ gereklidir. Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt
```

## 🚀 Simülasyon Çalıştırma

Örnek bir uçuş simülasyonu çalıştırmak için:

```bash
python example_sim.py
```

## 📂 Klasör Yapısı
*   `calculators/`: Mühendislik hesap araçları.
    *   `parachute_sizing.py`: İniş hızı ve paraşüt çapı hesabı.
    *   `link_budget.py`: RF Telemetri menzil ve marjin analizi.
    *   `thrust_analyzer.py`: Motor itki eğrisi analizi ve Total Impulse hesabı.
*   `data/`: Motor itki verileri (.eng) ve aerodinamik katsayılar (.csv).
*   `notebooks/`: Detaylı analizler için Jupyter Notebook'lar.
*   `results/`: Simülasyon çıktıları ve grafikler.
