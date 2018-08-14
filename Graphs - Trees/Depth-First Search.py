# This algorithm is designed for graphs and trees

# Implementation
def dfs(graph, vertex, path=[]):
   path += [vertex]
   for neighbor in graph[vertex]:
      if neighbor no in path:
         path = dfs(graph, neighbor, path)
return path
