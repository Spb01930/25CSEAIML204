def dfs(graph,node,visited):
    
    visited.add(node)
    print(node,end=" ")
       
    for neighbour in graph[node]:
          if neighbour not in visited:
              dfs(graph,neighbour,visited)
              
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':[],
    'G':[]
}
visited=set()
print("DFS Traversal:")
dfs(graph,'A',visited)