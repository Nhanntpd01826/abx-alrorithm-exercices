class Solution:
    def merge(self, nums1, m, nums2, n):        
        for i in range(n):
            nums1[-i-1]=nums2[i]
        nums1.sort()
        
                    
