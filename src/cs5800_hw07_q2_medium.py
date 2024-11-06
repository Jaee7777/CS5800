class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        result = list(map(str, nums))  # convert integers to strings.
        result.sort(key=lambda x: x * 9, reverse=True)  # nums[i]<=10**9.
        if result[0] == "0":  # If the largest number is 0,
            return "0"  # retrn 0, instead of multiple 0.
        return "".join(result)  # sum up sorted strings to a single string.


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    sol = Solution().largestNumber(nums)
    print(sol)
