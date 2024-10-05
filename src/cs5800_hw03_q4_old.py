# https://leetcode.com/problems/maximum-product-subarray/
# solve the leet code problem(Maximum Product Subarray)
class Solution:
    def maxProduct(self, nums):
        while len(nums) > 2:
            left_product = nums[0] * nums[1]
            right_product = nums[-1] * nums[-2]
            if left_product >= right_product:
                result = left_product
                nums.pop(-1)
            else:
                result = right_product
                nums.pop(0)
        return result


sol = Solution()
A = [2, 3, -2, 4]
print(f"Max product of the array is : {sol.maxProduct(A)}")
