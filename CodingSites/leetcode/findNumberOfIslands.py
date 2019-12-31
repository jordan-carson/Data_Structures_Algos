# iterate over the 2d array, and every time we find an island (which is a group of 1's horizontally
# or vertically, create a counter and increment it if we find an island
# if we find a 1 next to another one on the same row, or within an adjacent column we should put them
# as water so we do not mess up our counter
#
from collections import deque
#
# def append_if(queue, grid, x, y):
#     if 0 <= x < len(grid) and 0 <=y < len(grid[0]):
#         if grid[x][y] == '1':
#             queue.append((x, y))
#
#
# def markNeighbors(grid, row, col):
#     queue = deque()
#
#     queue.append((row, col))
#     while queue:
#         x, y = queue.pop()
#         grid[x][y] == '0'
#         append_if(queue, grid, x - 1, y)
#         append_if(queue, grid, x + 1, y)
#         append_if(queue, grid, x, y -1)
#         append_if(queue, grid, x, y + 1)
#
#
#
# def numIslands(grid):
#     if not grid or len(grid) == 0 or len(grid[0]) == 0:
#         return 0
#
#     islandcount = 0
#     row_length = len(grid)
#     col_length = len(grid[0])
#     for row in range(row_length):
#         for col in range(col_length):
#             if grid[row][col] == '1':
#                 # increase our counter
#                 islandcount += 1
#                 # change any other land connected to zeros
#                 markNeighbors(grid, row, col)
#
# def changeLandToWater(grid, i, j):
#     # everytime we encounter a 1 we run this function, in every direction if we see 1 change to 0
#     # first base condition is where our row is less than 0
#     # our row greater than greater than the current length in the grid (row len)
#     # our column is less than 0
#     # our column is less than the grid column length (col len)
#     # if we see a zero at the position, do nothing
#     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
#         return
#     # we know the position must be a 1
#     grid[i][j] = 0
#     # do this to every neighbor
#     changeLandToWater(grid, i-1, j) # down
#     changeLandToWater(grid, i+1, j) # up
#     changeLandToWater(grid, i, j-1) # left
#     changeLandToWater(grid, i, j+1) # right

# ----------------



class Solution:
# iterate over the 2d array, and every time we find an island (which is a group of 1's horizontally
# or vertically, create a counter and increment it if we find an island
# if we find a 1 next to another one on the same row, or within an adjacent column we should put them
# as water so we do not mess up our counter
    def append_if(self, queue, x, y):
        """Append to the queue only if in bounds of the grid and the cell value is 1."""
        if x < len(self.grid) and y < len(self.grid[0]):
            if self.grid[x][y] == '1':
                queue.append((x, y))

    def mark_neighbors(self, row, col):
        """Mark all the cells in the current island with value = 2. Breadth-first search."""
        queue = deque()

        queue.append((row, col))
        while queue:
            x, y = queue.pop()
            self.grid[x][y] = '2'

            self.append_if(queue, x - 1, y) #down
            self.append_if(queue, x, y - 1) #left
            self.append_if(queue, x + 1, y) #up
            self.append_if(queue, x, y + 1) #right

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        self.grid = grid

        row_length = len(grid)
        col_length = len(grid[0])

        island_counter = 0
        for row in range(row_length):
            for col in range(col_length):
                if self.grid[row][col] == '1':
                    # found an island
                    island_counter += 1

                    self.mark_neighbors(row, col)

        return island_counter


test_case = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','1']
]
print(Solution().numIslands(test_case))



























