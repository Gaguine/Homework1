from email.policy import default
from operator import index

import numpy as np
from numpy.ma.core import array, shape, count


#### 1. Create a random vector of size N and find the mean value
def rand_mean(N: int) -> float:
    # N is the size of the vector, meaning that the initial length of the list will be N
    num_list = []
    for num in range(N): num_list.append(num) # create a list from the number provided by the user
    vector = np.array(num_list)
    return vector.mean()

#### 2. Create a 8x8 matrix and fill it with a checkerboard pattern
def print_checkerboard():
    arr_1 = np.zeros((8,8),dtype=int)
    for y in range(arr_1.shape[0]):
        for x in range(arr_1.shape[1]):
            if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
                arr_1[x, y] = 1
    print(arr_1)

print_checkerboard()
'''
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
....

'''


#### 3. Print the minimum and maximum representable value for each numpy scalar type

def min_max_repr():
    for dtype in [np.int8, np.int32, np.int64]:
        ...
    for dtype in [np.float32, np.float64]:
        ...


#### 4. How to get the n largest values of an array?

def n_largest(n: int) -> np.array:
    A = np.arange(10000)
    np.random.shuffle(A)
    # hint (argpartition)

result = n_largest(5)
# result.size == 5

#### 5. How to compute ((A+B)*(-A/2)) in place (without copy)?

def compute_in_place():
    A = np.ones(3)*1
    B = np.ones(3)*2




# pip install numpy (!Inside virtual env)