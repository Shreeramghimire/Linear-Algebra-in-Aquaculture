
# Linear and Matrix Transformations – Principles & Methods

## 1.1 What is a Linear Transformation?

A transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is **linear** if it satisfies two rules for all vectors $\vec{u}, \vec{v}$ and scalars $c$:

1. **Additivity:** $T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$  
2. **Homogeneity:** $T(c\vec{u}) = cT(\vec{u})$

**Key consequence:** A linear transformation always maps the zero vector to the zero vector ($T(\vec{0}) = \vec{0}$).  
*(This is why translation by a nonzero vector is not linear, as seen in your earlier quiz.)*

---

## 1.2 The Standard Matrix of a Linear Transformation (Core Method)

For any linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, there exists a unique **$m \times n$ standard matrix** $A$ such that:

$T(\vec{x}) = A\vec{x} \quad \text{for all } \vec{x} \in \mathbb{R}^n$

**How to find $A$:**  
Let $$\vec{e}_1, \vec{e}_2, \dots, \vec{e}_n$$ be the standard basis vectors of $\mathbb{R}^n$ (columns of the identity matrix). Then:

$$
A = \begin{bmatrix} 
T(\vec{e}_1) & T(\vec{e}_2) & \cdots & T(\vec{e}_n)
\end{bmatrix}
$$

**Example:**  

If  
$T: \mathbb{R}^2 \to \mathbb{R}^3$  
and  

$$
T(\vec{e}_1) = \begin{bmatrix} 
1 \\ 
0 \\ 
0 \end{bmatrix}, \quad
T(\vec{e}_2) = \begin{bmatrix} 
0 \\ 
1 \\ 
0 \end{bmatrix},
$$

then the standard matrix is  

$$
A = \begin{bmatrix}
1 & 0 \\
0 & 1 \\
0 & 0
\end{bmatrix}.
$$

## 1.3 Geometric Linear Transformations (from your PDF)

| Transformation | Standard Matrix (2D) | Effect |
|----------------|----------------------|--------|
| **Horizontal shear** | ⎡1 &nbsp; k⎤<br>⎣0 &nbsp; 1⎦ | Shifts points horizontally by an amount proportional to their height. |
| **Vertical shear** | ⎡1 &nbsp; 0⎤<br>⎣k &nbsp; 1⎦ | Shifts points vertically by an amount proportional to their x-coordinate. |
| **Projection onto x-axis** | ⎡1 &nbsp; 0⎤<br>⎣0 &nbsp; 0⎦ | Collapses all points onto the x-axis (loses y-information). |
| **Projection onto y-axis** | ⎡0 &nbsp; 0⎤<br>⎣0 &nbsp; 1⎦ | Collapses all points onto the y-axis. |
| **Rotation by angle θ** | ⎡cos θ &nbsp; −sin θ⎤<br>⎣sin θ &nbsp; cos θ⎦ | Rotates points counterclockwise. |
| **Reflection across x-axis** | ⎡1 &nbsp; 0⎤<br>⎣0 &nbsp; −1⎦ | Flips points over the x-axis. |
| **Scaling** | ⎡s &nbsp; 0⎤<br>⎣0 &nbsp; s⎦ | Enlarges or shrinks uniformly. |

## 1.4 One-to-One (Injective) Transformations

**Definition:** $T$ is one-to-one if every output vector $\vec{b}$ comes from **at most one** input vector $\vec{x}$. Equivalently:

$$
T(\vec{x}) = T(\vec{y}) \implies \vec{x} = \vec{y}
$$

**Test:** For a linear transformation $T(\vec{x}) = A\vec{x}$,  
$T$ is one-to-one **if and only if** the equation $A\vec{x} = \vec{0}$ has **only the trivial solution** ($\vec{x} = \vec{0}$).

**Practical check:** The columns of $A$ must be linearly independent. For a square matrix, this means $\det(A) \neq 0$ (full rank, $n$ pivots).

---

## 1.5 Onto (Surjective) Transformations

**Definition:** $T$ is onto if every vector $\vec{b}$ in the codomain $\mathbb{R}^m$ is the image of **at least one** input vector $\vec{x}$.

**Test:** For $T(\vec{x}) = A\vec{x}$,  
$T$ is onto **if and only if** the columns of $A$ span $\mathbb{R}^m$.

**Practical check:** The rank of $A$ must equal $m$ (the number of rows).  
- If $m > n$ (more rows than columns), $T$ **cannot** be onto.  
- If $m \le n$ and rank = $m$, then it is onto.

---

## 1.6 Relationship Between One-to-One and Onto (Square Matrices)

For an **$n \times n$** matrix $A$ (domain and codomain same dimension):

- If $A$ has $n$ pivots (invertible), then $T$ is **both** one-to-one **and** onto.
- If $A$ has fewer than $n$ pivots, it is **neither** one-to-one nor onto.

This is why your quiz question ("If a $4 \times 4$ matrix has 4 pivots, then any system has a unique solution") was **True**.

---

## 1.7 Composition of Transformations

If $T_1: \mathbb{R}^n \to \mathbb{R}^m$ and $T_2: \mathbb{R}^m \to \mathbb{R}^p$, then the composition $T_2 \circ T_1$ has standard matrix:

$$
A = A_2 \cdot A_1
$$

This allows sequential processing (e.g., rotate, then scale, then project) to be combined into a single matrix multiplication.

---

# Part 2: Applications in Aquaculture with Concrete Examples

---

## 2.1 Image Processing (Computer Vision for Fish Monitoring)

**Method used:** Standard matrix, shears, rotations, projections.

**Example – Fish length measurement from underwater cameras:**  
Underwater cameras suffer from distortion due to water refraction and lens curvature. 

- **Step 1:** Calibrate the camera by imaging a known calibration grid. The transformation from real-world coordinates to pixel coordinates is modeled as a linear (affine) transformation.  
- **Step 2:** Find the standard matrix $A$ by mapping standard basis vectors in the real world to their pixel locations.  
- **Step 3:** Apply the **inverse** of $A$ to each image frame to correct distortion.  
- **Step 4:** Use a **projection** (project onto the x-axis) to collapse the 2D fish image into a 1D profile, making it easy to measure the fish's snout-to-tail length.  
- **Shear correction:** If the fish is tilted, apply a shear transformation to align it horizontally before measurement.

**Outcome:** Accurate, non-invasive biomass estimation without handling the fish.

---

## 2.2 Environmental Sensor Data Fusion

**Method used:** Matrix multiplication, linear combinations, onto/one-to-one checks.

**Example – Predicting dissolved oxygen (DO) from multiple sensors:**  
A smart aquaculture tank has sensors for temperature (T), salinity (S), pH, and turbidity (U). The dissolved oxygen level $y$ is a linear combination of these:

$$
y = a_1 T + a_2 S + a_3 \text{pH} + a_4 U
$$

- Collect historical data to form a matrix $X$ where rows are time points and columns are sensor readings.  
- Use **linear regression** (which solves $X\vec{a} = \vec{y}$ using matrix equations) to find the coefficients $\vec{a}$.  
- Once found, the transformation $T(\text{sensor vector}) = \text{predicted DO}$ is linear.  
- **One-to-one check:** If the sensor readings are linearly independent, the prediction is unique.  
- **Onto check:** If the columns span all possible DO levels, the model can predict any DO value (good for control systems).

**Outcome:** Real-time DO prediction without needing a fragile, fouling-prone DO probe.

---

## 2.3 Feed Optimization (Least-Cost Diet Formulation)

**Method used:** Linear systems, matrix equations, onto transformations.

**Example – Formulating a cost-minimizing fish feed:**  
A fish diet requires minimum amounts of protein (P), fat (F), and carbohydrates (C). Three feed ingredients (soy, fishmeal, corn) have known nutrient profiles.

- Let $x_1, x_2, x_3$ be the amounts (kg) of each ingredient.  
- The nutrient delivery is:

$$
\begin{bmatrix}
\text{Protein} \\
\text{Fat} \\
\text{Carbs}
\end{bmatrix}
= 
\begin{bmatrix}
p_1 & p_2 & p_3 \\
f_1 & f_2 & f_3 \\
c_1 & c_2 & c_3
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
$$

- This is a linear transformation $T(\vec{x}) = A\vec{x}$.  
- To hit a target nutrient profile $\vec{b} = \begin{bmatrix}40\\10\\30\end{bmatrix}$, solve $A\vec{x} = \vec{b}$.  
- **Onto check:** If the columns of $A$ span $\mathbb{R}^3$, then any nutrient profile is achievable (the system is "onto"). If not, some diets are impossible.  
- **One-to-one check:** If $A$ is invertible, the diet is unique; otherwise, multiple ingredient combinations give the same nutrients.

**Outcome:** Cost-optimized, nutritionally complete feed.

---

## 2.4 Growth Modeling (Predicting Fish Size Over Time)

**Method used:** State-space models, matrix exponentiation, one-to-one transformations.

**Example – Tracking fish weight and length over time:**  
Fish growth depends on temperature and feed. A simple linear state-space model:

$$

\vec{x}_{t+1} = A\vec{x}_t + B\vec{u}_t

$$

where:
- $\vec{x}_t = \begin{bmatrix}\text{weight} \\ \text{length}\end{bmatrix}$ at time $t$,
- $\vec{u}_t = \begin{bmatrix}\text{temperature} \\ \text{feed amount}\end{bmatrix}$,
- $A$ is a $2 \times 2$ growth matrix, $B$ is a $2 \times 2$ input matrix.

- The **standard matrix** $A$ is learned from historical growth data.  
- To predict future size, repeatedly apply $A$ (matrix powers).  
- **One-to-one check:** If $A$ is invertible, we can uniquely determine past sizes from present sizes (useful for tracing growth anomalies).  
- **Onto check:** If $A$ is onto, we can reach any desired final size from some initial condition by adjusting feed.

**Outcome:** Accurate harvest time prediction and feed scheduling.

---

## 2.5 Autonomous Feeding (Robotic Feed Distribution)

**Method used:** Homogeneous transformation matrices (4×4), rotations, translations, shears.

**Example – Path planning for an autonomous feeding drone:**  
A drone flies over a circular fish pen, distributing feed evenly. Its position and orientation in 3D space are described by a **homogeneous transformation matrix**:

$$

M = \begin{bmatrix}
R & \vec{t} \\
0 & 1
\end{bmatrix}

$$

where $R$ is a $3 \times 3$ rotation matrix (linear transformation) and $\vec{t}$ is a translation vector.

- To move the drone from point A to point B, we multiply the current transformation matrix by a movement matrix: $M_{\text{new}} = M_{\text{move}} \cdot M_{\text{current}}$.  
- **Shear** transformations model wind drift, adjusting the path in real-time.  
- **Projection:** Project the drone's 3D path onto the 2D water surface to ensure full coverage of the pen.

**Outcome:** Even feed distribution, reduced waste, and improved feed conversion ratio (FCR).

---

## 2.6 Disease Spread Modeling

**Method used:** Markov chain transition matrices, matrix powers, one-to-one/onto analysis.

**Example – Modeling Sea Lice infestation in a salmon farm:**  
Sea lice move through life stages: nauplius, copepodid, chalimus, adult. The population can be modeled as a vector $\vec{x}_t$ of counts in each stage at week $t$.

The transition from week to week is:

$$

\vec{x}_{t+1} = A \vec{x}_t

$$

where $A$ is a $4 \times 4$ transition matrix (e.g., probability of moving to next stage, mortality rates).

- **Matrix powers:** $A^k \vec{x}_0$ predicts the population after $k$ weeks.  
- **One-to-one check:** If $A$ is invertible, we can trace an outbreak back to its source (backward in time).  
- **Onto check:** If $A$ is onto, we can theoretically achieve any desired population distribution (e.g., all stages zero) by some intervention—meaning the system is controllable.  
- Farmers use this to time **chemical treatments** so that they hit the most vulnerable life stage.

**Outcome:** Optimal treatment timing, reduced chemical use, and healthier fish.

---

# Summary Table: Methods ↔ Aquaculture Applications

| Linear Algebra Method | Aquaculture Application |
|------------------------|--------------------------|
| Standard matrix $A = [T(\vec{e}_1) \dots]$ | Camera calibration for fish measurement |
| One-to-one (unique pre-image) | Acoustic tracking: each fish has unique echo |
| Onto (spanning the codomain) | Feed formulation: any nutrient profile achievable |
| Shear transformations | Correcting current-induced net deformation |
| Projection transformations | Collapsing 3D sonar to 1D for biomass estimates |
| Rotation / homogeneous matrices | Drone path planning and orientation |
| Matrix powers ($A^k$) | Growth and disease prediction over time |
| Solving $A\vec{x} = \vec{b}$ | Determining feed mix or treatment dose |

---

If you'd like, I can turn this into a printable study guide or even work through a numerical example (e.g., building the actual matrices for a fish growth model). Just let me know!
