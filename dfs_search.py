def dfs_search(graph,node,target,visited):
    visited.add(node)
    if node == target:
        return True
    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs_search(graph,neighbour,target,visited):
                return True
    return False
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
target = 'F'
if dfs_search(graph,'A',target,visited):
    print(" Target found.")
else:
    print(" Target not found.")    
    
   """
   OUTPUT:
   Target found.
   """
