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

\[
F(t) = \frac{0.02}{3}t^3 + \frac{0.5}{2}t^2 + 2t
\]
   
\[
F(t) \approx 0.00667t^3 + 0.25t^2 + 2t
\]
