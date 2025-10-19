# Matrix Operations and Linear Systems with Python

This repository contains Python scripts and notes covering essential matrix operations, linear systems, and computational methods. The goal is to progress from fundamental matrix arithmetic to using matrices for solving systems of equations, with a final step toward computational methods for larger matrices.

> **Note:** The core mathematical definitions and examples in this README are derived from the accompanying **Notes.rtf** source file in the root directory.

---

## 🐍 1. Python Basics and Setup

This folder contains introductory material on the Python programming language to ensure a foundational understanding before diving into matrix implementation.

### Files in `pythonBasics/`

* **`introToPython.py`**: This file gives a short intro to some basic Python syntax and concepts.
* **`forLoopsInPython.py`**: This file covers the use of For loops in Python.

---

## 📐 2. Intro to Matrices (`/matrixIntro`)

This section introduces what a matrix is, how to reference its elements, and provides an example of visualization.

### Basic Concepts

A matrix is an array of numbers organized into rows and columns.

* **Example Matrix A** (2 rows, 3 columns, or $2 \times 3$, where $\text{R} \times \text{C}$):
    $$\text{A} = \begin{bmatrix} 2 & 7 & -4 \\ 6 & 3 & 5 \end{bmatrix}$$
* **Order (Dimensions):** The order of a matrix is simply the rows and columns. The matrix above would be a **$2 \times 3$** matrix.
* **Square Matrices:** Square matrices are matrices where the number rows and columns are the same.
    $$\text{C} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$
* **Indexing:** Indexing into a matrix is similar to indexing into arrays in programming. Element $A_{2,3}$ (Row 2, Column 3) would be 5.

### Files in `matrixIntro/`

* **`matrixVisualization.py`**: This file shows a basic way to visualize matrices in Python.
* **`basicConcepts.py`**: This file provides an explanation of basic matrix concepts.

---

## ➕ 3. Basic Matrix Operations (`/basicMatrixOperations`)

This folder gives some background on matrix addition, subtraction, and scalar multiplication.

### 3.1. Adding and Subtracting

To add or subtract, simply add or subtract the elements in the same positions. **You cannot add or subtract matrices with different dimensions**.

$$\text{A} = \begin{bmatrix} 2 & 7 & -4 \\ 6 & 3 & 5 \end{bmatrix} \quad \text{B} = \begin{bmatrix} 3 & 1 & 5 \\ -7 & 4 & 2 \end{bmatrix}$$

* **Addition:**
    $$\text{A} + \text{B} = \begin{bmatrix} 5 & 8 & 1 \\ -1 & 7 & 7 \end{bmatrix}$$
* **Subtraction:**
    $$\text{A} - \text{B} = \begin{bmatrix} -1 & 6 & -9 \\ 13 & -1 & 3 \end{bmatrix}$$

### 3.2. Scalar Multiplication

Scalar multiplication of matrices involves multiplying every entry in a matrix by a single real number, called a **scalar**. This changes the magnitude of each element without altering the matrix's dimensions.

$$\text{A} = \begin{bmatrix} 5 & -2 \\ 7 & 3 \end{bmatrix} \quad \text{B} = \begin{bmatrix} -4 & 6 \\ -2 & 9 \end{bmatrix}$$

* **Example: Find 3A**
    $$3\text{A} = \begin{bmatrix} 15 & -6 \\ 21 & 9 \end{bmatrix}$$
* **Combined Operations (e.g., 5A - 6B):**
    $$\text{5A} - \text{6B} = \begin{bmatrix} 49 & -46 \\ 47 & -39 \end{bmatrix}$$

### Files in `basicMatrixOperations/`

* **`additionAndSubtraction.py`**: Implementation of matrix addition and subtraction.
* **`scalarMultiplication.py`**: Implementation of scalar multiplication.

---

## ✖️ 4. Advanced Matrix Operations (`/advancedMatrixOperations`)

### Files in `advancedMatrixOperations/`

* **`multiplyingMatrices.py`**: Script for matrix multiplication.

---

## 🔧 5. Solving Systems and Inverses (`/solvingSystemsAndInverses`)

This section focuses on the main application of matrices in mathematics: solving linear systems.

### Files in `solvingSystemsAndInverses/`

* **`solveLinearSystem.py`**: Using matrices to solve linear systems.
* **`matrixInverse.py`**: Calculating matrix inverses.
* **`calculateDeterminant.py`**: Calculating determinants.

---

## 💻 6. Applications and Computation (`/applicationsAndComputation`)

### Files in `applicationsAndComputation/`

* **`matrixApplications.py`**: Demonstrates practical applications of matrices.
* **`largeMatrixComputation.py`**: Focuses on using Python/other programs to work on larger matrices.

---

Now that the file is ready, would you like me to draft the actual Python code for the first file in the sequence, `introToPython.py`?