def printPascal(n: int):
    arr = [[0 for x in range(n)] for y in range(n)]
    for line in range(0, n):
        for i in range(0, line + 1):
            if i is 0 or i is line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")
            else:
                arr[line][i] = arr[line - 1][i - 1] + arr[line - 1][i]
                print(arr[line][i], end=" ")
        print("\n", end="")


def Pascal(n, k):
    triangle = [
        [0 for x in range(n)] for y in range(n)
    ]  # n-by-n array to store values of the triangle.
    stop_point = n * (n - 1) / 2 + k  # stop the loop at n-th row, k-th entry
    chk = 0  # initialize chk to check which element are we at in the triangle.
    for row in range(0, n):  # loop through the rows.
        for col in range(0, row + 1):  # loop through columns of the row.
            if row == 0:  # this is the topmost entry of the triangle.
                triangle[row][col] = 1
                chk += 1  # increase chk.
            else:
                triangle[row][col] = (
                    triangle[row - 1][col - 1] + triangle[row - 1][col]
                )  # given equation.
                chk += 1  # increase chk.
            if chk == stop_point:  # we have reached n-th row, k-th entry.
                entry_k = triangle[row][col]  # record the final answer.
                break  # break the loop since we have found the answer.
    return entry_k  # return the final answer.


print(Pascal(10, 7))  # 3th entry on 10th row.

printPascal(10)  # run the code for case where n = 5, k = 2
