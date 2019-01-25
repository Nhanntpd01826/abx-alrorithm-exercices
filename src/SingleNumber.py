class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=2*sum(set(nums))-sum(nums)
        return r