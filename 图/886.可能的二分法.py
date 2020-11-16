#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
# 70/70 cases passed (1688 ms)
# Your runtime beats 23.36 % of python3 submissions
# Your memory usage beats 7.17 % of python3 submissions (47.6 MB)
#
#
# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # 建图

        graph = [[0] * N for i in range(N)]
        for a, b in dislikes:
            graph[a - 1][b - 1] = 1
            graph[b - 1][a - 1] = 1

        # 涂色
        # 未上色 0
        # A色 1
        # B色 -1
        colors = [0] * N

        # 使用DFS遍历
        for i in range(N):
            if colors[i] == 0 and not self.DFS(graph, colors, i, 1, N):
                return False
        return True
    
    def DFS(self, graph, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            if graph[i][j]:
                if colors[j] == color:
                    return False
                elif colors[j] == 0 and not self.DFS(graph, colors, j, -1*color, N):
                    return False
        return True


# @lc code=end
