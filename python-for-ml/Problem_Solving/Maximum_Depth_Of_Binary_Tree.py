def build_tree(values):
    nodes = [None if v is None else [v, None, None] for v in values]
    for i, node in enumerate(nodes):
        if node:
            if 2*i+1 < len(nodes):
                node[1] = nodes[2*i+1]
            if 2*i+2 < len(nodes):
                node[2] = nodes[2*i+2]
    return nodes[0] if nodes else None

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root[1]), maxDepth(root[2]))

values = input("Enter values: ").split(",")
values = [None if v.strip().lower() == "null" else int(v.strip()) for v in values]
solution = maxDepth(build_tree(values))
print("Maximum depth:", solution)