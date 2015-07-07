class ShapeException(Exception):
    pass


def vector_add():
    # This is the addition of 2 vectors
    vector_a = [4, 8, 3]
    vector_b = [1, 2, 6]

    for i, bi in enumerate(vector_b): vector_a[i] += bi
    print(vector_a)


def vector_sub():
    # This is the subtraction of 2 vectors
    vector_c = [4, 8, 3]
    vector_d = [1, 2, 6]

    for i, bi in enumerate(vector_d): vector_c[i] -= bi
    print(vector_c)


def vector_multiply():
    # This is where you multiply a vector by a Scalar(number)
    vector_multi = [a*b for a, b in zip([4, 8, 3,], [1, 2, 6])]
    print(vector_multi)


def vector_mean():
    # This is the mean of multiple vectors
    vector_g = [4, 8, 3]
    vector_h = [1, 2, 6]

    for i, bi in enumerate(vector_h): vector_g[i] += bi / 2
    print(vector_g)


def dot_product():
    # This is where we do some dot product stuff
    vector_i = [4, 8, 3]
    vector_j = [1, 2, 6]

    dot =sum(x*y for x, y in zip(vector_i, vector_j))
    print(dot)


def magnitude():
    # This is the sqrt of vector * vector(dot)
    dot = 38
    new_magnitude = sum(dot*dot)**0.5
    print(new_magnitude)


def matrix_add():
    # This is where I add 2 matrix together
    A = [[9, 4, 1],
         [5, 2, 8],
         [7, 3, 6]]

    B = [[14, 4, 2],
         [5, 16, 4],
         [7, 11, 21]]

    new_matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    for r in range(len(A)):
        for c in range(len(A[0])):
            new_matrix[r][c] = A[r][c] + B[r][c]
    print(new_matrix)


def matrix_sub():
    # Subtraction of 2 matrix
    # This is not right
    A = [[9, 4, 1],
         [5, 2, 8],
         [7, 3, 6]]

    B = [[14, 4, 2],
         [5, 16, 4],
         [7, 11, 21]]

    new_matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    for r in range(len(A)):
        for c in range(len(A[0])):
            new_matrix[r][c] = A[r][c] - B[r][c]
    print(new_matrix)


def matrix_scalar_multiply():
    # Multiply a matrix by a scalar(number)
    matrix_list = [[2, 2], [9, 5], [3, 7]]

    for this in matrix_list:
        for that in this:
            print(that * 2)


def matrix_multiply():
    # Multiply a matrix by a matrix
    # I do not think this is working correctly.
    A = [[9, 4, 1],
         [5, 2, 8],
         [7, 3, 6]]

    B = [[14, 4, 2],
         [5, 16, 4],
         [7, 11, 21]]

    new_matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    for r in range(len(A)):
        for c in range(len(A[0])):
            new_matrix[r][c] = A[r][c] * B[r][c]
    print(new_matrix)