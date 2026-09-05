# The Fundamental Theorem of Calculus (FTC): in reference to Aquaculture

Doing infinite sums by hand is impossible. The **Fundamental Theorem of Calculus (FTC)** gives us the ultimate shortcut. It tells us that **integration (finding totals) and differentiation (finding rates) are reverse operations.**

For an aquaculturist, this means: If we know the *rate* at which our fish are growing, the FTC lets us find the *total* biomass gained in seconds.

---

## 1. The Two Parts of the FTC 

### Part 1: The "Rate of Accumulation" Rule
> *If you have a running total  g(x) of something (like total oxygen added up from time 0 to time  x , the **instantaneous rate** at which that total is changing at time x is just the original function f(x) .*

**Mathematically:**

$$
g(x) = \int_{a}^{x} f(t) \, dt \quad \Longrightarrow \quad g'(x) = f(x)
$$

**In Aquaculture:** 

Imagine f(t) is the *rate* of feed going into a tank (kg/hour). If g(x) is the *total* feed that has been added up to hour x , then the derivative of the total feed g'(x) tells you exactly how fast feed is being added *right now*, f(x). You don't have to recalculate the total; the rate is baked into the total.

---

### Part 2: The "Evaluation" Rule 

> *To find the exact total change of f(x) from time a to time b, just find an antiderivative F(x) (a function whose derivative is f(x), and subtract:*

**Mathematically:**

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

**In Aquaculture:** 

If f(x) is the **growth rate** of your fish (grams/day), and you know the antiderivative F(x) (which represents the *total weight formula*), then the total weight gained between Day a and Day b is simply **Weight at Day b minus Weight at Day a**. No infinite rectangles required!

---

## 2. Why This Saves Aquaculture Data Scientists

Without the FTC:

- We collect sensor data every 10 seconds.
- We multiply each reading by 10 seconds and add them all up (Riemann sums).
- If We miss a data point, our estimate is off.

With the FTC:
- We fit a continuous mathematical model to your sensor data (e.g., Oxygen depletion follows a polynomial curve).
- We find the antiderivative of that model.
- We evaluate it at the start and end times. (**Instant exact total**)

---

## 3. Worked Examples in Aquaculture

### Example 1: Calculating Total Feed Delivery (Using FTC Part 2)

A computerized feeder dispenses feed at a rate modeled by:

$$
r(t) = 100 + 20t \quad \text{(kg per hour)}
$$

where \ (t \) is the time in hours after 8:00 AM.

**Question:** How much total feed is dispensed between \( t = 1 \) (9:00 AM) and \( t = 4 \) (12:00 PM)?

**Solution:**

1. Find the antiderivative \( R(t) \) of \( r(t) \):
   
$$
R(t) = 100t + 10t^2
$$
   
*(Check: The derivative of \( 100t + 10t^2 \) is \( 100 + 20t \), which matches our rate.)*

2. Apply FTC Part 2:
   
$$
\text{Total Feed} = \int_{1}^{4} (100 + 20t) \, dt = R(4) - R(1)
$$

3. Calculate:

$$
R(4) = 100(4) + 10(4)^2 = 400 + 160 = 560
$$

$$
R(1) = 100(1) + 10(1)^2 = 100 + 10 = 110
$$

$$
\text{Total} = 560 - 110 = 450 \text{ kg}
$$

**Result:** The feeder drops **450 kg** of feed between 9:00 AM and 12:00 PM.

---

### Example 2: The "Running Total" (Using FTC Part 1)

You have a sensor that measures the rate of oxygen production by algae in a biofloc tank:

$$
p(t) = 5 + \sin(t) \quad \text{(mg/L per hour)}
$$

Let \( O(x) \) be the *total* oxygen produced from time \( 0 \) to time \( x \). 

**Question:** How fast is the *total* oxygen production increasing at exactly \( x = 3 \) hours?

**Solution:**

By FTC Part 1, the derivative of the total production is just the original rate function.

$$
O'(x) = p(x)
$$

So at \( x = 3 \):

$$
O'(3) = p(3) = 5 + \sin(3) \approx 5 + 0.141 = 5.141 \text{ mg/L per hour}
$$

**Result:** At the 3-hour mark, the total accumulated oxygen is increasing at a rate of **5.14 mg/L per hour**. This tells you exactly when the algae are most productive.

---

### Example 3: Calculating Total Biomass Gain (Polynomial Model)

A research paper provides a growth model for juvenile Salmon:

$$
G(t) = 0.02t^2 + 0.5t + 2 \quad \text{(grams per day)}
$$

where \( t \) is days. 

**Question:** What is the total biomass gained by a single fish between Day 10 and Day 30?

**Solution:**

1. **Find the Antiderivative** \( F(t) \):

$$
F(t) = \frac{0.02}{3}t^3 + \frac{0.5}{2}t^2 + 2t
$$
   
$$
F(t) \approx 0.00667t^3 + 0.25t^2 + 2t
$$


2. **Evaluate at \( t=30 \) and \( t=10 \):**

$$
F(30) = 0.00667(27000) + 0.25(900) + 2(30) = 180.09 + 225 + 60 = 465.09
$$

$$
F(10) = 0.00667(1000) + 0.25(100) + 2(10) = 6.67 + 25 + 20 = 51.67
$$

3. **Subtract**:

$$
\text{Total Gain} = F(30) - F(10) = 465.09 - 51.67 = 413.42 \text{ grams}
$$

**Result:** The salmon gains approximately **413 grams** in that 20-day grow-out period.

---

## 4. Why This Matters for Farm Management

| Scenario | Without FTC (Riemann Sums) | With FTC (Antiderivatives) |
| :--- | :--- | :--- |
| **Feed Ordering** | Estimate based on hourly manual checks. | Model the feeding rate, integrate over the month. Order exact feed bags. |
| **Aeration Control** | React to oxygen dropping too low. | Integrate the consumption rate to predict *exactly* when oxygen will hit a critical level. |
| **Harvest Weight** | Guess the average weight of the fish. | Use a growth rate curve, integrate it, and know the *exact* total biomass in the tank for market. |

---

## 5. Summary for Your Code/Repo

If you are writing a Python script or an R script for aquaculture data:

1. **If you have discrete sensor data** (e.g., readings every minute) → Use a **Riemann Sum** (trapz function in Python/NumPy).
2. **If you have a mathematical equation** for the rate of change (e.g., $\( f(t) = at^2 + bt + c \))$ → Use the **Fundamental Theorem of Calculus**. 
   - Use `sympy` (Python) to find the antiderivative symbolically.
   - Evaluate it at your start and end times.

The FTC is the mathematical bridge between **"What is happening right now?"** (rate) and **"What is the total impact?"** (accumulation). It is the single most important calculus tool for managing a recirculating aquaculture system (RAS).
