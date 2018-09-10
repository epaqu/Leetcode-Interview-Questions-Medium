class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #recursive solution
        k = 2
        while len(nums) > 1:
            if nums[-k] > k - 2:
                if len(nums) == 1:
                    return True
                else:
                    return self.canJump(nums[:-k+1])
            else:
                if k < len(nums):
                    k += 1
                else:
                    return False
        return True
