import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # W
    A = np.array(A)
    x = A.transpose()
    return x
    pass
