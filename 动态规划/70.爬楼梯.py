#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# 45/45 cases passed (40 ms)
# Your runtime beats 61.48 % of python3 submissions
# Your memory usage beats 18.69 % of python3 submissions (13.5 MB)
"""
    1️⃣ 定义数组元素的含义，数组是来保存历史的，注意定义数组的含义！
    2️⃣ 找出数组元素之间的关系式，即通过历史数据来推新的元素值
    3️⃣ 找出初始值

"""
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1️⃣ 定义数组元素的含义
        # 我们要求有多少种方法可以爬到楼顶，所以我们定义dp[n]为有多少种方法爬到楼顶
        # 很明显跳i阶楼梯有dp[i]种方法，j阶楼梯有dp[j]种方法，所以i+j阶有dp[i+j]种方法
        dp = [0] * (n+1)
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # 3️⃣ 定义初始值
        else:
            dp[1] = 1
            dp[2] = 2 

            # 2️⃣ 找出数组元素之间的关系式
            # dp[n] = dp[n-1] + dp[n-2]
            for i in range(3, n+1):
                dp[i] = dp[i-2] + dp[i-1]

            return dp[n]

# @lc code=end

