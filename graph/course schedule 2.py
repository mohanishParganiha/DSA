numCourses = 2
prerequisites = [[1, 0]]


def findOrder(numCourses: int, prerequisites: list[list[int]]):
    graph = {node: [] for node in range(numCourses)}
    for neighbor, node in prerequisites:
        graph[node].append(neighbor)

    states = {node: 0 for node in range(numCourses)}
    stack = []

    def dfs(node):
        if states[node] == 1:
            return True
        if states[node] == 2:
            return False

        states[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        states[node] = 2
        stack.append(node)
        return False

    for node in graph.keys():
        if states[node] == 0:
            if dfs(node):
                return []
    return stack[::-1]


print(findOrder(numCourses, prerequisites))
