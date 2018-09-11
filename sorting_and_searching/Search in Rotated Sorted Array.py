class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        if nums[0] == target:
            return 0
        sign = 1
        if nums[0] > target:
            sign = -1
        for i in range(len(nums)):
            if nums[sign*i] == target:
                return i if sign==1 else len(nums)-i
