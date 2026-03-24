
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs(tree, node, visited):
    visited.append(node)

    for neighbor in tree[node]:
        dfs(tree, neighbor, visited)

    return visited

result = dfs(tree, 1, [])
print("DFS Traversal:", *result)
