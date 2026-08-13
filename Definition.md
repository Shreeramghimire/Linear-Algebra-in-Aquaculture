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
|\\
|\\
|
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

---

## Elementary Row Operations

**Definition:** Elementary row operations are three mathematically valid transformations that alter a matrix's structure without changing the solution set of its underlying system. These operations are the tools we use to systematically solve systems.

**The Three Operations:**

| Operation | Notation | Description |
|-----------|----------|-------------|
| **Row Swapping** | $R_i \leftrightarrow R_j$ | Interchange two rows completely |
| **Row Scaling** | $cR_i \to R_i$ | Multiply every entry in a row by a non-zero constant $c$ |
| **Row Addition** | $R_i + cR_j \to R_i$ | Add a scalar multiple of one row to another row |

**Aquaculture Application:**
- **Row Swapping:** Bringing a row with a non-zero first entry to the top to create a clean pivot
- **Row Scaling:** Converting 30 to 1 by multiplying $R_2$ by $1/30$
- **Row Addition:** Eliminating the 30 below the first pivot by $R_2 - 30R_1$

---

## Pivot (Leading Entry)

**Definition:** A pivot, also called a leading entry, is the first non-zero numerical coefficient in a matrix row when reading from left to right. Pivots are the anchors used to guide elimination steps.

**Aquaculture Example:** In the matrix below, the pivots are circled:

$$\begin{bmatrix}
\boxed{1} & 1 & 1 & 300 \\
0 & \boxed{-15} & -20 & -3750 \\
0 & 0 & \boxed{3} & 450
\end{bmatrix}$$

Each pivot anchors a column. The goal of Gaussian elimination is to create a triangular pattern of pivots, then scale them to 1.

**Rule:** A pivot must be non-zero. If a pivot is zero, we swap rows with a lower row containing a non-zero entry in that column.

---

## Row Echelon Form (REF)

### Definition

A matrix is in **Row Echelon Form (REF)** when it satisfies the following conditions:

1. **All zero rows are at the bottom** — Any row consisting entirely of zeros must appear below all non-zero rows.
2. **Staggered pivots** — The leading entry (pivot) in each non-zero row must be strictly to the right of the pivot in the row above it.
3. **Entries below each pivot are zero** — All entries below a pivot must be zero.

### REF Structure Example

$$
\begin{bmatrix}
\boxed{1} & c & c & c \\
0 & \boxed{c} & c & c \\
0 & 0 & \boxed{c} & c
\end{bmatrix}
$$

where $c$ represents any number, including zero.

The boxed entries represent the **pivots**. Notice how each pivot moves to the right as we move down the rows.

### Aquaculture Example: REF

Consider the augmented matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & 300 \\
30 & 15 & 10 & 5250 \\
1 & -2 & 0 & 0
\end{bmatrix}
$$

After applying elementary row operations, it can be transformed into:

$$
\begin{bmatrix}
1 & 1 & 1 & 300 \\
0 & -15 & -20 & -3750 \\
0 & 0 & 3 & 450
\end{bmatrix}
$$

This matrix is in **Row Echelon Form (REF)** because:

- The first pivot is in column 1.
- The second pivot is in column 2.
- The third pivot is in column 3.
- Each pivot is to the right of the pivot above it.
- All entries below each pivot are zero.
- There are no zero rows in this example.

### Why REF Matters

REF reveals the **structure of a system of linear equations** and makes the system easier to solve using **back-substitution**.

Starting from the bottom row:

$$
3x_3 = 450
$$

We can solve for $x_3$ first, then substitute its value into the second row, and finally solve for $x_1$.

> **Important:** If a row of the form
>
> $$
> \begin{bmatrix}
> 0 & 0 & \cdots & 0 & | & c
> \end{bmatrix},
> \qquad c \neq 0
> $$
>
> appears, it represents a contradiction such as $0 = c$. Therefore, the system has **no solution**.
---

## Reduced Row Echelon Form (RREF)

**Definition:** Reduced Row Echelon Form is an advanced matrix structure meeting all REF requirements, with two additional constraints:

1. **Each pivot equals exactly 1** — Every leading entry is scaled to 1
2. **Each pivot is the only non-zero entry in its entire column** — All entries above and below a pivot are zero

**RREF Structure Example:**

$$
\begin{bmatrix}
\boxed{1} & 0 & 0 & c \\
0 & \boxed{1} & 0 & c \\
0 & 0 & \boxed{1} & c
\end{bmatrix}
$$

**Example (RREF):**

$$
\begin{bmatrix}
1 & 0 & 0 & 100 \\
0 & 1 & 0 & 50 \\
0 & 0 & 1 & 150
\end{bmatrix}
$$

**Why RREF Matters:** RREF provides the solution directly without back-substitution. When the left side is the identity matrix (diagonal of 1s), the right column contains the solution. This is the gold standard for solving linear systems.

---
