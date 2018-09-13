class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res
