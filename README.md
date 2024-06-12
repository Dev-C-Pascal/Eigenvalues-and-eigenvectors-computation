# Matrix Eigenvalues and Eigenvectors Computation

This project is a Python implementation of a function that computes the eigenvalues and eigenvectors of a square matrix using the NumPy library. It also performs a verification of the equality A⋅v=λ⋅v for each eigenvalue and its corresponding eigenvector.

## Requirements

- Python 3.11
- NumPy library

## Description

The `compute_eigenvalues_eigenvectors` function takes a square matrix as input and returns its eigenvalues and eigenvectors. The function performs the following steps:

1. Checks if the input matrix is square. If not, it raises a `ValueError`.
2. Computes the eigenvalues and eigenvectors of the matrix using `np.linalg.eig`.
3. For each eigenvalue and its corresponding eigenvector, it verifies the equality A⋅v=λ⋅v by calculating both sides and comparing them using `np.allclose`.
4. Prints a message indicating whether the equality holds or not for each eigenvalue and eigenvector pair.
5. Returns the computed eigenvalues and eigenvectors.

## Usage

1. Clone the repository or download the source code.
2. Make sure you have Python 3.11 and NumPy installed.
3. Run the script, and it will demonstrate the usage of the `compute_eigenvalues_eigenvectors` function with an example matrix.

You can also import the function and use it in your own Python code:

```python
import numpy as np
from eigencomputation import compute_eigenvalues_eigenvectors

matrix = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
