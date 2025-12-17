import math

def calculate_link_budget(tx_power_dbm, tx_gain_dbi, rx_gain_dbi, frequency_mhz, distance_km):
    """
    Calculates Link Margin using Friis Transmission Equation.
    """
    # Free Space Path Loss (FSPL)
    # FSPL(dB) = 20log10(d) + 20log10(f) + 32.44
    fspl = 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44
    
    # Received Power
    rx_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - fspl
    
    return rx_power_dbm, fspl

if __name__ == "__main__":
    print("📡 RF LINK BUDGET CALCULATOR")
    tx_p = float(input("Tx Power (dBm) [Example: 30 for 1W]: "))
    tx_g = float(input("Tx Antenna Gain (dBi) [Example: 2.1 for Dipole]: "))
    rx_g = float(input("Rx Antenna Gain (dBi) [Example: 10 for Yagi]: "))
    freq = float(input("Frequency (MHz) [Example: 433]: "))
    dist = float(input("Distance (km): "))
    sens = float(input("Rx Sensitivity (dBm) [Example: -120]: "))
    
    rx_p, loss = calculate_link_budget(tx_p, tx_g, rx_g, freq, dist)
    margin = rx_p - sens
    
    print(f"\nRESULTS:")
    print(f"Path Loss: {loss:.2f} dB")
    print(f"Received Power: {rx_p:.2f} dBm")
    print(f"Link Margin: {margin:.2f} dB")
    
    if margin > 10:
        print("✅ STRONG LINK (Good for Video)")
    elif margin > 3:
        print("⚠️ WEAK LINK (Telemetry Only)")
    else:
        print("❌ NO LINK (Signal Lost)")
