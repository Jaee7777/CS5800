class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        for i in range(len(nums) // 2):
            result += min(nums[2 * i], nums[2 * i + 1])
        return result


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    sol = Solution().arrayPairSum(nums)
    print(sol)
