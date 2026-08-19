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

## History
The idea comes from the Russian mathematician **Andrey Andreyevich Markov**. Markov developed this theory in the early 20th century.

He was interested in probability theory and sequences of events, particularly whether events could be modeled when the probability of the next event depends on the previous event.

## Why "Chain"?

The word chain comes from the fact that the process can be represented as a sequence of transitions:
X₀ → X₁ → X₂ → X₃ → ⋯
Where:

- X₀ = initial state
- X₁ = state at time 1
- X₂ = state at time 2
- X₃ = state at time 3
- etc.

Each arrow (→) represents a possible transition from one state to the next.

### Example

Imagine a fish farm monitoring fish health. The possible states are:

- Healthy
- Mildly stressed
- Diseased
- Recovered
- Dead

A fish might move through states like this:
Healthy → Healthy → Stress → Disease
