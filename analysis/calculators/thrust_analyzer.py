import matplotlib.pyplot as plt
import numpy as np

def analyze_thrust_curve(time_data, thrust_data):
    """
    Analyzes thrust curve data.
    """
    dt = np.diff(time_data)
    impulse = np.sum(thrust_data[:-1] * dt) # Riemann sum
    max_thrust = np.max(thrust_data)
    avg_thrust = np.mean(thrust_data)
    burn_time = time_data[-1] - time_data[0]
    
    return impulse, max_thrust, avg_thrust, burn_time

if __name__ == "__main__":
    print("🔥 MOTOR THRUST ANALYZER (Simulation)")
    
    # Generate dummy thrust curve (Trapezoidal)
    t = np.linspace(0, 4, 100)
    thrust = np.piecewise(t, 
                         [t < 0.5, (t >= 0.5) & (t < 3.5), t >= 3.5], 
                         [lambda x: x*2000, 1000, lambda x: 1000 - (x-3.5)*2000])
    thrust = np.clip(thrust, 0, None) # Remove negative values
    
    impulse, max_th, avg_th, burn = analyze_thrust_curve(t, thrust)
    
    # Class determination (e.g., M-class: 5120-10240 Ns)
    motor_class = "Unknown"
    if 5120 <= impulse < 10240: motor_class = "M"
    elif 2560 <= impulse < 5120: motor_class = "L"
    
    print(f"\nRESULTS:")
    print(f"Total Impulse: {impulse:.1f} Ns (Class: {motor_class})")
    print(f"Max Thrust: {max_th:.1f} N")
    print(f"Burn Time: {burn:.2f} s")
    
    plt.plot(t, thrust)
    plt.title(f"Thrust Curve | {impulse:.0f} Ns")
    plt.xlabel("Time (s)")
    plt.ylabel("Thrust (N)")
    plt.grid(True)
    plt.savefig("thrust_curve.png")
    print("📊 Graph saved as 'thrust_curve.png'")
