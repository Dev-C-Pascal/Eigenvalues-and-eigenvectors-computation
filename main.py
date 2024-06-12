import numpy as np

Batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
    [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]
])

# випадкова генерація матриці
correct_matrix = A = np.random.uniform(1, 11, size=(3, 3)).astype(int)


def compute_eigenvalues_eigenvectors(matrix):

    # Перевірка на то чи є матриця квадратною
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Матриця повинна бути квадратною.")

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # eigenvalues -> власні значення
    # eigenvectors -> власні вектори

    for i in range(len(eigenvalues)):
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]

        Av = np.dot(matrix, eigenvector)

        # Обчислення λ⋅v
        lambdav = eigenvalue * eigenvector

        # Порівняння A⋅v та λ⋅v
        if np.allclose(Av, lambdav):
            print(
                f"Для власного значення {eigenvalue} та власного вектора {eigenvector} рівність A⋅v = λ⋅v виконується.")
        else:
            print(
                f"Для власного значення {eigenvalue} та власного вектора {eigenvector} рівність A⋅v = λ⋅v не виконується.")

    return eigenvalues, eigenvectors


if __name__ == '__main__':
    print(correct_matrix)
    compute_eigenvalues_eigenvectors(correct_matrix)
