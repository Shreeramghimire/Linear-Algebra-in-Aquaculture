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

### General Form

A matrix with $m$ rows and $n$ columns is called an **$m \times n$ matrix**.

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

where $a_{ij}$ refers to the element in **row $i$ and column $j$**.

### Aquaculture Example: Coefficient Matrix

For example, consider the following coefficient matrix:

$$
A =
\begin{bmatrix}
1 & 1 & 1 \\
30 & 15 & 10 \\
1 & -2 & 0
\end{bmatrix}
$$

This is a **$3 \times 3$ matrix**, meaning it contains 3 rows and 3 columns.

| Row | Column 1 | Column 2 | Column 3 |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 30 | 15 | 10 |
| 3 | 1 | -2 | 0 |

Here, for example:

- $a_{11} = 1$ → row 1, column 1
- $a_{23} = 10$ → row 2, column 3
- $a_{32} = -2$ → row 3, column 2
Each row represents a constraint (mass, protein, ratio), and each column represents an ingredient (Fishmeal, Soy, Wheat).

---
## Augmented Matrix

**Definition:** An augmented matrix is derived by appending the columns of two matrices, typically the coefficients of a linear system on the left and the constant values (outputs) on the right, separated by a vertical line.


### General Form: Augmented Matrix

An **augmented matrix** combines the coefficient matrix $A$ with the right-hand-side vector $\mathbf{b}$.

$$
\left[
\begin{array}{ccc|c}
a_{11} & a_{12} & \cdots & b_1 \\
a_{21} & a_{22} & \cdots & b_2 \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & b_m
\end{array}
\right]
$$

The vertical line $|$ separates the **coefficient matrix** from the **right-hand-side values**.

### Aquaculture Example

For an aquaculture system with three unknowns, the augmented matrix can be written as:

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 300 \\
30 & 15 & 10 & 5250 \\
1 & -2 & 0 & 0
\end{array}
\right]
$$

This represents the system of linear equations:

$$
\begin{aligned}
x_1 + x_2 + x_3 &= 300 \\
30x_1 + 15x_2 + 10x_3 &= 5250 \\
x_1 - 2x_2 &= 0
\end{aligned}
$$

The matrix can also be viewed as:

$$
\left[
\begin{array}{ccc}
1 & 1 & 1 \\
30 & 15 & 10 \\
1 & -2 & 0
\end{array}
\begin{array}{c}
\\ \:
\\ \:
\\ \:
\end{array}
\begin{array}{c}
300 \\
5250 \\
0
\end{array}
\right]
$$


where:

- The **left side** contains the coefficient matrix $A$.
- The **right side** contains the vector of constants $\mathbf{b}$.
- The vertical line $|$ separates $A$ from $\mathbf{b}$.
