import collections


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        start = self.board2str(board)

        bfs = collections.deque()
        bfs.append((start, 0))
        visited = set()
        visited.add(start)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while bfs:
            path, step = bfs.popleft()

            if path == goal:
                return step
            p = path.index("0")
            x, y = p // 3, p % 3
            path = list(path)
            for dir in dirs:
                tx, ty = x + dir[0], y + dir[1]
                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3:
                    continue
                path[tx * 3 + ty], path[x * 3 +
                                        y] = path[x * 3 + y], path[tx * 3 + ty]
                pathStr = "".join(path)
                if pathStr not in visited:
                    bfs.append((pathStr, step + 1))
                    visited.add(pathStr)
                path[tx * 3 + ty], path[x * 3 +
                                        y] = path[x * 3 + y], path[tx * 3 + ty]
        return -1

    def board2str(self, board):
        bstr = ""
        for i in range(2):
            for j in range(3):
                bstr += str(board[i][j])
        return bstr


sol = Solution()
board = [[1, 2, 3], [4, 0, 5]]

sol.slidingPuzzle(board)
