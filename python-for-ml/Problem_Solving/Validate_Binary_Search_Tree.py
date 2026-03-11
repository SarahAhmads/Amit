def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not (low < node[0] < high):
        return False
    return is_valid_bst(node[1], low, node[0]) and is_valid_bst(node[2], node[0], high)

def build_tree(values):
    if not values:
        return None
    nodes = [None if v is None else [v, None, None] for v in values]
    for i, node in enumerate(nodes):
        if node:
            if 2*i+1 < len(nodes): node[1] = nodes[2*i+1]
            if 2*i+2 < len(nodes): node[2] = nodes[2*i+2]
    return nodes[0]

values = input("Enter values in order: ").split(",")
values = [None if v.strip().lower() == "null" else int(v.strip()) for v in values]
print("Is valid BST?", is_valid_bst(build_tree(values)))