
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

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

root.children = [n2, n3]
n2.children = [n4, n5]
n3.children = [n6, n7]

DLS(root, 2)