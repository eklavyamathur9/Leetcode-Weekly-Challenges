#Solution1 : Sort Matrix by Diagonals
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        n=len(grid)
        d=defaultdict(list)
        for i in range(n):
            for j in range(n):
                d[i-j].append(grid[i][j])
        for k in d:
            if k>=0:
                d[k].sort(reverse=True)
            else:
                d[k].sort()
        for i in range(n):
            for j in range(n):
                grid[i][j]=d[i-j].pop(0)
        return grid
        