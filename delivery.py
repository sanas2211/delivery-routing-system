from graph import Graph

# Create graph instance
g = Graph()

# Add sample city routes (can load from file later)
g.add_edge("Warehouse", "CityA", 4)
g.add_edge("Warehouse", "CityB", 2)
g.add_edge("CityA", "CityC", 3)
g.add_edge("CityB", "CityC", 1)
g.add_edge("CityC", "CityD", 6)

# Dijkstra shortest paths from Warehouse
shortest_paths = g.dijkstra("Warehouse")
print("Shortest distances from Warehouse:")
for city, dist in shortest_paths.items():
    print(f"{city}: {dist} units")

# BFS delivery route simulation
print("\nDelivery Route (BFS Traversal):")
route = g.bfs_delivery("Warehouse")
print(" -> ".join(route))
