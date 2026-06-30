"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        q = deque()
        hashmap = {}
        

        def dfs(node):
            new = Node()
            new.val = node.val

            hashmap[node] = new

            
            for neighbor in node.neighbors:
                if neighbor not in hashmap:
                    new_n = dfs(neighbor)
                    new.neighbors.append(new_n)
                else:
                    new.neighbors.append(hashmap[neighbor])
            return new
        
        if node:
             return dfs(node)
        else:
            return node
            







