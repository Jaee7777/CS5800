def rod_cut_cost(price, n, cost):
    revenue = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        max_revenue = price[i - 1]
        for j in range(i):
            max_revenue = max(max_revenue, price[j] + revenue[i - j - 1] - cost)
        revenue[i] = max_revenue
    return revenue[-1]


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(rod_cut_cost(price, n=4, cost=1))
