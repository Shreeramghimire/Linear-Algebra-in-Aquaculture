# The Fundamental Theorem of Calculus (FTC): The Aquaculture "Shortcut"

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

**Aquaculture Translation:** 

Imagine f(t) is the *rate* of feed going into a tank (kg/hour). If g(x) is the *total* feed that has been added up to hour x , then the derivative of the total feed g'(x) tells you exactly how fast feed is being added *right now*, f(x). You don't have to recalculate the total; the rate is baked into the total.

---

### Part 2: The "Evaluation" Rule 

> *To find the exact total change of f(x) from time a to time b, just find an antiderivative F(x) (a function whose derivative is f(x), and subtract:*

**Mathematically:**

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

**Aquaculture Translation:** 
If f(x) is the **growth rate** of your fish (grams/day), and you know the antiderivative F(x) (which represents the *total weight formula*), then the total weight gained between Day a and Day b is simply **Weight at Day b minus Weight at Day a**. No infinite rectangles required!

---

## 2. Why This Saves Aquaculture Data Scientists

Without the FTC:

- You collect sensor data every 10 seconds.
- You multiply each reading by 10 seconds and add them all up (Riemann sums).
- If you miss a data point, your estimate is off.

With the FTC:
- You fit a continuous mathematical model to your sensor data (e.g., Oxygen depletion follows a polynomial curve).
- You find the antiderivative of that model.
- You evaluate it at the start and end times. (**Instant exact total**)

---
