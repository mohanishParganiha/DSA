graph = {
    1: [2],
    2: [3],
    3: [2]  # Cycle: 2→3→2
}


def detectCycle(graph):
    # state = 0 ,unvisited . state=1,visiting. state=2,visited.
    state = {node: 0 for node in graph.keys()}

    def dfs(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False

        state[node] = 1  # mark  as visiting at start

        for neighbour in graph[node]:
            # check if the neighbour is already visited or visiting
            if dfs(neighbour):
                return True

        # if everything's fine then at last mark this node as visited
        state[node] = 2  # mark as visited
        return False

    for nodes in graph.keys():
        if state[nodes] == 0:
            if dfs(nodes):
                return True

    return False


print(detectCycle(graph))
