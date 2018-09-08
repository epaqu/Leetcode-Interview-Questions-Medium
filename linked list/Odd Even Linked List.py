# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
    #예외
        if not head or not head.next or not head.next.next:
            return head
        #기본세팅
        root = head
        odd = root          #odd 1 2 3 4 5
        root = root.next    #root 2 3 4 5
        even = root         #even 2 3 4 5
        root = root.next    #root 3 4 5
        odd.next = None       #odd 1
        even.next = None      #even 2
        evenRoot = even
        while root:
            odd.next = root     #odd 1 3 4 5
            root = root.next    #root 4 5
            if not root:
                odd = odd.next
                break
            even.next = root    #even 2 4 5
            root = root.next    #root 5
            odd = odd.next      #odd (1) 3 4 5
            odd.next = None       #odd (1) 3
            even = even.next    #even (2) 4 5
            even.next = None      #even (2) 4
        odd.next = evenRoot
        
        return head
