#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque

        def bfs(node):
            if not node:
                return
            else:
                lookup = {}  # 存储已经看过的节点
                clone = Node(node.val, [])

                q = deque()
                q.appendleft(node)
                lookup[node] = clone
                while q:
                    tmp_node = q.pop()
                
                    # 放入所有邻居节点
                    for n in tmp_node.neighbors:
                        if n not in lookup:
                            lookup[n] = Node(n.val, [])
                            q.appendleft(n)
                        lookup[tmp_node].neighbors.append(lookup[n])
                
                return clone
        
        return bfs(node)

        
        

       
# @lc code=end

