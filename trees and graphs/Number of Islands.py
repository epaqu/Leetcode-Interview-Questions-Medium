class Solution:
    def isLand(self, row, col, grid):
        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.isLand(row-1, col, grid) if row > 0 else None
            self.isLand(row+1, col, grid) if row < len(grid)-1 else None
            self.isLand(row, col-1, grid) if col > 0 else None
            self.isLand(row, col+1, grid) if col < len(grid[0])-1 else None
            return True
        return False
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #look for a 1
            #once found a 1,
                #count += 1
                #check its four neighbors if they are also 1.
                    #if a neighbor==1, change it to 0
                    #and repeat this on the said neighbor.
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isLand(i, j, grid):
                    count += 1                    
        return count
