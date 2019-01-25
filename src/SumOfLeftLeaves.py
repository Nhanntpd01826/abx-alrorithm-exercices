class Solution:
    def sumOfLeftLeaves(self, root):
        res=0
        if root==None: 
            return res  
        res=self.sumOfLeftLeaves(root.left)  + self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.right and not root.left.left:
            res+=root.left.val      
        return res

