num={"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        sum=0
        while i < len(s):
            if i+1==len(s):
                sum +=num[s[i]]
                i+=1
            elif num[s[i]] >= num[s[i+1]]:
                sum+=num[s[i]]
                i+=1
            else:
                sum+=num[s[i+1]]-num[s[i]]
                i+=2
        return sum
        
