class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        sum = 0
        for i in range(0, len(nums)):
            sum = sum + nums[i]
            if sum > a:
                   a = sum
            if sum < 0:
                   sum = 0
        return a
