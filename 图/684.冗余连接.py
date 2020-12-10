#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 使用拓扑排序后无环图将为空的性质
        # edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

        # 图转换为邻接矩阵形式
        import collections
        neibors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)

        for s, t in edges:
            neibors[s].append(t)
            neibors[t].append(s)

            degrees[s] += 1
            degrees[t] += 1
        
        # 找出所有度为1的节点
        degree_one = [k for k, v in degrees.items() if v==1]
        
        while degree_one:
            degree_one_after_delete = []
            # 当度为1的节点不为空
            for n in degree_one:
                # 删除度为1的节点,并将他的所有邻居的度减1
                for neibor in neibors[n]:
                    degrees[neibor] -= 1
                    if degrees[neibor] == 1:
                        degree_one_after_delete.append(neibor)
            
                del neibors[n]
            del degree_one[:]
            degree_one = degree_one_after_delete

        for s, t in edges[::-1]:  # edges[::-1]其实是edges的反向列表,因为
            if min(degrees[s], degrees[t]) > 1:
                return [s, t]  # 度不为1的就是要删除的结果

                
        
# @lc code=end

