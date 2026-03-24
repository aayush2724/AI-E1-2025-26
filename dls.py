class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def DLS(root, depth_limit):
    visited = []

    def dfs(node, depth):
        if node is None:
            return
        
        visited.append(node.value)

        if depth == depth_limit:
            return
        
        for child in node.children:
            dfs(child, depth + 1)

    dfs(root, 0)
    print("DLS Visit Order:", visited)


nodes = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    val = int(input("Enter node value: "))
    nodes[val] = Node(val)

for val in nodes:
    children_vals = input(f"Enter children of {val} (space separated, press enter if none): ").split()
    for child_val in children_vals:
        nodes[val].children.append(nodes[int(child_val)])

root_val = int(input("Enter root node: "))
depth_limit = int(input("Enter depth limit: "))

DLS(nodes[root_val], depth_limit)
