import csv
import heapq
from collections import defaultdict

# Load graph from CSV
def load_graph(filename):
    graph = defaultdict(dict)

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source'].strip()
            dest = row['destination'].strip()
            dist = int(row['distance'])

            graph[src][dest] = dist
            graph[dest][src] = dist

    return graph


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


# Load graph
graph = load_graph("indian_cities_distances.csv")

# Create case-insensitive mapping
city_map = {city.lower(): city for city in graph}

# Display available cities
print("Available cities:")
for city in graph:
    print("-", city)

# Loop until valid start city
while True:
    start_input = input("\nEnter starting city: ").strip().lower()
    
    if start_input in city_map:
        start_city = city_map[start_input]
        break
    else:
        print("Invalid city! Please try again.")

# Run algorithm
result = dijkstra(graph, start_city)

# Loop until valid choice
while True:
    choice = input("\nDo you want distance to a specific city? (yes/no): ").strip().lower()
    
    if choice in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# If user wants specific destination
if choice == "yes":
    
    while True:
        dest_input = input("Enter destination city: ").strip().lower()
        
        if dest_input in city_map:
            dest_city = city_map[dest_input]
            print(f"\nShortest distance from {start_city} to {dest_city}: {result[dest_city]} km")
            break
        else:
            print("Invalid destination city! Please try again.")

# Otherwise show all distances
else:
    print(f"\nShortest distances from {start_city}:")
    for city, dist in result.items():
        print(city, ":", dist, "km")