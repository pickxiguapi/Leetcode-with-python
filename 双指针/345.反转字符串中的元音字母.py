#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# 481/481 cases passed (48 ms)
# Your runtime beats 98.86 % of python3 submissions
# Your memory usage beats 22.89 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        point1 = 0
        point2 = len(s) - 1
        vowels = set('aeiouAEIOU')  # 这里用集合in会快很多
        sl = list(s)

        while point1 < point2:
            if sl[point1] in vowels:
                if sl[point2] in vowels:
                    sl[point1], sl[point2] = sl[point2], sl[point1]

                    point1 += 1
                    point2 -= 1
                else:
                    point2 -= 1
            
            elif s[point2] in vowels:
                if s[point1] in vowels:
                    sl[point1], sl[point2] = sl[point2], sl[point1]

                    point1 += 1
                    point2 -= 1
                else:
                    point1 += 1
            else:
                point1 += 1
                point2 -= 1
        return ''.join(sl)
            
            
# @lc code=end

