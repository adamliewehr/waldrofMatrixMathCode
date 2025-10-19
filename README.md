# Matrix Operations and Linear Systems with Python

This repository contains Python scripts and notes covering essential matrix operations, linear systems, and computational methods. The goal is to progress from fundamental matrix arithmetic to using matrices for solving systems of equations, with a final step toward computational methods for larger matrices.

## 🐍 1. Python Basics and Setup

This folder contains introductory material on the Python programming language to ensure a foundational understanding before diving into matrix implementation.

### Files in `pythonBasics/`

* [cite_start]**`introToPython.py`**: This file gives a short intro to some basic Python syntax and concepts[cite: 1].
* [cite_start]**`forLoopsInPython.py`**: This file covers the use of For loops in Python[cite: 8].

---

## 📐 2. Intro to Matrices (`/matrixIntro`)

This section introduces what a matrix is, how to reference its elements, and provides an example of visualization.

### Basic Concepts

[cite_start]A matrix is an array of numbers organized into rows and columns[cite: 3].

* [cite_start]**Example Matrix A** (2 rows, 3 columns, or 2x3, where $\text{R} \times \text{C}$)[cite: 4]:
    $$\text{A} = \begin{bmatrix} 2 & 7 & -4 \\ 6 & 3 & 5 \end{bmatrix}$$
* [cite_start]**Order (Dimensions):** The order of a matrix is simply the rows and columns[cite: 5]. [cite_start]The matrix above would be a **2x3** matrix[cite: 6].
* [cite_start]**Square Matrices:** Square matrices are matrices where the number rows and columns are the same[cite: 6].
    $$\text{C} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$
* [cite_start]**Indexing:** Indexing into a matrix is similar to indexing into arrays in programming[cite: 4].
    * [cite_start]Element $A_{2,3}$ (Row 2, Column 3) would be 5[cite: 5].
    * [cite_start]Element $A_{1,2}$ (Row 1, Column 2) would be 7[cite: 5].
    * [cite_start]Element $A_{2,1}$ (Row 2, Column 1) would be 6[cite: 5].

### Files in `matrixIntro/`

* [cite_start]**`matrixVisualization.py`**: This file shows a basic way to visualize matrices in Python[cite: 2].
* [cite_start]**`basicConcepts.py`**: This file provides an explanation of basic matrix concepts[cite: 3].

---

## ➕ 3. Basic Matrix Operations (`/basicMatrixOperations`)

[cite_start]This folder gives some background on matrix addition, subtraction, and scalar multiplication[cite: 7].

### 3.1. Adding and Subtracting

[cite_start]To add or subtract, simply add or subtract the elements in the same positions[cite: 8]. [cite_start]**You cannot add or subtract matrices with different dimensions**[cite: 9].

$$\text{A} = \begin{bmatrix} 2 & 7 & -4 \\ 6 & 3 & 5 \end{bmatrix} \quad \text{B} = \begin{bmatrix} 3 & 1 & 5 \\ -7 & 4 & 2 \end{bmatrix}$$

* **Addition:**
    $$\text{A} + \text{B} = \begin{bmatrix} 2+3 & 7+1 & -4+5 \\ 6+(-7) & 3+4 & 5+2 \end{bmatrix} = \begin{bmatrix} 5 & 8 & 1 \\ -1 & 7 & 7 \end{bmatrix}$$
* **Subtraction:**
    $$\text{A} - \text{B} = \begin{bmatrix} 2-3 & 7-1 & -4-5 \\ 6-(-7) & 3-4 & 5-2 \end{bmatrix} = \begin{bmatrix} -1 & 6 & -9 \\ 13 & -1 & 3 \end{bmatrix}$$

### 3.2. Scalar Multiplication

[cite_start]Scalar multiplication of matrices involves multiplying every entry in a matrix by a single real number, called a scalar[cite: 10]. [cite_start]This changes the magnitude of each element without altering the matrix's dimensions[cite: 10].

$$\text{A} = \begin{bmatrix} 5 & -2 \\ 7 & 3 \end{bmatrix} \quad \text{B} = \begin{bmatrix} -4 & 6 \\ -2 & 9 \end{bmatrix}$$

* [cite_start]**Example: Find 3A** [cite: 11]
    $$3\text{A} = \begin{bmatrix} 3\times 5 & 3\times (-2) \\ 3\times 7 & 3\times 3 \end{bmatrix} = \begin{bmatrix} 15 & -6 \\ 21 & 9 \end{bmatrix}$$
* **Combined Operations (e.g., 5A - 6B):** You can perform scalar multiplication and then addition/subtraction.
    $$\text{5A} - \text{6B} = 5\begin{bmatrix} 5 & -2 \\ 7 & 3 \end{bmatrix} - 6\begin{bmatrix} -4 & 6 \\ -2 & 9 \end{bmatrix}$$
    * [cite_start]Multiplying B by -6 is an alternative approach that changes the matrix operation from subtraction to addition[cite: 13, 14]:
    $$\text{5A} + (-\text{6B}) = \begin{bmatrix} 25 & -10 \\ 35 & 15 \end{bmatrix} + \begin{bmatrix} 24 & -36 \\ 12 & -54 \end{bmatrix} = \begin{bmatrix} 49 & -46 \\ 47 & -39 \end{bmatrix}$$

### Files in `basicMatrixOperations/`

* [cite_start]**`additionAndSubtraction.py`**: Implementation of matrix addition and subtraction[cite: 8].
* [cite_start]**`scalarMultiplication.py`**: Implementation of scalar multiplication[cite: 10].

---

## ✖️ 4. Advanced Matrix Operations (`/advancedMatrixOperations`)

### Files in `advancedMatrixOperations/`

* [cite_start]**`multiplyingMatrices.py`**: Script for matrix multiplication[cite: 15].

---

## 🔧 5. Solving Systems and Inverses (`/solvingSystemsAndInverses`)

This section focuses on the main application of matrices in mathematics: solving linear systems.

### Files in `solvingSystemsAndInverses/`

* [cite_start]**`solveLinearSystem.py`**: Using matrices to solve linear systems[cite: 15].
* [cite_start]**`matrixInverse.py`**: Calculating matrix inverses[cite: 15].
* [cite_start]**`calculateDeterminant.py`**: Calculating determinants[cite: 15].

---

## 💻 6. Applications and Computation (`/applicationsAndComputation`)

### Files in `applicationsAndComputation/`

* [cite_start]**`matrixApplications.py`**: Demonstrates practical applications of matrices[cite: 16].
* [cite_start]**`largeMatrixComputation.py`**: Focuses on using Python/other programs to work on larger matrices[cite: 16].