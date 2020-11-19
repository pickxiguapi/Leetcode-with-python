#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
# 46/46 cases passed (672 ms)
# Your runtime beats 7.11 % of python3 submissions
# Your memory usage beats 32.78 % of python3 submissions (15.7 MB)

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 即判断有向图是否有环

        # 1️⃣ 将边缘列表转换为邻接矩阵
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        # 2️⃣ 判断是否访问过
        visited = [0 for _ in range(numCourses)]
        
        # 3️⃣ 判断有向图是否有环
        for i in range(numCourses):
            if not self.dfs(adjacency, i, visited):
                return False
        return True
    
    def dfs(self, adjacency, i, visited):
        if visited[i] == 1:
            return False
        visited[i] = 1
        for j in adjacency[i]:
            if not self.dfs(adjacency, j, visited):
                return False
        visited[i] = 0
        return True

# @lc code=end

