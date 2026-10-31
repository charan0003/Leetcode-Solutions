class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                idx = i * n + j

                if grid[i][j] == 0:
                    right[i][j] = idx
                    down[i][j] = idx
                else:
                    if i + 1 < m:
                        right[i][j] = down[i + 1][j]

                    if j + 1 < n:
                        down[i][j] = right[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                if j + 1 < n:
                    dest = right[i][j + 1]

                    if dest != -1:
                        x, y = divmod(dest, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

                if i + 1 < m:
                    dest = down[i + 1][j]

                    if dest != -1:
                        x, y = divmod(dest, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]