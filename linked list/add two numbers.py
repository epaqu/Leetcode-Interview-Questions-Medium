# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getSum(x):
            return x.val + 10 * getSum(x.next) if x else 0
        sum = getSum(l1) + getSum(l2)
        start = end = ListNode(sum % 10)
        while sum >= 10:
            sum /= 10
            end.next = end = ListNode(sum%10)
        return start
