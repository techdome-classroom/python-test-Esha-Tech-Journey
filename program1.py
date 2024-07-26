class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:

    #    write your code here
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 'W':
                return
            grid[row][col] = 'W'  # Mark as visited
            # Explore neighboring cells
            dfs(row-1, col)  # Up
            dfs(row+1, col)  # Down
            dfs(row, col-1)  # Left
            dfs(row, col+1)  # Right

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    islands += 1
                    dfs(i, j)
            
    

        return islands