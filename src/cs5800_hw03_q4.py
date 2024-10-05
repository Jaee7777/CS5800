# https://leetcode.com/problems/maximum-product-subarray/
# solve the leet code problem(Maximum Product Subarray)
class Solution:
    def maxProduct(self, nums):
        # There can be either positive or negative number as a product.
        # initial max (for positive) and min (for negative) values are nums[0]
        pos_product = nums[0]
        neg_product = nums[0]
        result = nums[0]

        # loop starting from the second element of nums array.
        for n in nums[1:]:
            # if current element n is negative, max and min will be switched.
            if n < 0:
                pos_product, neg_product = neg_product, pos_product
            # update the max and min of the positive/negative number product.
            pos_product = max(n, pos_product * n)
            neg_product = min(n, neg_product * n)
            result = max(result, pos_product)
        return result


sol = Solution()
A = [1, 2, 3, -4, 5]
print(f"Max product of the array is : {sol.maxProduct(A)}")
