import math

def calculate_parachute_diameter(mass_kg, target_descent_rate_mps, cd=1.5):
    """
    Calculates required parachute diameter.
    :param mass_kg: Recovery mass (Rocket + Payload - Motor Fuel)
    :param target_descent_rate_mps: Desired landing speed (usually 6-8 m/s)
    :param cd: Drag Coefficient (1.5 for flat circular, 2.2 for elliptical)
    """
    rho = 1.225 # Air density at sea level (kg/m^3)
    
    # Area = (2 * m * g) / (rho * Cd * v^2)
    g = 9.81
    area = (2 * mass_kg * g) / (rho * cd * target_descent_rate_mps**2)
    
    # Diameter = sqrt(4 * Area / pi)
    diameter = math.sqrt(4 * area / math.pi)
    
    return diameter, area

if __name__ == "__main__":
    print("🪂 PARACHUTE SIZING CALCULATOR")
    m = float(input("Rocket Mass (kg): "))
    v = float(input("Target Descent Rate (m/s) [Rec: 6.0]: ") or 6.0)
    cd = float(input("Drag Coefficient [Rec: 1.5]: ") or 1.5)
    
    dia, area = calculate_parachute_diameter(m, v, cd)
    
    print(f"\nRESULTS:")
    print(f"Required Area: {area:.2f} m²")
    print(f"Required Diameter: {dia:.2f} m ({dia*3.28084:.2f} ft)")
    print(f"Impact Energy: {0.5 * m * v**2:.1f} Joules (Human leg breaks at ~60J)")
