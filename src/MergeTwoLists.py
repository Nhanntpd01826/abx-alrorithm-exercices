# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l2.val <= l1.val:
            l3 = l2
            l3.next = self.mergeTwoLists(l1,l2.next)
        else:
            l3 = l1 
            l3.next = self.mergeTwoLists(l1.next, l2)       
        return l3
