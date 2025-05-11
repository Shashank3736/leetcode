#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Handle edge cases
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        
        # Build adjacency list and degree array
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        # Initialize queue with leaves (nodes with degree 1)
        from collections import deque
        queue = deque([i for i in range(n) if degree[i] == 1])
        remaining_nodes = n
        
        # Trim leaves until 1 or 2 nodes remain
        while remaining_nodes > 2:
            # Process all current leaves
            leaves_count = len(queue)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = queue.popleft()
                # Update neighbor's degree
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        # Return remaining nodes (the roots of MHTs)
        return list(queue)
# @lc code=end

