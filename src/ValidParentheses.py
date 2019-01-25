open_list= {"[", "{", "("}
list1 = {"]":"[", "}":"{",")":"("}                  

class Solution:
    def isValid(self, s):        
        if not s:
            return True
        
        if s[0] not in open_list:
            return False      
        
        stack = []
        for j,i in enumerate(s):
            if i in open_list:
                stack.append(i)
            else:
                try:
                    last = stack.pop()
                    if last != list1[i]:  
                        return False                   
                except IndexError:
                    return False  
        return not stack
        
