## Linear Equation

**Definition:** A linear equation is an algebraic equation where each term is either a constant or the product of a constant and a single variable raised to the first power. No variable is multiplied by another variable, and no variable appears with an exponent other than 1.

**General Form:**
$$a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$$

Where:
- $a_1, a_2, \dots, a_n$ are coefficients (constants)
- $x_1, x_2, \dots, x_n$ are variables
- $b$ is the constant term (the output or result)

**Aquaculture Example:**
$$30x + 15y + 10z = 5250$$

Here, $x$ = Fishmeal (kg), $y$ = Soy Protein (kg), $z$ = Wheat Flour (kg). The coefficients (30, 15, 10) represent protein yield per kilogram, and 5250 is the total protein target.

---
## System of Linear Equations

**Definition:** A system of linear equations is a collection of two or more linear equations sharing the same set of variables. The goal is to find values for the variables that satisfy **all equations simultaneously**.

**General Form:**

a₁₁x₁ + a₁₂x₂ + ⋯ + a₁ₙxₙ = b₁
a₂₁x₁ + a₂₂x₂ + ⋯ + a₂ₙxₙ = b₂
       ⋮
aₘ₁x₁ + aₘ₂x₂ + ⋯ + aₘₙxₙ = bₘ

**Aquaculture Example:**

x + y + z = 300           (Total mass)
30x + 15y + 10z = 5250    (Protein target)
x − 2y = 0                (Ratio constraint)

**Key Insight:** A solution to a system is a set of values that makes all equations true simultaneously. In aquaculture, this means finding feed ingredient weights that meet all nutritional, mass, and biological constraints at once.

---
## Matrix

**Definition:** A matrix is a rectangular array of numbers arranged in horizontal rows and vertical columns. It compactly stores the numerical parameters of a system, allowing systematic manipulation.

**General Form:**
$$A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$$

**Notation:** A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix. $a_{ij}$ refers to the element in row $i$, column $j$.

**Aquaculture Example (Coefficient Matrix):**
$$A = \begin{bmatrix}
1 & 1 & 1 \\
30 & 15 & 10 \\
1 & -2 & 0
\end{bmatrix}$$

Each row represents a constraint (mass, protein, ratio), and each column represents an ingredient (Fishmeal, Soy, Wheat).

---
