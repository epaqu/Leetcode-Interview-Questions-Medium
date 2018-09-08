import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = collections.Counter(nums)
        return nums_counter.most_common(1)[0][0]
