"""
binomial_heapq_template.py
Oct 24, 2024
James Kim

the operations that we are interested in are: Insertion, Extraction (or min) and Merging. 
You should note that Insertion and Extraction all revolves some work with Merging. 
Also note that we are inputting items into the queue one at a time; 
meaning that our array of trees (representing the queue) changes with additional or extraction of items.
"""

from math import log, factorial


# function for the number of combinations.
def comb(n, h):
    return factorial(n) // (factorial(h) * factorial(n - h))


def merge(p: list, q: list) -> list:
    """
    Merge two bionmial heaps of the same size and return the merged binomial heap.

    @parameter
    p, list: binomial heap
    q, list: binomial heap

    @return
    list: merged binomial heap
    """
    # find the depth of p.
    n = int(log(len(p), 2))
    # make sure which has a smaller root number.
    if p[0] <= q[0]:
        tree_small, tree_big = p, q
    else:
        tree_small, tree_big = q, p
    # initialize a result array and place the first element.
    result = [tree_small.pop(0)]
    # use combinations to place elements on each depth in a correct order
    for i in range(1, n + 1):
        for x in range(0, comb(n, i - 1)):
            result.append(tree_big.pop(0))
        for y in range(0, comb(n, i)):
            result.append(tree_small.pop(0))
    result.append(tree_big.pop(-1))  # place the last element into the result.
    return result


def deleteMin(p: list):
    """
    return and delete the minimum and maintain the heap-order

    @parameter
    p, list: binomial heap

    @return
    number: previous minimum
    """
    # find min_value to be returned.
    min_value = p[0]
    # find the depth of p.
    n = int(log(len(p), 2))
    # swap root and tail.
    i = -1
    while p[-1] == float("inf"):
        i -= 1
    p[0], p[i] = p[i], p[0]
    # delete min at tail and add float("inf").
    p.pop(i)
    p.append(float("inf"))
    print("print", p)
    # restor heap order.
    print("p after deletemin", p)
    cursor = p[0]
    n_current = n
    i_low = 1
    i_high = comb(n, 1) + 1
    min_child_value = min(p[x] for x in range(i_low, i_high))
    while cursor > min_child_value:
        for i, x in enumerate(p[i_low:i_high]):
            if x == min_child_value:
                cursor = p[i]
                n_current = n_current - (i_high - i)

    for i, tree in enumerate(p):
        print(i, tree)
    return min_value


def insert(p: list, n):
    """
    insert a number to the binomial heap and maintain the heap-order

    @parameter
    p, list: binomial heap
    n, number: number to insert
    """
    pass


### Test merge
assert merge([1, 3], [0, 2]) == [0, 1, 2, 3]
print(merge([1, 3], [0, 2]))
assert merge([0, 2], [1, 3]) == [0, 1, 2, 3]
print(merge([0, 2], [1, 3]))
assert merge([0], [1]) == [0, 1]
print(merge([0], [1]))
assert merge([1], [0]) == [0, 1]
print(merge([1], [0]))
assert merge([7, 12, 8, 13], [3, 5, 4, 9]) == [3, 7, 5, 4, 12, 8, 9, 13]
print(merge([7, 12, 8, 13], [3, 5, 4, 9]))
assert merge([3, 5, 4, 9], [7, 12, 8, 13]) == [3, 7, 5, 4, 12, 8, 9, 13]
print(merge([3, 5, 4, 9], [7, 12, 8, 13]))

### Test deleteMin
arr = [3, 5, 4, 9]
assert deleteMin(arr) == 3
assert arr == [4, 5, 9, float("inf")]
assert deleteMin(arr) == 4
assert arr == [5, 9, float("inf"), float("inf")]
assert deleteMin(arr) == 5
assert arr == [9, float("inf"), float("inf"), float("inf")]
arr = [3, 7, 5, 4, 12, 8, 9, 13]
assert deleteMin(arr) == 3
assert arr == [4, 7, 5, 13, 12, 8, 9, float("inf")]
assert deleteMin(arr) == 4
assert arr == [5, 7, 9, 13, 12, 8, float("inf"), float("inf")]
assert deleteMin(arr) == 5
assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]

arr = [3, 4, 5, 7, 12, 8, 9, 13]
assert deleteMin(arr) == 3
assert arr == [4, 8, 5, 7, 12, 13, 9, float("inf")]
assert deleteMin(arr) == 4
assert arr == [5, 8, 9, 7, 12, 13, float("inf"), float("inf")]
assert deleteMin(arr) == 5
assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]


arr = merge([3, 4, 5, 7, 12, 8, 9, 13], [5, 6, 7, 9, 14, 10, 11, 15])
assert deleteMin(arr) == 3
assert arr == [4, 5, 8, 5, 7, 6, 7, 9, 12, 15, 9, 14, 10, 11, 13, float("inf")]
assert deleteMin(arr) == 4
assert arr == [
    5,
    6,
    8,
    5,
    7,
    10,
    7,
    9,
    12,
    15,
    9,
    14,
    13,
    11,
    float("inf"),
    float("inf"),
]
assert deleteMin(arr) == 5
assert arr == [
    5,
    6,
    8,
    9,
    7,
    10,
    7,
    9,
    12,
    15,
    11,
    14,
    13,
    float("inf"),
    float("inf"),
    float("inf"),
]

arr = merge([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
assert deleteMin(arr) == 3
assert arr == [4, 5, 5, 5, 7, 6, 7, 9, 6, 8, 9, 14, 10, 11, 15, float("inf")]
assert deleteMin(arr) == 4
assert arr == [5, 6, 5, 5, 7, 10, 7, 9, 6, 8, 9, 14, 15, 11, float("inf"), float("inf")]
assert deleteMin(arr) == 5
assert arr == [
    5,
    6,
    6,
    5,
    7,
    10,
    7,
    9,
    11,
    8,
    9,
    14,
    15,
    float("inf"),
    float("inf"),
    float("inf"),
]


### Test insert
arr = merge([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
deleteMin(arr)
deleteMin(arr)
deleteMin(arr)
insert(arr, 11)
assert arr == [
    5,
    6,
    6,
    5,
    7,
    10,
    7,
    9,
    11,
    8,
    9,
    14,
    15,
    11,
    float("inf"),
    float("inf"),
]
insert(arr, 15)
assert arr == [5, 6, 6, 5, 7, 10, 7, 9, 11, 8, 9, 14, 15, 11, 15, float("inf")]
insert(arr, 7)
assert arr == [5, 6, 6, 5, 7, 7, 7, 9, 11, 8, 9, 10, 15, 11, 15, 14]
