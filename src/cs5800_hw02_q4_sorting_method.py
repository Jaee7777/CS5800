import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("N", type=int, help="create an array A with size N")
parser.add_argument("max", type=int, help="pick a maximum integer for an array A")
parser.add_argument("t", type=int, help="pick a threshold t")
args = parser.parse_args()

rnd = np.random.RandomState(10)  # deterministic random data
A = rnd.randint(args.max, size=args.N)  # create array A with integer values.
A_lst = A.tolist()  # convert A to list data type to run merge sort function.


# define a function for merge sort which has a complexity of n log n.
# this function uses list datatype of python instead of numpy array.
def merge_sort(lst):
    if len(lst) <= 1:  # when there is only one element left, stop spliting.
        return lst
    middle = len(lst) // 2  # find the middle point.
    left = lst[:middle]  # split left and right of the middle point.
    right = lst[middle:]
    sorted_left = merge_sort(left)  # run recursive function.
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []  # inittalize an empty list
    while left and right:  # ruun until either left or right is []
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # append remaining last element to result
    if left:
        result += left
    if right:
        result += right
    return result

# now we sort A_lst
A_lst_sorted = merge_sort(A_lst)

# we know have to use a search algorithm to find 

print(A)
print(A_lst_sorted)
print(args.t)
