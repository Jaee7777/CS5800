# Structure for an item which stores weight and
# corresponding value of Item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


# Main greedy function to solve problem
def fractionalKnapsack(W, arr):

    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # Result(value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:

        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit

        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.profit * W / item.weight
            break

    # Returning final value
    return finalvalue


# Driver Code
if __name__ == "__main__":
    W = 20
    arr = [Item(480, 4), Item(500, 5), Item(480, 6), Item(490, 7), Item(520, 8)]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
