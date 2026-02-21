def numberOfConnectedComponents(n: int, edges: list[list[int]]) -> int:
    adjacency_list = {node: [] for node in range(n)}
    for node1, node2 in edges:
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)

    seen_list = set()

    def dfs(node, parent):
        if node in seen_list:
            return
        seen_list.add(node)
        for neighbor in adjacency_list[node]:

            dfs(neighbor, node)
    number_of_connected_componenets = 0
    for node in range(n):
        if node not in seen_list:
            dfs(node, -1)
            number_of_connected_componenets += 1
    return number_of_connected_componenets
