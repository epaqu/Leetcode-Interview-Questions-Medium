class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #iterative method
        if len(nums) <= 1:
            return True
        j = len(nums) - 1
        i = j - 1
        while i > 0:
            if nums[i] >= j - i:
                j = i
                i -= 1
            else:
                i -= 1
        return nums[0] >= j
