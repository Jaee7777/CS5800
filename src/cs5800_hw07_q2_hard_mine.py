ratings = [1, 2, 2, 5, 3, 2, 3, 4, 5, 4, 3]
n = len(ratings)

candy_min = 0  # minimum number of candies at the moment.
candy = [candy_min] * len(ratings)  # array to store number of candies.

for i, r in enumerate(ratings):
    if i == 0 and r <= ratings[1]:
        candy[i] = 1
        continue
    elif i == 0:
        continue
    if i == n - 1 and r <= ratings[-2]:
        candy[i] = 1
        continue
    elif i == n - 1:
        continue

    # If both neighbors are larger, one candy is given.
    if ratings[i - 1] >= r and r <= ratings[i + 1]:
        candy[i] = 1


print(ratings)
print(candy)
print(candy_min)
