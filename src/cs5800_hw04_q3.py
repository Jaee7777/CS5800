def HUNGARIAN_QUICKSORT(A, low, high):
    # initalize counts for comparisons
    cnt = 0
    # if A is empty, quit procedure.
    if A == []:
        return print("Array is empty.")
    # condition required to run partition.
    if low < high:
        pivot, cnt_i = PARTITION(A, low, high)
        # recursively call quicksort on sub-arrays.
        cnt_l = HUNGARIAN_QUICKSORT(A, low, pivot - 1)
        cnt_r = HUNGARIAN_QUICKSORT(A, pivot + 1, high)
        # sum up all the number of comparisons
        cnt = cnt + cnt_l + cnt_r + cnt_i
    return cnt


def PARTITION(A, p, c):
    # initalize comparison count
    cnt = 0
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
            cnt += 1  # count number of comparison
            c += 1  # cursor moves to the right
        elif c > p:
            cnt += 1  # count number of comparison
            c -= 1  # cursor moves to the left
        print(A)  # show the process of sorting
    print(f"Number of comparisons for this PARTITION is : {cnt}")
    return p, cnt


A = [3, 1, 5, 7, 6, 2, 4]
print(f"Input array is :{A}")
comp = HUNGARIAN_QUICKSORT(A, 0, len(A) - 1)
print(f"Output array is : {A}")
print(f"Total number of comparisons is : {comp}")
