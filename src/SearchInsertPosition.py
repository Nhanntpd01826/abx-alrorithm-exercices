class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if target <= nums[i]:
                j=i
                break            
            if target > nums[i]:
                j=i+1
        return j
        
