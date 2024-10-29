class Solution:
    def maxSum(self, nums):
        # initialize sum result and indices x and y.
        sum_process = []

        for x in range(0, len(nums)):
            result = 0
            for y in range(x, len(nums)):
                result = result + nums[y]
                sum_process.append(result)
        return max(sum_process)


sol = Solution()
# A = [1, 2, 3, -4, 5]
# A = [-2, -3, 4, -1, -2, 1, 5, -3]
A = [-1, 1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23]
A = [1, 2, -4, 8, 16, -32, 64, 128, -256, 512, 1024, -2048]
# A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(f"Input Array is : {A}")
print(f"Max Sum of the array is : {sol.maxSum(A)}")
