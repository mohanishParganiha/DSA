# first create a adjacency list from edge list and n
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]


def validTree(n: int, edges: list[list[int]]) -> bool:
    # number of edges for graph valid tree is n-1, if there are n nodes
    if len(edges) != n-1:
        return False

    adjacency_list = {node: [] for node in range(n)}
    for node1, node2 in edges:
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)

    # things to look for ,
    # check if the graph tree does not has cycles with seen set
    #  we need to track parent/prev node so we dont go back to where we came from
    # next in dfs if we reach k nodes , and if k==n-1, then its graph valid tree

    seen_set = set()

    def dfs(node, parent):
        if node in seen_set:
            return False
        seen_set.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node):
                return False
        return True

    if not dfs(0, -1):
        return False
    if len(seen_set) != n:
        return False
    return True


print(validTree(n, edges))

# Test 1: Valid tree
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(validTree(n, edges))  # Should be True

# Test 2: Has cycle
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(validTree(n, edges))  # Should be False

# Test 3: Disconnected
n = 5
edges = [[0, 1], [2, 3]]
print(validTree(n, edges))  # Should be False

# Test 4: Single node
n = 1
edges = []
print(validTree(n, edges))  # Should be True

# Test 5: Two nodes, connected
n = 2
edges = [[0, 1]]
print(validTree(n, edges))  # Should be True

# Test 6: Two nodes, disconnected
n = 2
edges = []
print(validTree(n, edges))  # Should be False
