class Solution:
    def combination(self, l1, l2):
        """
        returns a list of all combinations of elements in l1 with elements in l2
        """
        res = []
        for e1 in l1:
            for e2 in l2:
                res.append(e1+e2)
        return res
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        keyboard = [['a','b','c'],
                    ['d','e','f'],
                    ['g','h','i'],
                    ['j','k','l'],
                    ['m','n','o'],
                    ['p','q','r','s'],
                    ['t','u','v'],
                    ['w','x','y','z']]
        perm = keyboard[int(digits[0])-2]
        for i in range(1, len(digits)):
            perm = self.combination(perm, keyboard[int(digits[i])-2])
        return perm
        
        """
        pseudocode:
        perm = keyboard[0]
        for i in range(1, len(digits)):
            perm = self.perm(perm, keyboard[digits[i]-2])
        return perm
        """
