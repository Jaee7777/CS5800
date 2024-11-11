class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in reversed(range(1, n)):
            if ratings[i - 1] > ratings[i]:
                candy[i - 1] = max(candy[i - 1], candy[i] + 1)

        return sum(candy)


if __name__ == "__main__":
    example = [1, 3, 4, 5, 2]
    sol = Solution()
    print(sol.candy(example))
