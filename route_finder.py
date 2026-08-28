from collections import deque


# ============================================================
#                 ROUTE FINDER - DSA PROJECT
#                 GRAPH + BFS + DFS
# ============================================================


class Graph:

    def __init__(self):
        self.graph = {}

    # --------------------------------------------------------
    # Add a city
    # --------------------------------------------------------
    def add_city(self, city):

        if city not in self.graph:
            self.graph[city] = []
            return True

        return False

    # --------------------------------------------------------
    # Add connection between two cities
    # --------------------------------------------------------
    def add_connection(self, city1, city2):

        if city1 not in self.graph:
            self.add_city(city1)

        if city2 not in self.graph:
            self.add_city(city2)

        if city2 not in self.graph[city1]:
            self.graph[city1].append(city2)

        if city1 not in self.graph[city2]:
            self.graph[city2].append(city1)

    # --------------------------------------------------------
    # Display all cities
    # --------------------------------------------------------
    def display_cities(self):

        print("\n" + "=" * 65)
        print("                         CITIES")
        print("=" * 65)

        for number, city in enumerate(self.graph.keys(), 1):
            print(f"{number}. {city}")

        print("=" * 65)

    # --------------------------------------------------------
    # Display complete graph
    # --------------------------------------------------------
    def display_graph(self):

        print("\n" + "=" * 65)
        print("                      CITY MAP")
        print("=" * 65)

        for city, neighbours in self.graph.items():

            if neighbours:
                print(f"{city:<15} -> {', '.join(neighbours)}")
            else:
                print(f"{city:<15} -> No connections")

        print("=" * 65)

    # --------------------------------------------------------
    # BFS - Breadth First Search
    # Uses Queue
    # --------------------------------------------------------
    def bfs(self, start, destination):

        queue = deque()

        queue.append([start])

        visited = set()

        visited.add(start)

        traversal = []

        while queue:

            path = queue.popleft()

            current = path[-1]

            traversal.append(current)

            if current == destination:
                return path, traversal

            for neighbour in self.graph[current]:

                if neighbour not in visited:

                    visited.add(neighbour)

                    new_path = path + [neighbour]

                    queue.append(new_path)

        return None, traversal

    # --------------------------------------------------------
    # DFS - Depth First Search
    # Uses Stack
    # --------------------------------------------------------
    def dfs(self, start, destination):

        stack = []

        stack.append([start])

        visited = set()

        traversal = []

        while stack:

            path = stack.pop()

            current = path[-1]

            if current in visited:
                continue

            visited.add(current)

            traversal.append(current)

            if current == destination:
                return path, traversal

            for neighbour in reversed(self.graph[current]):

                if neighbour not in visited:

                    new_path = path + [neighbour]

                    stack.append(new_path)

        return None, traversal


# ============================================================
#                 CREATE INITIAL GRAPH
# ============================================================

city_graph = Graph()


# Add cities

initial_cities = [
    "Bangalore",
    "Ramanagara",
    "Channapatna",
    "Mandya",
    "Mysore",
    "Tumkur",
    "Hassan"
]


for city in initial_cities:
    city_graph.add_city(city)


# Add connections

city_graph.add_connection("Bangalore", "Ramanagara")
city_graph.add_connection("Bangalore", "Tumkur")

city_graph.add_connection("Ramanagara", "Channapatna")

city_graph.add_connection("Channapatna", "Mandya")

city_graph.add_connection("Mandya", "Mysore")

city_graph.add_connection("Tumkur", "Hassan")

city_graph.add_connection("Hassan", "Mysore")


# ============================================================
#                 GET VALID CITY
# ============================================================

def get_city(prompt):

    while True:

        city = input(prompt).strip()

        if city in city_graph.graph:
            return city

        print("\n❌ City not found.")
        print("Please enter a valid city name.")


# ============================================================
#                 DISPLAY ROUTE
# ============================================================

def display_route(route):

    if route is None:

        print("\n❌ No route found.")

        return

    print("\n📍 ROUTE FOUND")
    print("-" * 65)

    print(" → ".join(route))

    print("-" * 65)

    print(f"Cities in route     : {len(route)}")
    print(f"Connections         : {len(route) - 1}")


# ============================================================
#                 BFS ROUTE
# ============================================================

def find_bfs_route():

    print("\n" + "=" * 65)
    print("                     BFS ROUTE FINDER")
    print("=" * 65)

    city_graph.display_cities()

    start = get_city("\nEnter starting city: ")

    destination = get_city("Enter destination city: ")

    route, traversal = city_graph.bfs(start, destination)

    print("\n🔵 BFS TRAVERSAL")
    print("-" * 65)

    print(" → ".join(traversal))

    display_route(route)

    print("\nDSA Used:")
    print("Queue + Graph + Breadth First Search")

    print("Time Complexity: O(V + E)")


# ============================================================
#                 DFS ROUTE
# ============================================================

def find_dfs_route():

    print("\n" + "=" * 65)
    print("                     DFS ROUTE FINDER")
    print("=" * 65)

    city_graph.display_cities()

    start = get_city("\nEnter starting city: ")

    destination = get_city("Enter destination city: ")

    route, traversal = city_graph.dfs(start, destination)

    print("\n🟢 DFS TRAVERSAL")
    print("-" * 65)

    print(" → ".join(traversal))

    display_route(route)

    print("\nDSA Used:")
    print("Stack + Graph + Depth First Search")

    print("Time Complexity: O(V + E)")


# ============================================================
#                 COMPARE BFS AND DFS
# ============================================================

def compare_algorithms():

    print("\n" + "=" * 65)
    print("                    BFS vs DFS")
    print("=" * 65)

    city_graph.display_cities()

    start = get_city("\nEnter starting city: ")

    destination = get_city("Enter destination city: ")

    bfs_route, bfs_traversal = city_graph.bfs(
        start,
        destination
    )

    dfs_route, dfs_traversal = city_graph.dfs(
        start,
        destination
    )

    print("\n" + "=" * 65)
    print("                         BFS")
    print("=" * 65)

    print("\nTraversal:")
    print(" → ".join(bfs_traversal))

    print("\nRoute:")

    if bfs_route:
        print(" → ".join(bfs_route))
    else:
        print("No route found.")

    print(f"\nCities visited: {len(bfs_traversal)}")

    print("\n" + "=" * 65)
    print("                         DFS")
    print("=" * 65)

    print("\nTraversal:")
    print(" → ".join(dfs_traversal))

    print("\nRoute:")

    if dfs_route:
        print(" → ".join(dfs_route))
    else:
        print("No route found.")

    print(f"\nCities visited: {len(dfs_traversal)}")

    print("\n" + "=" * 65)
    print("                     COMPARISON")
    print("=" * 65)

    print("""
BFS:
• Uses Queue
• Explores level by level
• Finds shortest path in an unweighted graph

DFS:
• Uses Stack
• Explores deeply before backtracking
• Does not guarantee the shortest path
""")

    if bfs_route and dfs_route:

        print(f"BFS route length: {len(bfs_route) - 1} connections")
        print(f"DFS route length: {len(dfs_route) - 1} connections")


# ============================================================
#                 ADD NEW CITY
# ============================================================

def add_new_city():

    print("\n" + "=" * 65)
    print("                      ADD NEW CITY")
    print("=" * 65)

    city = input("Enter new city name: ").strip()

    if not city:

        print("\n❌ City name cannot be empty.")

        return

    if city in city_graph.graph:

        print("\n⚠️ City already exists.")

        return

    city_graph.add_city(city)

    print(f"\n✅ {city} added successfully.")


# ============================================================
#                 ADD CONNECTION
# ============================================================

def add_new_connection():

    print("\n" + "=" * 65)
    print("                   ADD CONNECTION")
    print("=" * 65)

    city_graph.display_cities()

    city1 = get_city("\nEnter first city: ")

    city2 = get_city("Enter second city: ")

    if city1 == city2:

        print("\n❌ A city cannot connect to itself.")

        return

    city_graph.add_connection(city1, city2)

    print(
        f"\n✅ Connection added: {city1} ↔ {city2}"
    )


# ============================================================
#                 MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")

        print("=" * 65)
        print("                  🗺️ ROUTE FINDER")
        print("                 GRAPH + BFS + DFS")
        print("=" * 65)

        print("1. Display City Map")
        print("2. Find Route using BFS")
        print("3. Find Route using DFS")
        print("4. Compare BFS and DFS")
        print("5. Add New City")
        print("6. Add City Connection")
        print("7. Exit")

        print("=" * 65)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            city_graph.display_graph()

        elif choice == "2":

            find_bfs_route()

        elif choice == "3":

            find_dfs_route()

        elif choice == "4":

            compare_algorithms()

        elif choice == "5":

            add_new_city()

        elif choice == "6":

            add_new_connection()

        elif choice == "7":

            print("\n" + "=" * 65)
            print("             Thank you for using Route Finder!")
            print("=" * 65)

            print("\nProject completed using:")
            print("• Graph")
            print("• BFS")
            print("• DFS")
            print("• Queue")
            print("• Stack")

            print("\nKeep learning DSA! 🚀")

            break

        else:

            print("\n❌ Invalid choice.")
            print("Please enter a number between 1 and 7.")


# ============================================================
#                 START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()