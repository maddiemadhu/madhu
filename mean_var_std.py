import numpy as np

def calculate(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Input matrix must be 3x3")

    matrix = np.array(matrix)

    row_mean = np.mean(matrix, axis=1)
    col_mean = np.mean(matrix, axis=0)
    ele_mean = np.mean(matrix)

    row_var = np.var(matrix, axis=1)
    col_var = np.var(matrix, axis=0)
    ele_var = np.var(matrix)

    row_std = np.std(matrix, axis=1)
    col_std = np.std(matrix, axis=0)
    ele_std = np.std(matrix)

    row_max = np.max(matrix, axis=1)
    col_max = np.max(matrix, axis=0)
    ele_max = np.max(matrix)

    row_sum = np.sum(matrix, axis=1)
    col_sum = np.sum(matrix, axis=0)
    ele_sum = np.sum(matrix)

    calculations = {
        'mean': {
            'row': row_mean.tolist(),
            'col': col_mean.tolist(),
            'element': ele_mean.item()
        },
        'variance': {
            'row': row_var.tolist(),
            'col': col_var.tolist(),
            'element': ele_var.item()
        },
        'standard deviation': {
            'row': row_std.tolist(),
            'col': col_std.tolist(),
            'element': ele_std.item()
        },
        'max': {
            'row': row_max.tolist(),
            'col': col_max.tolist(),
            'element': ele_max.item()
        },
        'sum': {
            'row': row_sum.tolist(),
            'col': col_sum.tolist(),
            'element': ele_sum.item()
        }
    }

    return calculations
