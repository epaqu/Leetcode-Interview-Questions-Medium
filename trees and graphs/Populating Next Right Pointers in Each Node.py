# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left:
            return None
        self.connect(root.left)
        self.connect(root.right)
        left  = root.left
        right = root.right
        while left:
            left.next = right
            left  = left.right
            right = right.left
