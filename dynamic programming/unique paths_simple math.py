class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #for any given m and n,
        #we are moving m-1 right and n-1 down
        #there are (m-1+n-1)! permutations of RIGHT and DOWN
        #and (m-1)! repetitions of RIGHT permutations
        #and (n-1)! repetitions of DOWN permutations
        #so there are (m+n-2)! / (m-1)! / (n-1)! unique paths
        return int(math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1))
