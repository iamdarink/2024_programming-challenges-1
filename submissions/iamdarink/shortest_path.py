import heapq

def dijkstra(edges, start, end):
    graph = {}
    for u, v, weight in edges:
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, []).append((u, weight))
    
    queue = [(0, start)]
    distances = {start: 0}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node == end:
            return current_distance
        
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return float('inf')

edges_input = input("input: ")
start = int(input("จุดเริ่มต้น: "))
end = int(input("จุดสิ้นสุด: "))

edges = eval(edges_input)

shortest_path_length = dijkstra(edges, start, end)

print(f"output: {shortest_path_length}")
