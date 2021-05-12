nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5, 4, -1, 7, 8]


class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        max_global = max_local = nums[0]

        for i in range(1, len(nums)):
            max_local = max(nums[i], max_local + nums[i])
            max_global = max(max_global, max_local)

        return max_global


sol = Solution()
print(sol.maxSubArray(nums1))
print(sol.maxSubArray(nums2))
