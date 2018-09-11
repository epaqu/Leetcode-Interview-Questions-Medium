class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        firstVals = [row[0] for row in matrix]
        toSearch = []
        for i in range(len(firstVals)):
            if firstVals[i] <= target:
                toSearch.append(i)
        if not toSearch:
            return False
        for i in toSearch:
            for val in matrix[i]:
                if val == target:
                    return True
        return False
