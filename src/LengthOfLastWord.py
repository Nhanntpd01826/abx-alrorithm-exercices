class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split()
        if len(a) == 0:
            return 0
        return len(a[-1])    
