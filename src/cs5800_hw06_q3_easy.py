class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)  # create an array of zeros with length n+1.
        for i in range(1, n + 1):  # loop through i = 1, 2, .., n.
            # i & 1 = 0 if i is an even number.
            # i & 1 = 1 if i is an odd number.
            ans[i] = ans[i // 2] + (i & 1)
        return ans


if __name__ == "__main__":
    sol = Solution().countBits(5)
    print(sol)
