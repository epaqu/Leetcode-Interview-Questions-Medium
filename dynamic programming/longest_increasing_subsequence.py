class Solution:
    def binarySearch(self, indices, nums, target):
        start = 0
        end = len(indices) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[indices[mid]] == target:
                return mid
            if mid == start or mid == end:
                break
            if nums[indices[mid]] < target:
                start = mid
            elif nums[indices[mid]] > target:
                end = mid
        return end
    
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        indices = []
        for i in range(len(nums)):
            if len(indices) == 0:
                indices.append(i)
                continue
            if nums[i] > nums[indices[-1]]:
                indices.append(i)
            else:
                if nums[i] < nums[indices[0]]:
                    indices[0] = i
                else:
                    replace = self.binarySearch(indices, nums, nums[i])
                    indices[replace] = i
        return len(indices)
