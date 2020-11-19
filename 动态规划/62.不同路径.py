#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# 62/62 cases passed (36 ms)
# Your runtime beats 88.69 % of python3 submissions
# Your memory usage beats 5.13 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 当机器人从左上角走到坐标为(i, j)的地方时，有dp[i][j]种不同的路径
        # dp[m-1][n-1]是我们要的答案
        dp = [[0]*n for _ in range(m)]

        # 寻找初始值
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 寻找递推公式
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pass
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


# @lc code=end

