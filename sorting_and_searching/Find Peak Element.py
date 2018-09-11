class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #when it starts decreasing, it is at its peak
        goingUp = False
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                goingUp = True
            if nums[i] > nums[i+1] and goingUp:
                return i
                goingUp = False
        if not goingUp:
            return 0
        return len(nums)-1
