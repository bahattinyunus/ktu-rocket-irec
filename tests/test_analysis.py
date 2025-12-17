import sys
import os
import unittest
import pandas as pd
import numpy as np

# 'analysis' klasörünü path'e ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.post_flight_analysis import analyze_flight_data

class TestFlightAnalysis(unittest.TestCase):
    def setUp(self):
        # Test için geçici bir CSV oluştur
        self.test_file = "test_flight_data.csv"
        time = np.linspace(0, 10, 100)
        altitude = time * 10 # Basit lineer artış
        df = pd.DataFrame({'Time': time, 'Altitude_AGL': altitude})
        df.to_csv(self.test_file, index=False)

    def test_analysis_runs(self):
        # Fonksiyonun hata vermeden çalıştığını test et
        try:
            analyze_flight_data(self.test_file)
        except Exception as e:
            self.fail(f"analyze_flight_data raised Exception unexpectedly: {e}")

    def tearDown(self):
        # Temizlik
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists("flight_profile.png"):
            os.remove("flight_profile.png")

if __name__ == '__main__':
    unittest.main()
