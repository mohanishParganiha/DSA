numCourses = 2  # total number of courses to take
# [[ai,bi]], to take course ai , we need to complete course bi, bi->ai
prerequisits = [[1, 0]]


def courseSchedule(numCourses: int, prerequisits: list[list[int]]):
    graph = {key: [] for key in range(numCourses)}

    for course_to_take, course_to_take_before in prerequisits:
        graph[course_to_take_before].append(course_to_take)

    # states[node] = 0, unvisited.
    # states[node] = 1, visiting
    # states[node] = 2, visited
    states = {node: 0 for node in graph.keys()}

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
        return False

    for node in graph.keys():
        if states[node] == 0:
            if dfs(node):
                return False
    return True


print(courseSchedule(numCourses, prerequisits))
