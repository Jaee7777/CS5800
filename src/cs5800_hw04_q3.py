def HUNGARIAN_QUICKSORT(A, low, high):
    # if A is empty, quit procedure.
    if A == []:
        return print("Array is empty.")
    # condition required to run partition.
    if low < high:
        pivot = PARTITION(A, low, high)
        # recursively call quicksort on sub-arrays.
        HUNGARIAN_QUICKSORT(A, low, pivot - 1)
        HUNGARIAN_QUICKSORT(A, pivot + 1, high)
    return


def PARTITION(A, p, c):
    # if A has one element, exit partitiion.
    if len(A) == 1:
        return p
    # run the loop until p == c.
    while p != c:
        if c > p and A[p] > A[c]:
            A[p], A[c] = A[c], A[p]  # swap elements
            p, c = c, p  # swap indices
        elif c < p and A[p] < A[c]:
            A[p], A[c] = A[c], A[p]  # swap elements
            p, c = c, p  # swap indices
        elif c < p:
            c += 1  # cursor moves to the right
        elif c > p:
            c -= 1  # cursor moves to the left
    return p


A = [3, 1, 5, 7, 6, 2, 4]
print(f"Input array is :{A}")
HUNGARIAN_QUICKSORT(A, 0, len(A) - 1)
print(f"Output array is : {A}")
