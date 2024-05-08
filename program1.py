class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here

     if not grid or not grid[0]:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        grid[i][j] = 'W'  # Mark the land as visited by turning it into water
        # Explore the four possible directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'L':
                island_count += 1
                dfs(i, j)
    
    return island_count

