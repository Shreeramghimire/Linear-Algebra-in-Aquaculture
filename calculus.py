# Aquaculture Data Analysis: Riemann Sums vs. The FTC

### Scenario
You are managing a **Recirculating Aquaculture System (RAS)** for raising Atlantic Salmon. You have:
1. **Sensor data** measuring oxygen consumption rate every 2 hours for a 24-hour period.
2. A **mathematical model** for fish growth rate over a 120-day grow-out period.

**Your Tasks:**
1. Estimate total oxygen consumed in 24 hours using a Riemann sum.
2. Calculate the exact oxygen consumption using a fitted model and the FTC.
3. Predict the total biomass of a single fish at harvest using the FTC.
4. Visualize the data and the accumulated totals.

---

### Cell 1: Import Required Libraries
Run this cell first to import everything we need.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz, quad
import sympy as sp
from sympy import symbols, integrate, lambdify

# Enable inline plotting for Jupyter
%matplotlib inline

# Set style for better plots
plt.style.use('seaborn-v0_8-whitegrid')
print("Libraries imported successfully!")

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
