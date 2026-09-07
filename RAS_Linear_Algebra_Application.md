
In **Recirculating Aquaculture Systems (RAS)**, one of the most critical phases is the bacterial maturation period, the weeks-long process of establishing a stable nitrifying bacterial community before introducing fish. This isn't just biology; it's applied linear algebra in action.

When we introduce bacteria into a new RAS tank and wait for the system to "stabilize," we are witnessing complex mathematical phenomena unfold: **eigenvalues** determining stability, **steady-state vectors** representing equilibrium, and even the mathematical principle behind **PageRank** (the "teleportation" concept) describing how we intervene to guide the system toward stability.

I explain these mathematical concepts in plain language, connect them to the real-world challenge of stabilizing bacterial populations in RAS, and provide references for further reading.

## Part 1: Eigenvalues and System Stability

Imagine we have a system that evolves: the concentrations of ammonia, nitrite, bacteria, and oxygen in our RAS tank. The system can be described by a collection of equations that govern how each variable changes based on the others. This system can be represented as a matrix 
A.

An eigenvalue (λ) is a number that tells you whether the system will settle down to a stable state or spiral out of control. It answers the question: "If I disturb this system, will it recover, or will it get worse?"

The eigenvalues of a system's matrix determine its stability:

| Conditions | Meaning for RAS |
|---|---|
| **All eigenvalues have negative real parts** | The system is **locally asymptotically stable**. Disturbances decay over time. **This is what we're waiting for during cycling.** |
| **Any eigenvalue has a positive real part** | The system is **unstable**. Ammonia or nitrite may accumulate uncontrollably. |
| **Eigenvalues with imaginary parts** | The system may experience **damped oscillations** before settling, for example, transient spikes in ammonia/nitrite as bacterial populations fluctuate. |

**The Mathematical Framework**

The state of the RAS water can be represented as a vector:

$$
\vec{x}(t)=
\begin{bmatrix}
\text{Ammonia } (NH_3) \\
\text{Nitrite } (NO_2^-) \\
\text{Nitrate } (NO_3^-) \\
\text{Nitrifying Bacteria Population} \\
\text{Dissolved Oxygen}
\end{bmatrix}
$$


The rate of change of this system over time is modeled by:

$$
\frac{d\vec{x}}{dt}=A\vec{x}
$$

where A is the matrix describing how each variable affects the others.

The eigenvalues of A are the solutions to:

$$
\det(A-\lambda I)=0
$$

**What This Means for RAS:**

During the bacterial maturation period :

- Initially, the system has eigenvalues with positive real parts; ammonia and nitrite levels spike as bacterial population is low.

- Over time, as bacteria establish, the eigenvalues gradually shift toward negative values.

- When the largest eigenvalue becomes negative, our system is ready for fish.

**Practical implication:** The speed of our cycling is determined by how close the dominant eigenvalue is to zero. A value close to zero means a slow, drawn-out cycle.

This stability analysis is routinely used in aquaculture research. Studies on water quality dynamics have used eigenvalue analysis of Jacobian matrices to determine local asymptotic stability of aquaculture systems.

## Part 2: The Power Method and Markov Chains

The Power Method is an iterative algorithm for approximating the dominant eigenvalue and its corresponding eigenvector of a matrix. It is the mathematical engine behind Google's PageRank algorithm and, conceptually, behind tracking our RAS bacterial population over time.

When we start cycling our tank, we don't know the final stable state. We monitor daily. This process is mathematically equivalent to repeatedly applying the system's transition rules:

| **Day** | **Mathematical Description** |
|---|---|
| **Day 0** | Initial state vector: $(\vec{x}_0\)$ (high ammonia, low bacteria) |
| **Day 1** | $(\vec{x}_1 = A\vec{x}_0\)$ |
| **Day 2** | $(\vec{x}_2 = A\vec{x}_1 = A^2\vec{x}_0\)$ |
| **...** | ... |
| **Day k** | $(\vec{x}_k = A^k\vec{x}_0\)$ |

As **k→∞**, the system approaches the steady-state vector, the stable bacterial community composition and water chemistry.

A **Markov chain** is a sequence of states where the next state depends only on the current state. The bacterial population in our RAS follows this principle: tomorrow's bacterial community depends primarily on today's conditions (temperature, pH, nutrient availability), not on the entire history.

In the context of our RAS:

- States: Different bacterial community compositions (e.g., ratios of Nitrosomonas to Nitrobacter)

- Transition Matrix: Governs how the community shifts from one state to another

- Steady State: The stable bacterial equilibrium we're aiming for before introducing fish

> **A stochastic model for managing microorganisms in RAS was developed using Monte Carlo simulation to predict the growth of key microorganisms and monitor population dynamics** (Fu, Songzhe, et al., 2015)

## Part 3: Bacterial Population Dynamics as a Network

Our RAS biofilter isn't a single species—it's a complex web of interacting bacterial species:

- Nitrosomonas: Converts ammonia to nitrite

- Nitrobacter: Converts nitrite to nitrate

- Other heterotrophs: Consume organic matter

This creates a food web where each species links to the next.

**The PageRank Analogy**

Just as PageRank assigns importance to webpages based on incoming links, we can think of bacterial species having "importance" based on the flow of nutrients:

- *Nitrosomonas* → produces nitrite (food for *Nitrobacter*)
- *Nitrobacter* → produces nitrate (less toxic, but can accumulate)



## References

Fu, S., Liu, Y., Li, X., Tu, J., Lan, R., & Tian, H. (2015). A preliminary stochastic model for managing microorganisms in a recirculating aquaculture system. Annals of Microbiology, 65(2), 1119-1129.


