class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #for any given coordinate (x,y), there are
        #self.uniquePaths(x-1, y) + self.uniquePaths(x, y-1)
        #unique paths.
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
