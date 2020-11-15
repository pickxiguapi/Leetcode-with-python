#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# 78/78 cases passed (52 ms)
# Your runtime beats 93.04 % of python3 submissions
# Your memory usage beats 19.33 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        flag = True  # is bipartite
        node_num = len(graph)

        # -1 A组
        # 0 未分组
        # 1 B组
        # 初始化全部为0
        colors = [0 for i in range(node_num)]

        # 建图
        grid = [[0]*node_num for _ in range(node_num)]
        for i in range(node_num):
            for j in graph[i]:
                grid[i][j] = 1
        
        for i in range(node_num):
            if colors[i] == 0 and not self.DFS(grid, colors, i, 1, node_num):
                return False
        
        return True

    def DFS(self, grid, colors, i, color, node_num):
        """
        grid: graph
        colors: node colors
        i: node name
        color: node color
        node_num: node_num
        """
        colors[i] = color
        for j in range(node_num):
            if grid[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.DFS(grid, colors, j, -1*color, node_num):
                    return False
        return True

# @lc code=end

