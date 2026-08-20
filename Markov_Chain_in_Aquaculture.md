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
 etc.

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


Here:

- X₀ = Healthy
- X₁ = Healthy
- X₂ = Stress
- X₃ = Disease

Other possible paths:

Healthy → Mildly Stressed → Diseased → Recovered

or,

Healthy → Healthy → Healthy → Mildly Stressed

## States
The first important concept is a state.

A state represents a condition or situation that the system can occupy.

For example, consider fish health:

S={H,S,D,R,M}

where:

H = Healthy
S = Stressed
D = Diseased
R = Recovered
M = Dead

The system can move between these states.
For example:

H→S

means a healthy fish becomes stressed.

And:

D→R

means a diseased fish recovers.

Transitions

A transition is movement from one state to another.

For example:

H→S

is a transition from Healthy to Stressed.

But not every transition needs to be possible.

For example, we might define:

H→H

H→S

S→H

S→D

D→R

D→M

The transition structure describes the behavior of the system.

## Transition Probability
The most important quantity in a Markov chain is the transition probability.

Suppose historical farm data shows:

When fish are currently Healthy:

- 90% remain Healthy
- 8% become Stressed
- 2% become Diseased

Then:

P(H→H)=0.90

P(H→S)=0.08

P(H→D)=0.02

Notice:

0.90 + 0.08 + 0.02 = 1

This must always be true for all possible next states.

## Transition Matrix

Instead of writing every transition individually, we can put all transition probabilities into a matrix.

Suppose we have three states:

S={H,S,D}

The transition matrix might be:

|           | State 1 | State 2 | State 3 |
|-----------|---------|---------|---------|
| **State 1** | 0.90    | 0.08    | 0.02    |
| **State 2** | 0.30    | 0.50    | 0.20    |
| **State 3** | 0.10    | 0.20    | 0.70    |

$$
\begin{bmatrix} 
0.90 & 0.08 & 0.02 \\
0.30 & 0.50 & 0.20 \\
0.10 & 0.20 & 0.70 \end{bmatrix}
$$

Each row sums to 1.

The rows represent the current state.

The columns represent the next state.


So:

| Current → Next | Healthy | Stressed | Diseased |
|----------------|---------|----------|----------|
| **Healthy**    | 0.90    | 0.08     | 0.02     |
| **Stressed**   | 0.30    | 0.50     | 0.20     |
| **Diseased**   | 0.10    | 0.20     | 0.70     |

For example:

P₁₂ = 0.08


This means:

If the fish is currently **Healthy**, there is an **8%** probability that it will be **Stressed** in the next observation period.

We also need to know the distribution of the system at the beginning.

Suppose we have 1,000 fish and:

- 800 Healthy

- 150 Stressed

- 50 Diseased

Then the initial probability vector is:
π₀ = [0.80  0.15  0.05]

This tells us the probability distribution at time t=0.

Now something interesting happens.

We can multiply the current probability distribution by the transition matrix:
π₁ = π₀ P

So,

$$
\pi_1 = 
\begin{bmatrix}
0.80 & 0.15 & 0.05
\end{bmatrix}
\times
\begin{bmatrix}
0.90 & 0.08 & 0.02 \\
0.30 & 0.50 & 0.20 \\
0.10 & 0.20 & 0.70
\end{bmatrix}
$$


This produces the expected distribution of fish states at the next time step.

This is where linear algebra and probability come together.

And this is particularly relevant to your broader work with linear algebra applications in aquaculture.

**Iterating the Markov Chain**

We can repeat the process:

$$
\pi_1 = \pi_0 P
$$

$$
\pi_2 = \pi_1 P
$$

Therefore:

$$
\pi_2 = \pi_0 P^2
$$

And generally:

$$
\pi_n = \pi_0 P^n
$$


This demonstrates the power of **matrix exponentiation** in modeling system evolution over time.

It means we can use the transition matrix to estimate the state distribution several time periods into the future.

### Self-Transitions

An important concept is a self-transition.

For example:

H→H

with probability:

P(H→H)=0.90

This means the system stays in the same state.

In real applications, self-transitions are extremely common.

For example:

- Healthy fish → Healthy fish
  
- Good water quality → Good water quality
  
- Normal feeding → Normal feeding
  
- Low mortality → Low mortality

## Evolution of Markov Chain Theory

The original idea has developed considerably since Markov's work.

A simplified historical progression is:


$$
\begin{array}{c}
\text{Early 1900s} \\
\downarrow \\
\text{Andrey Markov: Markov Chains} \\
\downarrow \\
\text{Development of Stochastic-Process Theory} \\
\downarrow \\
\text{Statistical and Mathematical Modeling} \\
\downarrow \\
\begin{array}{l}
\quad \text{Queueing Systems} \\
\quad \text{Reliability Engineering} \\
\quad \text{Population Models} \\
\quad \text{Finance} \\
\quad \text{Genetics} \\
\quad \text{Physics}
\end{array} \\
\downarrow \\
\text{Computer Science and Artificial Intelligence} \\
\downarrow \\
\begin{array}{l}
\quad \text{Search Engines} \\
\quad \text{Natural Language Processing} \\
\quad \text{Speech Recognition} \\
\quad \text{Recommendation Systems}
\end{array} \\
\downarrow \\
\text{Modern Probabilistic Modeling} \\
\downarrow \\
\begin{array}{l}
\quad \text{Hidden Markov Models} \\
\quad \text{Markov Decision Processes} \\
\quad \text{Markov Chain Monte Carlo (MCMC)} \\
\quad \text{Reinforcement Learning}
\end{array}
\end{array}
$$

**Best to Remember**

We can think of a Markov chain as a probabilistic state machine.

A normal deterministic system might say:

>**If temperature exceeds 15°C, fish enter Stress.**

A Markov model instead says:

>**If fish are currently Healthy, there is a 90% probability they remain Healthy, an 8% probability they become Stressed, and a 2% probability they become Diseased during the next observation period.**

That difference is important.

Real biological systems are uncertain. Markov chains give us a mathematical framework for representing that uncertainty.

## Markov Chain in Aquaculture

### 1. Discrete-time Markov chain

The system changes at discrete intervals:

t=0,1,2,3,…

For example, fish health recorded:

- Monday
  
- Tuesday
  
- Wednesday
  
- Thursday

### 2. Continuous-time Markov chain

Transitions can occur at any point in time rather than at fixed intervals.

For example:

Healthy → Stress → Disease

where the transitions occur according to rates rather than simply "every day."

This can become particularly interesting for **disease and mortality modeling**.

### 3. Hidden Markov Model (HMM)

Sometimes we cannot directly observe the true state.

For example, we may not know whether a fish is truly:

Healthy → Stressed → Diseased

Instead, we observe:

- swimming behavior
  
- appetite
  
- oxygen consumption
  
- activity
  
- external appearance

The actual health condition is hidden, while measurements are observable.

### 4. Markov Decision Process

A normal Markov chain describes:

>**State→State**

A Markov Decision Process introduces actions:

>**State+Action→New State**

For example:

$$
\begin{array}{l}
\text{Fish stressed} \\
\quad \downarrow \\
\quad
\begin{array}{ll}
\text{├──} & \text{Increase oxygen} \\
\text{├──} & \text{Reduce feeding} \\
\text{└──} & \text{Increase water exchange}
\end{array} \\
\quad\quad\quad\quad\quad\quad\downarrow \\
\quad\quad\quad\text{New fish-health state}
\end{array}
$$

This becomes relevant when we want to move from prediction to decision-making.


Once we define these states and estimate their transition probabilities from historical data, we can build a Markov model.

For example:

$$
P = 
\begin{bmatrix}
0.85 & 0.12 & 0.03 \\
0.30 & 0.50 & 0.20 \\
0.05 & 0.15 & 0.80
\end{bmatrix}
$$

could represent the probability of moving among three fish-health states.

Then we can ask meaningful questions such as:

- What is the probability that a healthy fish population will enter a high-risk condition within the next 7 days?

- What proportion of the population is expected to remain healthy after 30 days?

- What is the long-term probability of being in each health state?

That is where Markov chains move from:

Mathematical theory → Statistical modeling → Practical aquaculture decision support

----

## Markov Chain Analysis of Sea-Lice Dynamics in Norwegian Salmon Farms

### Objective

This project will investigate whether Markov chain models can be used to describe and predict the progression of adult female sea-lice levels in Norwegian Atlantic salmon farms.

The primary objective is to estimate:

$$
P(L_{t+k} \geq 0.5)
$$

where ($L_t$) represents adult female lice per fish and (0.5) is the Norwegian regulatory threshold.

The model will provide locality-level probabilities of future threshold exceedance, rather than simply predicting a single future lice count.

### Dataset

The dataset contains weekly observations from Norwegian salmon-farming localities from 2020 through week 31 of 2026.

Key variables include:

- year
  
- week
  
- locality_name

- locality_number

- female_lice
  
- latitude
  
- longitude

- sea_temperature

The longitudinal structure of the data makes it suitable for modeling transitions in lice-risk states over time.

### Markov Chain Concept

A Markov chain models a system that moves between discrete states over time.

The fundamental assumption is the Markov property:

$$
P(X_{t+1}|X_t)
$$

In practical terms, the probability of the next lice state depends primarily on the current lice state.

A transition matrix (P) describes the probability of moving from one state to another:

$$
P_{ij}=P(X_{t+1}=j|X_t=i)
$$

Future state probabilities can then be estimated using:

$$
\pi_{t+k}=\pi_tP^k
$$

where ($\pi_t$) is the current state-probability vector.

### Lice Risk States
Adult female lice will be converted from continuous measurements into discrete analytical states.
An initial proposed classification is:

| State | Female lice/fish | Interpretation |
|-------|------------------|----------------|
| S0    | < 0.10           | Baseline / very low |
| S1    | 0.10–<0.50       | Trigger / early warning |
| S2    | 0.50–<0.80       | Threshold exceeded |
| S3    | 0.80–<1.00       | High lice level |
| S4    | ≥ 1.00           | Very high lice level |

The 0.50 female lice/fish level represents the regulatory threshold. The other boundaries are analytical categories and should be evaluated against the observed data and relevant biological/industry guidance before finalization.

The state structure allows the model to capture both escalation and recovery:

$$
S0\rightarrow S1\rightarrow S2\rightarrow S3\rightarrow S4
$$

and:

$$
S4\rightarrow S3\rightarrow S2\rightarrow S1\rightarrow S0
$$

### Production-Cycle Structure

A major feature of Norwegian salmon production is that a locality does not operate continuously.

A locality may experience:

$$
\text{Production Cycle}
\rightarrow
\text{Harvest}
\rightarrow
\text{Fallow}
\rightarrow
\text{New Production Cycle}
$$

Therefore, missing observations after harvest must not be interpreted as zero lice or as a normal state transition.

Each locality should be assigned a production-cycle identifier where possible.

A useful additional variable is:

$$
CycleAge_t=\text{weeks since stocking}
$$

This allows lice dynamics to be compared according to the stage of the production cycle.

### Locality-Level Prediction

The model can estimate the probability of future threshold exceedance for each active locality.

For example:

$$
Risk_i(t+k)=P(L_{i,t+k}\geq0.5)
$$

A locality currently at 0.38 female lice/fish might therefore have estimated probabilities such as:

| Forecast horizon | Probability of ≥0.5 |
|------------------|---------------------|
| 1 week           | 0.12                |
| 4 weeks          | 0.31                |
| 8 weeks          | 0.48                |

These values are illustrative; actual probabilities will be estimated from the historical dataset.

This provides an early-warning framework rather than only a point forecast.

### Seasonality and Environmental Factors

A single transition matrix for 2020–2026 may be too simplistic because sea-lice dynamics are seasonal.

Therefore, the analysis should compare:

**Basic Markov model**

$$
P(X_{t+1}|X_t)
$$

with a seasonal model:

$$
P(X_{t+1}|X_t,Season_t)
$$

The available sea-temperature variable can also be incorporated:

$$
P(X_{t+1}|X_t,Temperature_t)
$$

Additional variables such as cycle age and geographical region may subsequently be evaluated.

Latitude and longitude can be used to investigate spatial variation in transition behavior and to produce locality-level risk maps.

### Production Cycles and Repeated Localities

Because the dataset covers approximately six years, many localities may contain observations from multiple production cycles.

This allows investigation of questions such as:

- Do lice dynamics differ between production cycles?
  
Does cycle age affect transition probabilities?
Does a locality with high lice levels in one cycle show different risk in its subsequent cycle?
How does the transition from harvest/fallow to a new cycle affect early-cycle lice risk?

Previous-cycle characteristics may be explored as potential predictors, while recognizing that biological carry-over should not be assumed automatically.
