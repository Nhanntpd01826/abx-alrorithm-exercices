class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            try:
                del nums[nums.index(val)]
            except:
                 pass
             