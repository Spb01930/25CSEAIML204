import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 3), ('C', 1), ('E', 2)],
    'E': [('D', 2)]
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 0
}

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(
        open_list,
        (heuristic[start], start)
    )
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        f_current, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]
            
        for neighbour, cost in graph[current]:
            new_g = g_cost[current] + cost
            
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                f_neighbour = new_g + heuristic[neighbour]
                
                heapq.heappush(
                    open_list,
                    (f_neighbour, neighbour)
                )
                parent[neighbour] = current
                
    return None, float("inf")

path, cost = a_star(
    graph,
    heuristic,
    'A',
    'E'
)

print("Shortest Path :", path)
print("Total Cost :", cost)

"""
OUTPUT:
Shortest Path : ['A', 'B', 'D', 'E']
Total Cost : 7
"""
