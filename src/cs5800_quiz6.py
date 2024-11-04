from math import log, factorial


# function for the number of combinations.
def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def Pascal_Tri(n, k):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            pass

    return


def printPascal(n: int):

    # An auxiliary array to store
    # generated pascal triangle values
    arr = [[0 for x in range(n)] for y in range(n)]

    # Iterate through every line
    # and print integer(s) in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line number
        for i in range(0, line + 1):

            # First and last values
            # in every row are 1
            if i is 0 or i is line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")

            # Other values are sum of values
            # just above and left of above
            else:
                arr[line][i] = arr[line - 1][i - 1] + arr[line - 1][i]
                print(arr[line][i], end=" ")
        print("\n", end="")


# Driver Code
n = 5
printPascal(n)


if __name__ == "__main__":
    # print(Pascal_Tri(5, 2))
    print(comb(5, 2))
    n = 7
    printPascal(n)
