import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        """Додає ребро з вершини u у вершину v з вагою weight"""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # якщо граф неорієнтований

    def dijkstra(self, start):
        """Алгоритм Дейкстри з використанням бінарної купи"""
        distances = {vertex: float("inf") for vertex in self.adj_list}
        distances[start] = 0

        # heapq реалізує мін-купу
        priority_queue = [(0, start)]  # (відстань, вершина)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайшли кращий шлях раніше — пропускаємо
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                # Якщо знайшли коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "F", 11)

    start_vertex = "A"
    shortest_paths = g.dijkstra(start_vertex)

    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"До {vertex}: {distance}")
