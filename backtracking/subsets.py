class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        lastPerms = []
        if not nums:
            return res
        nums.sort()
        for num in nums:
            lastPerms.append([num])
        res.extend(lastPerms)
        for _ in nums[1:]:
            thisPerms = []
            for element in lastPerms:
                for num in nums:
                    temp = element[:]
                    print(temp)
                    if temp[len(temp)-1] < num:
                        temp.append(num)
                        thisPerms.append(temp)
            res.extend(thisPerms)
            print(res)
            lastPerms = thisPerms
        return res
