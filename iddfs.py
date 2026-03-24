def dls(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return True

    if depth > 0:
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True

        visited.remove(node)

    return False


def iddfs(graph, start, goal):
    depth = 0

    while True:
        visited = set()
        print(f"Searching at depth {depth}")

        if dls(graph, start, goal, depth, visited):
            print(f"Found at depth {depth}")
            return True

        depth += 1


graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

iddfs(graph, start, goal)
