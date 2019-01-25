class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        for i in range(1, x+1):
            if i*i>x:
                return i-1
