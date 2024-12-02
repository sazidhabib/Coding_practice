import heapq

def dijkstra(graph, source):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize distances with infinity
    dist = [float('inf')] * n
    dist[source] = 0  # Distance to the source is 0
    
    # Min-heap priority queue: (distance, vertex)
    pq = [(0, source)]
    
    # While the priority queue is not empty
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Skip processing if the distance in the queue is outdated
        if current_distance > dist[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # If a shorter path is found
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

# Example graph as an adjacency list
# Graph: vertex -> [(neighbor, weight), ...]
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

# Example usage
source = 0
shortest_distances = dijkstra(graph, source)
print(f"Shortest distances from vertex {source}: {shortest_distances}")
