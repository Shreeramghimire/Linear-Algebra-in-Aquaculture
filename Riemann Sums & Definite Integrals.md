# Riemann Sums & Definite Integrals: An Aquaculture Perspective

In aquaculture, we constantly deal with continuous data; oxygen levels fluctuating over time, fish biomass accumulating, or feed being dispersed across a pond. How do we calculate the **total** effect of these continuous changes? We can't just multiply a single rate by time because the rate keeps changing.

This is where **Riemann Sums** and **Definite Integrals** come in. They allow us to sum up tiny, continuous changes to find a total.

## Definition

### The Net Area
The net area under a graph of $f(x)$ from  $a$ to $b$ is the difference between the area above the x-axis $A_1$ and the area below it $A_2$.

> **Aquaculture Context:** If $f(t)$ represents the *rate of oxygen change* (mg/L per hour), the net area tells us the net change in oxygen. If the line goes below the x-axis, oxygen is being consumed (negative area).

### The Riemann Sum
We divide the interval $[a, b]\$ into $( n )$ subintervals. The width of each slice is:

$$
\Delta x = \frac{b-a}{n}
$$

We pick a sample point $( x_i^* \)$ in each slice and calculate the sum:

$$
\sum_{i=1}^{n} f(x_i^*) \Delta x_i
$$

This approximates the total net area using rectangles.

| Type of Sum | How to Choose $x_i^*$ | Aquaculture Analogy |
| :--- | :--- | :--- |
| **Left-Endpoint** | Use the value at the start of the interval. | Checking the water temperature *only* at the beginning of each hour. |
| **Right-Endpoint** | Use the value at the end of the interval. | Checking the temperature *only* at the end of each hour. |
| **Midpoint** | Use the value in the middle of the interval. | Taking a reading halfway through the hour (generally more accurate). |
| **Lower Sum** | Choose the minimum value in the interval. | Optimistically assuming the fish ate the *least* amount of feed possible in that time frame. |
| **Upper Sum** | Choose the maximum value in the interval. | Pessimistically assuming the fish ate the *most* feed possible. |

> **Rule of Thumb for Monotonic Functions:**
> * If the function is **increasing** (e.g., fish weight gain accelerating), a **Left** sum is an **underestimate** and a **Right** sum is an **overestimate**.
> * If the function is **decreasing** (e.g., oxygen depleting), a **Left** sum is an **overestimate** and a **Right** sum is an **underestimate**.

### The Definite Integral
The definite integral is the **limit** of the Riemann sum as the number of rectangles approaches infinity (\( n \to \infty \)). It gives the *exact* net area.

$$
\int_{a}^{b} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x
$$

---

## 2. Practical Applications in Aquaculture

Here is how we apply these mathematical tools to real fish farming problems:

### Application A: Total Feed Consumption

You know the *rate* at which fish eat feed (kg/hour), but you need the *total* feed given over a 12-hour period. If the feeding rate changes throughout the day, you integrate the rate function.

### Application B: Oxygen Depletion & Aeration

Dissolved oxygen (DO) is critical for fish survival. If you measure the rate of oxygen consumption at different times of the day, integrating that rate tells you exactly how much oxygen was depleted. This helps you program aerators to turn on at the right time.

### Application C: Fish Growth (Biomass)

If you have a model for the daily growth rate of your fish (grams/day), integrating that model from Day 1 to Day 120 gives you the total biomass added to the tank.

---

## 3. Worked Examples

### Example 1: Estimating Oxygen Consumption (Riemann Sum)

You measure the rate of oxygen depletion in a tank $r(t)$ (in mg/L per minute) at 5-minute intervals.

| Time (min) | 0 | 5 | 10 | 15 | 20 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rate** \( r(t) \) | -0.2 | -0.5 | -0.8 | -0.4 | -0.1 |

**Question:** Use a Right Riemann Sum with 4 intervals to estimate the total oxygen lost over 20 minutes.

**Solution:**
- Width of intervals: \( \Delta t = 5 \) minutes.
- Right endpoints: \( t = 5, 10, 15, 20 \).
- Calculation:

$$
\text{Oxygen Lost} \approx 5 \cdot [ r(5) + r(10) + r(15) + r(20) ]
$$

$$
= 5 \cdot [ (-0.5) + (-0.8) + (-0.4) + (-0.1) ] = 5 \cdot (-1.8) = -9.0 \text{ mg/L}
$$

**Interpretation:** The fish consumed approximately 9 mg/L of oxygen during this 20-minute period. Since the rate is negative, the integral yields a negative value (depletion).

---

### Example 2: Total Biomass Gain (The Definite Integral)

The growth rate of a specific species of Tilapia is modeled by:

$$
G(t) = 0.5 + 0.1t \quad \text{(grams per day)}
$$

where $t$ is time in days.

**Question:** How much total biomass does a single fish gain between day 0 and day 10?

**Solution:**
We need the definite integral:

$$
\text{Total Gain} = \int_{0}^{10} (0.5 + 0.1t) \, dt
$$

**Step 1:** Find the antiderivative:
