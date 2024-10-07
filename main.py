def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
        if n <= 0:
            matrix.append([])
        elif m <= 0:
            matrix.append([])
        else:
            return matrix

matrix_1 = get_matrix(2, 2, 10)
matrix_2 = get_matrix(4, 7, 58)
matrix_3 = get_matrix(5, 7, 15)

print(matrix_1)
print(matrix_2)
print(matrix_3)