import math


class ShapeException(Exception):
    pass


def shape(*vector):
    if type(vector[0]) is int:
        return len(vector)
    elif type(vector[0]) is list:
        return len(vector), len(vector[0])


def vector_sum(*vectors):
    for vector in vectors:
        if shape(vector) != shape(vectors[0]):
            raise ShapeException("These do not match")

    return [sum([vector[i] for vector in vectors])
        for i in range(len(vectors[0]))]


def vector_add(a, p):
    # This is the addition of 2 vectors
    if shape(a) != shape(p):
        raise ShapeException("These do not match")

    return [a[x] + p[x] for x in range(len(a))]


def vector_sub(a, p):
    # This is the subtraction of 2 vectors
    if shape(a) != shape(p):
        raise ShapeException("These do not match")

    return [a[x] - p[x] for x in range(len(a))]


def vector_multiply(vector, scalar):
    # This is where you multiply a vector by a Scalar(number)
        return[vector[x]*scalar for x in range(len(vector))]


def matrix_row(matrix, row_idx):
    return matrix[row_idx]


def matrix_col(matrix, col_idx):

    return [matrix[col_idx] for matrix in matrix]


def vector_mean(*vectors):
    # This is the mean of multiple vectors
    # add the 2 vectors together then divide by len() of the vectors
    return vector_multiply(vector_sum(*vectors), (1 / len(vectors)))


def dot(a, b):
    # This is where we do some dot product stuff
    if shape(a) != shape(b):
        raise ShapeException
    return sum(a[x]*b[x] for x in range(len(a)))


def magnitude(vector):
    # This is the sqrt of vector * vector(dot)
    return math.sqrt(dot(vector, vector))


def matrix_add(x, y):
    # This is where I add 2 matrix together
    return [sum(x[a] + y[a]) for a in range(len(x))]


def matrix_sub(x, y):
    # Subtraction of 2 matrix

    return [sum(x[a] - y[a]) for a in range(len(x))]


def matrix_scalar_multiply(matrix, scalar):
    # Multiply a matrix by a scalar(number)
    return [[line*scalar for line in matrix[x]]
        for x in range(len(matrix))]


# def matrix_multiply():
#     # Multiply a matrix by a matrix
#     pass