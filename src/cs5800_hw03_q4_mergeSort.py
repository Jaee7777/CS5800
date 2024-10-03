# https://leetcode.com/problems/maximum-product-subarray/
# solve the leet code problem(Maximum Product Subarray)
class Solution:
    # We can simply perform a merge sort, and compare products of two ends.
    def maxProduct(self, nums):
        if len(nums) <= 1:
            print("Array has less than one  element.")
            return
        sort_nums = self.mergeSort(nums)
        left_product = sort_nums[0] * sort_nums[1]
        right_product = sort_nums[-1] * sort_nums[-2]
        if left_product >= right_product:
            return left_product
        else:
            return right_product

    # Define method to perform merge sort.
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        sort_left = self.mergeSort(left)
        sort_right = self.mergeSort(right)
        return self.merge(sort_left, sort_right)

    def merge(self, left, right):
        ans = []
        while left and right:
            if left[0] < right[0]:
                ans.append(left[0])
                left.pop(0)
            else:
                ans.append(right[0])
                right.pop(0)
        if left:
            ans += left
        else:
            ans += right
        return ans


sol = Solution()
# example array to be solved
nums = [2, 3, -2, 4]
print(f"The max product of the array is : {sol.maxProduct(nums)}")
