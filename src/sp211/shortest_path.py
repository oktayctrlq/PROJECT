import heapq

def dijkstra(graph, start):
    """
    Returns the shortest paths from start node to all other nodes in the graph using Dijkstra's algorithm.

    Args:
        graph (dict): The adjacency list of the graph. Example:
                      {'A': {'B': 4, 'C': 2}, 'B': {'C': 1, 'D': 5}, ...}
        start (str): The starting node.

    Returns:
        distances (dict): The shortest distance from start to each node.
        previous (dict): The previous node in the shortest path.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    return distances, previous

