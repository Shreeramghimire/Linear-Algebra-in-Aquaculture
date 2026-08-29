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
