class Solution:
    def combination(self, l, n):
        """
        returns all combinations of all elements of all rows in l with n.
        """
        combs = []
        for row in l:
            for i in range(0, len(row)+1):
                comb = []
                for j in range(0, i):
                    comb.append(row[j])
                comb.append(n)
                for j in range(i, len(row)):
                    comb.append(row[j])
                combs.append(comb)
        print(combs)
        return combs
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #since all are distinct, it's just a cobmination of all indices.
        if not nums:
            return []
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            res = self.combination(res, nums[i])
        return res
