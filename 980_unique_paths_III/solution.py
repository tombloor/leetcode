class Solution:
    def inbounds(self, coords):
        if coords[1] < 0 or coords[1] >= len(self.grid):
            return False
        if coords[0] < 0 or coords[0] >= len(self.grid[0]):
            return False
        return True
    
    def count_routes(self, x, y, visited, total_routes):
        visited = visited + [(x, y)]

        if len(visited) > self.target_moves:
            return 0
        
        right = (x + 1, y)
        down = (x, y -1)
        left = (x - 1, y)
        up = (x, y + 1)
        
        if self.inbounds(right):
            value = self.grid[right[1]][right[0]]
            if value == 0 and right not in visited:
                total_routes = self.count_routes(right[0], right[1], visited, total_routes)
            elif value == 2 and self.target_moves == len(visited):
                total_routes += 1
                
        if self.inbounds(down):
            value = self.grid[down[1]][down[0]]
            if value == 0 and down not in visited:
                total_routes = self.count_routes(down[0], down[1], visited, total_routes)
            elif value == 2 and self.target_moves == len(visited):
                total_routes += 1
                
        if self.inbounds(left):
            value = self.grid[left[1]][left[0]]
            if value == 0 and left not in visited:
                total_routes = self.count_routes(left[0], left[1], visited, total_routes)
            elif value == 2 and self.target_moves == len(visited):
                total_routes += 1
                
        if self.inbounds(up):
            value = self.grid[up[1]][up[0]]
            if value == 0 and up not in visited:
                total_routes = self.count_routes(up[0], up[1], visited, total_routes)
            elif value == 2 and self.target_moves == len(visited):
                total_routes += 1
            
        return total_routes
    
    def uniquePathsIII(self, grid: [[int]]) -> int:
        self.grid = grid
        self.target_moves = 0
        start = None
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    start = (j, i)
                    self.target_moves += 1
                if grid[i][j] == 0:
                    self.target_moves += 1
        
        routes = self.count_routes(start[0], start[1], [], 0)
        
        return routes