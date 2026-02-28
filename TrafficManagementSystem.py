class TrafficManagementSystem:
    def __init__(self, max_nodes=10):
        self.MAX = max_nodes
        self.graph = [[0] * self.MAX for _ in range(self.MAX)]
        self.trafficLight = [0] * self.MAX
        self.n = 0

    def init_graph(self, n):
        self.n = n
        for i in range(n):
            for j in range(n):
                self.graph[i][j] = 0
            self.trafficLight[i] = 0  # All lights red initially

    def add_road(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def toggle_traffic_light(self, intersection):
        self.trafficLight[intersection] = 1 - self.trafficLight[intersection]

    def display_traffic_lights(self):
        for i in range(self.n):
            state = "Green" if self.trafficLight[i] == 1 else "Red"
            print(f"Intersection {i}: {state}")

    def display_graph(self):
        print("Adjacency Matrix Representation of the Traffic Network:")
        for i in range(self.n):
            for j in range(self.n):
                print(self.graph[i][j], end=" ")
            print()

    def menu(self):
        while True:
            print("\n--- Traffic Management System ---")
            print("1. Toggle Traffic Light")
            print("2. Display Traffic Lights")
            print("3. Display Road Network")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                intersection = int(input("Enter intersection number: "))
                if 0 <= intersection < self.n:
                    self.toggle_traffic_light(intersection)
                    print("Traffic light toggled successfully.")
                else:
                    print("Invalid intersection.")

            elif choice == 2:
                self.display_traffic_lights()

            elif choice == 3:
                self.display_graph()

            elif choice == 4:
                print("Exiting Traffic Management System.")
                break

            else:
                print("Invalid choice. Try again.")


# -------- Main Program --------
tms = TrafficManagementSystem()

n = int(input("Enter the number of intersections: "))
tms.init_graph(n)

m = int(input("Enter the number of roads: "))
for i in range(m):
    u, v = map(int, input(f"Enter road {i+1} (u v): ").split())
    tms.add_road(u, v)

tms.menu()
