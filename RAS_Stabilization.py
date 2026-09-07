# RAS Stabilization Prediction Model: 
   It predicts biofilter/nitrogen-cycle stabilization time in a Recirculating Aquaculture System (RAS) using:
  1. A Monod-kinetics ODE system (ammonia -> nitrite -> nitrate via AOB/NOB)
  2. Monte Carlo simulation over uncertain initial conditions / parameters
  3. Local stability analysis via the Jacobian's eigenvalues
 
 
import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass, field, asdict

# 1. BASE CONDITIONS — this is your single configuration point
# ----------------------------------------------------------------------
# State vector order: [NH3, NO2, NO3, X_AOB, X_NOB]
#   NH3, NO2, NO3   : mg/L (nitrogen species)
#   X_AOB           : ammonia-oxidizing bacteria biomass (mg/L, proxy units)
#   X_NOB           : nitrite-oxidizing bacteria biomass (mg/L, proxy units)
 
 
@dataclass
class BaseConditions:
    # --- initial state ---
    NH3_0: float = 5.0        # mg/L, starting ammonia spike
    NO2_0: float = 0.0        # mg/L
    NO3_0: float = 0.0        # mg/L
    X_AOB_0: float = 0.05     # mg/L, seed AOB biomass
    X_NOB_0: float = 0.05     # mg/L, seed NOB biomass
 
    # --- Monod kinetics parameters (defaults from nitrification literature) ---
    mu_max_AOB: float = 0.9   # 1/day, max growth rate of AOB
    mu_max_NOB: float = 1.0   # 1/day, max growth rate of NOB
    Ks_NH3: float = 0.5       # mg/L, half-saturation const for AOB on NH3
    Ks_NO2: float = 0.3       # mg/L, half-saturation const for NOB on NO2
    Y_AOB: float = 0.15       # yield coefficient (biomass per mg N oxidized)
    Y_NOB: float = 0.05       # yield coefficient
    b_AOB: float = 0.05       # 1/day, AOB decay rate
    b_NOB: float = 0.05       # 1/day, NOB decay rate
 
    # --- environmental modifiers ---
    temperature_C: float = 20.0
    DO_mgL: float = 6.0
    Ks_DO: float = 0.5        # half-saturation for DO limitation
 
    # --- system / operational ---
    flow_exchange_rate: float = 0.1   # 1/day, dilution/water-exchange rate
    NH3_load_rate: float = 0.0        # mg/L/day, continuous feed-derived input
 
    def initial_state(self):
        return np.array([self.NH3_0, self.NO2_0, self.NO3_0,
                          self.X_AOB_0, self.X_NOB_0])
 
 
BASE = BaseConditions()
 
# Distributions used for Monte Carlo sampling (mean, std)
# Keys must match BaseConditions field names.
PARAM_DISTRIBUTIONS = {
    "NH3_0":       (BASE.NH3_0, 1.0),
    "temperature_C": (BASE.temperature_C, 2.0),
    "mu_max_AOB":  (BASE.mu_max_AOB, 0.1),
    "mu_max_NOB":  (BASE.mu_max_NOB, 0.1),
    "DO_mgL":      (BASE.DO_mgL, 0.5),
}
