import heapq
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, src, dest, weight):
        self.adj[src].append((dest, weight))
        self.adj[dest].append((src, weight))  # Bidirectional for delivery routes

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.adj}
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            if curr_dist > dist[curr_node]:
                continue

            for neighbor, weight in self.adj[curr_node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist

    def bfs_delivery(self, start):
        visited = set()
        queue = deque([start])
        route = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                route.append(node)
                for neighbor, _ in self.adj[node]:
                    queue.append(neighbor)

        return route
