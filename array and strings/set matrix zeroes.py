class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            coordinates = []
            for row in range(0, len(matrix)):
                for col in range(0, len(matrix[0])):
                    if matrix[row][col] == 0:
                        coordinates.append([row, col])
            for coordinate in coordinates:
                row = coordinate[0]
                col = coordinate[1]
                matrix[row] = [0] * len(matrix[0])
                for i in range(len(matrix)):
                    matrix[i][col] = 0
