from email.policy import default
from operator import index

import numpy as np
from numpy.ma.core import array, shape, count


#### 1. Create a random vector of size N and find the mean value
def rand_mean(N: int) -> float:
    # N is the size of the vector, meaning that the initial length of the list will be N
    return np.random.rand(N).mean()

#### 2. Create a 8x8 matrix and fill it with a checkerboard pattern
def print_checkerboard():
    arr_1 = np.zeros((8,8),dtype=int)
    arr_1[1::2, ::2] = 1
    arr_1[::2, 1::2] = 1
    print(arr_1)


#### 3. Print the minimum and maximum representable value for each numpy scalar type
'''https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars
https://numpy.org/doc/stable/user/basics.types.html#overflow-errors''' # usage of numpy.iinfo and numpy.finfo
def min_max_repr():
    for dtype in [np.int8, np.int32, np.int64]: # Integer Types
        print(np.iinfo(dtype))
    for dtype in [np.float32, np.float64]: # Floating-Point Types
        print(np.finfo(dtype))


#### 4. How to get the n largest values of an array?

def n_largest(n: int) -> np.array:
    """ larg_list = []
        larg_list.append(np.partition(A,-n)[-n:])
        a = np.array(larg_list)""" # solution using np.partition.
    A = np.arange(10000)
    np.random.shuffle(A)
    largest_num_indices = np.argpartition(A,-n)[-n:] # solution using np.argpartition.

    return A[largest_num_indices]
    # hint (argpartition)

# result = n_largest(5)
# print(result)
# # result.size == 5

#### 5. How to compute ((A+B)*(-A/2)) in place (without copy)?
"""I am not sure whether I got the "compute in place" right("""
def compute_in_place(A,B):
    np.add(A, B, out=B)
    np.divide(A, 2, out=A)
    np.negative(A, out=A)
    np.multiply(A, B, out=A)
    return A

A = np.ones(3)*1
B = np.ones(3)*2
print(compute_in_place(A,B))



# pip install numpy (!Inside virtual env)