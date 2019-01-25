class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        if len(nums)<2:
            return len(nums)       
        for i in range(len(nums)):
            if nums[t]!= nums[i]: 
                t+=1 
                nums[t] = nums[i]
        return t + 1
                