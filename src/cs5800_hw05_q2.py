def merge(p, q):
    if p[0] <= q[0]:
        return p + q
    else:
        return q + p
    # restore the heap order


def deleteMin(p):
    # find the last non-empty node.
    i = -1
    while p[i] is None:
        i -= 1
    # swap the first and the last non-empty nodes
    p[0], p[i] = p[i], p[0]
    p.pop(i)
    p.append(None)
    # restore the heap order.
    return p[0]


def insert(p, n):
    # replace the empty slot to 'n', if p[-1] is an empty slot.
    if p[-1] is None:
        p.pop()
        p.append(n)
    # restore the heap order.
    heap_order(p)
    return


def heap_order(A):
    # let r is the root, and c is the cursor.
    c = -1
    # search for the last non-empty element.
    while A[c] is None:
        c -= 1
    l = len(A) + c + 1  # lenght of the non-empty array
    return


A = [1, 3, 2, 8]
B = [5, 4, 7, 9, None, None]
print(merge(B, A))
print(deleteMin(A), "deleteMin")
print(A)

insert(B, 11)
print(B)
