class Solution:
    def maximumProduct(self, nums):
        """      
        0, 1: 	 2 so am dau tien
        -1,-2,-3: 3 so duong cuoi cung
        """ 
        nums.sort()        
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
