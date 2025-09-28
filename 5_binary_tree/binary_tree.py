import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Генерація градієнту кольорів
def generate_colors(n, start_color=(18, 150, 240), end_color=(200, 230, 255)):
    colors = []
    for i in range(n):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / max(1, n-1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / max(1, n-1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / max(1, n-1))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

# Створення бінарного дерева
def create_binary_tree():
    G = nx.DiGraph()
    edges = [
        (1, 2), (1, 3),
        (2, 4), (2, 5),
        (3, 6), (3, 7)
    ]
    G.add_edges_from(edges)
    return G

# DFS без рекурсії
def dfs(G, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            children = list(G.neighbors(node))
            stack.extend(reversed(children))
    return visited

# BFS без рекурсії
def bfs(G, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(G.neighbors(node))
    return visited

# Анімація обходу
def animate_traversal(G, visited_order, title):
    colors = generate_colors(len(visited_order))
    pos = nx.spring_layout(G, seed=42)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    def update(frame):
        ax.clear()
        node_colors = []
        for node in G.nodes():
            if node in visited_order[:frame+1]:
                idx = visited_order.index(node)
                node_colors.append(colors[idx])
            else:
                node_colors.append("#DDDDDD")
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=12, ax=ax)
        ax.set_title(title)
    
    ani = FuncAnimation(fig, update, frames=len(visited_order), interval=800, repeat=False)
    plt.show()

# Основна програма
if __name__ == "__main__":
    tree = create_binary_tree()
    
    dfs_order = dfs(tree, 1)
    bfs_order = bfs(tree, 1)
    
    animate_traversal(tree, dfs_order, "Анімація обходу в глибину (DFS)")
    animate_traversal(tree, bfs_order, "Анімація обходу в ширину (BFS)")
