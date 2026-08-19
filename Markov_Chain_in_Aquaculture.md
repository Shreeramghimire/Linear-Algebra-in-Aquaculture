# What is Markov Chain?
A **Markov chain** is a mathematical model for describing a system that moves between different **states** over time.  
The key feature is that the probability of moving to the next state depends **only** on the current state, not on the entire history of how the system got there.

**Core Principle:** “The future depends on the present, not on the complete past.”
It makes the model **memoryless** and computationally efficient.

**For example**, imagine a fish farm monitoring fish health:

- Healthy
- Mildly stressed
- Diseased
- Recovered
- Dead

A fish might move:

Healthy → Mild Stress → Diseased → Recovered

or perhaps:

Healthy → Healthy → Healthy → Mild Stress

A Markov model asks:

Given that the fish is currently Healthy, what is the probability that tomorrow it will be Healthy, Mildly Stressed, or Diseased?
