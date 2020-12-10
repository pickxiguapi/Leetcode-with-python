#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# 176/176 cases passed (6180 ms)
# Your runtime beats 21.93 % of python3 submissions
# Your memory usage beats 18.88 % of python3 submissions (21.2 MB)
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # 定义dp[i][j]即s[i...j]是否为回文子串,则最长回文子串为j-i+1
        dp = [[0] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = 1

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        
        return s[start: start+max_len]



# @lc code=end

