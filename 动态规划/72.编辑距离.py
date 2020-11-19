#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# 1146/1146 cases passed (188 ms)
# Your runtime beats 72.52 % of python3 submissions
# Your memory usage beats 10.15 % of python3 submissions (17.2 MB)
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1) + 1
        len2 = len(word2) + 1

        # 定义二维数组dp[i][j]，word1[:i]到word2[:j]的最小转换次数
        # 之后两个word各增加一个字符进入判断，根据增加的字符是否相等进行相应的操作
        # 初始化
        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        for i in range(len1):
            dp[i][0] = i
        for j in range(len2):
            dp[0][j] = j

        # 1️ 如果word1[i] = word2[j]，则有dp[i+1][j+1] = dp[i][j]
        # 2 如果word1[i] ≠ word2[j]
        # 则可以考虑的方法有插入 删除 替换
        # 插入：对word1插入一个字符 dp[i+1][j+1] = dp[i+1][j] + 1
        # 删除：对word1删除一个字符 dp[i+1][j+1] = dp[i][j+1] + 1
        # 替换：对word1替换一个字符 dp[i+1][j+1] = dp[i][j] + 1
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[len1-1][len2-1]

# @lc code=end

