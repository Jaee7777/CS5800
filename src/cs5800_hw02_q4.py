import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("N", type=int, help="create an array A with size N")
parser.add_argument("max", type=int, help="pick a maximum integer for an array A")
parser.add_argument("t", type=int, help="pick a threshold t")
args = parser.parse_args()

rnd = np.random.RandomState(10)  # deterministic random data.
A = rnd.randint(args.max, size=args.N)  # create array A with integer values.
B = args.t * A  # create an array B = t * A.

E = 0  # initialize critical event count.
i = 0  # initialize indice i count.
# create for loops that cover all values for i < j
for a_i in A:
    i += 1
    for j in range(i, len(B)):
        if a_i > B[j]:
            E += 1  # add a count to E when critical condition is met.

print(f"Array A is {A}, and t is t {args.t}")
print(f"There are {E} critical events in array A")
