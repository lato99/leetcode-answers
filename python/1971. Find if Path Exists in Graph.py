#Time Complexity: O(E+V), where E represents the number of edges, and V represend number of vertices. Building the graph takes O(V) time. Using dfs takes O(V+E) in worst case, where every vertices and edge is discovered.
#Space Complexity: O(E+V). The graph which represents the adjaceny has space of O(E+V) in worst case where each node have edge to every other node, visited set has O(V) space, it stores every vertice in worst case. The recursive stack
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = dict()
        for k,v in edges:
            if k in graph:
                graph[k].append(v)
            else:
                graph[k] = [v]
            if v in graph:
                graph[v].append(k)
            else:
                graph[v] = [k]
        def dfs(node, visited):
            if node == destination:
                return True
            else:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        if  dfs(neighbor,visited):
                            return True
            return False
        visited = set()
        return dfs(source, visited)