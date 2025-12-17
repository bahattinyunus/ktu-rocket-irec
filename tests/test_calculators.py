import unittest
import sys
import os

# Add analysis path to sys.path to allow importing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../analysis')))

from calculators.parachute_sizing import calculate_parachute_diameter
from calculators.link_budget import calculate_link_budget

class TestEngineeringTools(unittest.TestCase):

    def test_parachute_sizing(self):
        # Case: 20kg mass, 6 m/s descent
        # Area = (2*20*9.81)/(1.225*1.5*36) = 392.4 / 66.15 = 5.93 m^2
        # Dia = sqrt(4*5.93/pi) = 2.74 m
        dia, area = calculate_parachute_diameter(mass_kg=20, target_descent_rate_mps=6.0, cd=1.5)
        self.assertAlmostEqual(dia, 2.74, places=1)
        self.assertAlmostEqual(area, 5.93, places=1)

    def test_link_budget(self):
        # Case: 433 MHz, 10 km
        # FSPL = 20log(10) + 20log(433) + 32.44
        # FSPL = 20 + 52.73 + 32.44 = 105.17 dB
        rx_p, loss = calculate_link_budget(tx_power_dbm=30, tx_gain_dbi=2, rx_gain_dbi=10, frequency_mhz=433, distance_km=10)
        
        expected_fspl = 105.17
        expected_rx = 30 + 2 + 10 - expected_fspl # -63.17 dBm
        
        self.assertAlmostEqual(loss, expected_fspl, places=1)
        self.assertAlmostEqual(rx_p, expected_rx, places=1)

if __name__ == '__main__':
    unittest.main()
