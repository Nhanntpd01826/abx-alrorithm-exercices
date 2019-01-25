class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        i = 0
        size = len(nums)
        while i < size and nums[i] != 0:
            i += 1
        j = i
        while i < size:
            while i < size and nums[i] == 0:
                i += 1
            if i < size:
                nums[j] = nums[i]
                i += 1
                j += 1
        while j < size:
            nums[j] = 0
            j += 1
        
        

        
        
    
    