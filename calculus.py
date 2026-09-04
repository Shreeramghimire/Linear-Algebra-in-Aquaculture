# Aquaculture Data Analysis: Riemann Sums vs. The FTC

### Scenario

We are managing a **Recirculating Aquaculture System (RAS)** for raising Atlantic Salmon. We have:
1. **Sensor data** measuring oxygen consumption rate every 2 hours for a 24-hour period.
2. A **mathematical model** for fish growth rate over a 120-day grow-out period.

**Our Tasks:**
1. Estimate total oxygen consumed in 24 hours using a Riemann sum.
2. Calculate the exact oxygen consumption using a fitted model and the FTC.
3. Predict the total biomass of a single fish at harvest using the FTC.
4. Visualize the data and the accumulated totals.



### Cell 1: Import Required Libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid
from scipy.integrate import quad
import sympy as sp
from sympy import symbols, integrate, lambdify

# Enable inline plotting for Jupyter
%matplotlib inline

# Set style for better plots
plt.style.use('seaborn-v0_8-whitegrid')
print("Libraries imported successfully!")


### Cell 2: Riemann Sum with Synthetic Sensor Data
# Define the data
time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
consumption_rate = np.array([0.0, 0.8, 1.5, 2.1, 2.6, 3.0, 3.2, 3.1, 2.8, 2.3, 1.7, 0.9, 0.0])

# Width of each subinterval (hours)
delta_t = 2
n_subintervals = len(time) - 1

# Right Riemann Sum: use rates at indices 1 through 12 (the right endpoints)
right_endpoints = consumption_rate[1:]  # Skip the first value at t=0
right_riemann_sum = delta_t * np.sum(right_endpoints)

print(f"Number of subintervals: {n_subintervals}")
print(f"Width of each subinterval: {delta_t} hours")
print(f"Right Riemann Sum estimate of total oxygen consumed: {right_riemann_sum:.2f} mg/L")

### Cell 3: Visualize the Riemann Sum Rectangles

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the actual data points
ax.plot(time, consumption_rate, 'bo-', label='Sensor Data', linewidth=2, markersize=8)

# Plot the right Riemann sum rectangles 
for i in range(1, len(time)):
    x_left = time[i-1]
    x_right = time[i]
    y_height = consumption_rate[i]  # Right endpoint value
    ax.add_patch(plt.Rectangle((x_left, 0), delta_t, y_height, 
                               facecolor='red', alpha=0.3, edgecolor='red'))

# Formatting
ax.set_xlabel('Time (hours)', fontsize=12)
ax.set_ylabel('Oxygen Consumption Rate (mg/L per hour)', fontsize=12)
ax.set_title('Right Riemann Sum Approximation (12 Subintervals)', fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 25)
ax.set_ylim(0, 3.5)

plt.tight_layout()
plt.show()

Cell 4: Exact Integration Using FTC 

# Fit a smooth cubic to the sensor data itself, rather than picking coefficients
# by hand — an unfitted model can drift below zero (an unphysical negative
# consumption rate) and give a nonsensical, even negative, definite integral.
fit_coeffs = np.polyfit(time, consumption_rate, 3)

def consumption_model(t):
    return np.polyval(fit_coeffs, t)

# Use scipy's quad function to find the definite integral 
exact_total, error = quad(consumption_model, 0, 24)

print(f"Fitted model coefficients (t^3, t^2, t^1, t^0): {fit_coeffs}")
print(f"Exact total oxygen consumed (using FTC / numerical integration): {exact_total:.2f} mg/L")
print(f"Right Riemann Sum estimate: {right_riemann_sum:.2f} mg/L")
print(f"Difference (Riemann - Exact): {right_riemann_sum - exact_total:.2f} mg/L")
print(f"Percent error: {abs((right_riemann_sum - exact_total) / exact_total * 100):.2f}%")

### Cell 5: Visualizing the Continuous Model vs. Data
# Create fine time points for the continuous model
time_fine = np.linspace(0, 24, 200)
rate_fine = consumption_model(time_fine)

# Calculate the accumulated oxygen (running total) using FTC Part 1.
# np.polyint gives the antiderivative coefficients directly from fit_coeffs,
# so this always matches whatever model was fitted in Cell 4 (no manual algebra
# to keep in sync).
antideriv_coeffs = np.polyint(fit_coeffs)
accumulated_oxygen = np.polyval(antideriv_coeffs, time_fine)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top plot: Consumption Rate
ax1.plot(time_fine, rate_fine, 'b-', label='Continuous Model', linewidth=2)
ax1.scatter(time, consumption_rate, color='red', s=50, label='Sensor Data', zorder=5)
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Consumption Rate (mg/L per hour)')
ax1.set_title('Oxygen Consumption Rate Model')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Bottom plot: Accumulated Total (The Definite Integral)
ax2.plot(time_fine, accumulated_oxygen, 'g-', linewidth=2)
ax2.axhline(y=exact_total, color='purple', linestyle='--', label=f'Total at 24 hrs = {exact_total:.2f} mg/L')
ax2.set_xlabel('Time (hours)')
ax2.set_ylabel('Total Oxygen Consumed (mg/L)')
ax2.set_title('Accumulated Oxygen (Running Total via FTC Part 1)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

### Cell 6: Fish Biomass Prediction (FTC Symbolic)

# Define symbolic variable
t = sp.Symbol('t')

# Define the growth rate function symbolically.
# Note: this is an illustrative growth-rate function, not fitted to real
# biological growth data — treat downstream numbers as a worked example,
# not a validated prediction for actual fish.
G_t = 0.002 * t**2 + 0.15 * t + 0.5

# Find the antiderivative (indefinite integral)
F_t = sp.integrate(G_t, t)
print(f"Antiderivative (Total weight function): F(t) = {F_t}")

# Evaluate the definite integral from 0 to 120
total_gain = sp.integrate(G_t, (t, 0, 120))
print(f"\nTotal biomass gained from Day 0 to Day 120: {total_gain:.2f} grams")

# Initial weight at stocking
initial_weight = 50  # grams

# Final weight at harvest
final_weight = initial_weight + total_gain
print(f"Final weight at harvest (Day 120): {final_weight:.2f} grams")

### Cell 7: Creating a Growth Curve Visualization

# Convert symbolic expressions to numerical functions for plotting
G_num = lambdify(t, G_t, 'numpy')
F_num = lambdify(t, F_t, 'numpy')

# Generate time array
days = np.linspace(0, 120, 500)
growth_rates = G_num(days)
total_weights = F_num(days) + initial_weight  # Add the initial weight

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Top: Growth Rate 
ax1.plot(days, growth_rates, 'b-', linewidth=2)
ax1.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Growth Rate (grams/day)')
ax1.set_title('Daily Growth Rate of Atlantic Salmon')
ax1.grid(True, alpha=0.3)

# Bottom: Total Weight 
ax2.plot(days, total_weights, 'g-', linewidth=2, label='Total Weight')
ax2.scatter([0, 120], [initial_weight, final_weight], color='red', s=100, zorder=5, 
            label=f'Start: {initial_weight}g, Harvest: {final_weight:.1f}g')
ax2.set_xlabel('Time (days)')
ax2.set_ylabel('Total Weight (grams)')
ax2.set_title('Fish Growth Curve (Integral of Growth Rate)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Summary:")
print(f"  - Stocking weight: {initial_weight} g")
print(f"  - Harvest weight: {final_weight:.2f} g")
print(f"  - Total gain: {total_gain:.2f} g")
print(f"  - Average daily gain: {total_gain / 120:.2f} g/day")

### Cell 8: Comparison Summary Table
# Data for comparison
methods = ['Right Riemann Sum (Sensor Data)', 'Numerical Integration (FTC)', 'Symbolic Integration (FTC)']
oxygen_values = [right_riemann_sum, exact_total, exact_total]  # Both FTC methods give same result

# For growth, we only have symbolic FTC
growth_methods = ['Symbolic FTC (Growth)']
growth_values = [total_gain]

# Create summary table
print("=" * 60)
print("OXYGEN CONSUMPTION SUMMARY (24 hours)")
print("=" * 60)
print(f"{'Method':<35} {'Total (mg/L)':<15}")
print("-" * 60)
for method, value in zip(methods, oxygen_values):
    print(f"{method:<35} {value:<15.2f}")
print("=" * 60)

print("\n" + "=" * 60)
print("BIOMASS GAIN SUMMARY (120 days)")
print("=" * 60)
print(f"{'Method':<35} {'Total Gain (g)':<15}")
print("-" * 60)
print(f"{'Symbolic FTC (Growth Model)':<35} {total_gain:<15.2f}")
print("=" * 60)

print("\n**Key Takeaway:**")
print("  - The Riemann sum (using discrete data) is an approximation.")
print("  - The FTC (using a continuous model) gives the exact area under the curve.")
print("  - In real aquaculture, you use Riemann sums for sensor data and FTC for mathematical models.")

### Cell 9: Combined Dashboard
   
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: Riemann sum rectangles
ax = axes[0, 0]
ax.plot(time, consumption_rate, 'bo-', label='Sensor Data', linewidth=2, markersize=6)
for i in range(1, len(time)):
    x_left = time[i-1]
    y_height = consumption_rate[i]
    ax.add_patch(plt.Rectangle((x_left, 0), delta_t, y_height,
                               facecolor='red', alpha=0.3, edgecolor='red'))
ax.set_title('Right Riemann Sum')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('O2 Rate (mg/L/hr)')
ax.legend(fontsize=8)

# Panel 2: Fitted continuous model vs. sensor data
ax = axes[0, 1]
ax.plot(time_fine, rate_fine, 'b-', label='Fitted Model', linewidth=2)
ax.scatter(time, consumption_rate, color='red', s=30, label='Sensor Data', zorder=5)
ax.set_title('Oxygen Consumption Model')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('O2 Rate (mg/L/hr)')
ax.legend(fontsize=8)

# Panel 3: Accumulated oxygen (FTC Part 1)
ax = axes[0, 2]
ax.plot(time_fine, accumulated_oxygen, 'g-', linewidth=2)
ax.axhline(y=exact_total, color='purple', linestyle='--', label=f'Total = {exact_total:.2f} mg/L')
ax.set_title('Accumulated Oxygen (FTC)')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Total O2 (mg/L)')
ax.legend(fontsize=8)

# Panel 4: Growth rate
ax = axes[1, 0]
ax.plot(days, growth_rates, 'b-', linewidth=2)
ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax.set_title('Daily Growth Rate')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Growth Rate (g/day)')

# Panel 5: Growth curve
ax = axes[1, 1]
ax.plot(days, total_weights, 'g-', linewidth=2)
ax.scatter([0, 120], [initial_weight, float(final_weight)], color='red', s=60, zorder=5)
ax.set_title('Fish Growth Curve')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Total Weight (g)')

# Panel 6: text summary of the headline numbers
pct_err = abs((right_riemann_sum - exact_total) / exact_total * 100)
axes[1, 2].axis('off')
axes[1, 2].text(0.05, 0.85, 'Summary', fontsize=14, fontweight='bold')
axes[1, 2].text(0.05, 0.68, f'O2 (Riemann): {right_riemann_sum:.2f} mg/L')
axes[1, 2].text(0.05, 0.56, f'O2 (FTC): {exact_total:.2f} mg/L')
axes[1, 2].text(0.05, 0.44, f'Difference: {pct_err:.2f}%')
axes[1, 2].text(0.05, 0.28, f'Stocking wt: {initial_weight} g')
axes[1, 2].text(0.05, 0.16, f'Harvest wt: {float(final_weight):.1f} g')

fig.suptitle('RAS Oxygen & Growth Analysis Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('ras_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

### Cell 10: Results Summary Image

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')

summary_rows = [
    ("Right Riemann Sum (O2, 24h)", f"{right_riemann_sum:.2f} mg/L"),
    ("FTC / Exact Integration (O2, 24h)", f"{exact_total:.2f} mg/L"),
    ("Percent Difference", f"{pct_err:.2f}%"),
    ("Stocking Weight", f"{initial_weight} g"),
    ("Harvest Weight (Day 120, FTC)", f"{float(final_weight):.1f} g"),
    ("Total Biomass Gain", f"{float(total_gain):.1f} g"),
]

table = ax.table(cellText=summary_rows, colLabels=["Metric", "Value"],
                  cellLoc='left', loc='center', colWidths=[0.65, 0.35])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2.2)
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(fontweight='bold', color='white')
        cell.set_facecolor('#2c7fb8')
    else:
        cell.set_facecolor('#f0f8ff' if row % 2 == 0 else 'white')

ax.set_title('RAS Calculus Analysis — Key Results', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('ras_results_summary.png', dpi=150, bbox_inches='tight')
plt.show()
