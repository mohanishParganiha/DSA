from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, negihbors in self.adj_list.items():
            graph_str += f"{node} -> {negihbors}\n"

        return graph_str

    def add_node(self, node) -> None:
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("node already exists ")

    def remove_node(self, node) -> None:
        if node not in self.adj_list:
            raise ValueError("node does not exist")

        for neighbors in self.adj_list.values:
            neighbors.discard(node)

        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None) -> None:
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)

    def remove_edge(self, from_node, to_node) -> None:
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError("edge dose not exist")
            if not self.directed:
                if to_node in self.adj_list[from_node]:
                    self.adj_list[to_node].remove(from_node)

        else:
            raise ValueError("edge does not exist")

    def get_neighbour(self, node) -> bool:
        return self.adj_list.get(node, set())

    def has_node(self, node) -> bool:
        return node in self.adj_list

    def has_edge(self, from_node, to_node) -> bool:
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    def get_nodes(self) -> list:
        return list(self.adj_list.keys())

    def get_edges(self) -> list:
        edges = []
        for node in self.adj_list:
            for neighbor in self.adj_list[node]:
                edges.append((node, neighbor))
        return edges

    def dfs(self, start):
        visited = set()

        def helper(node):
            visited.add(node)
            print(node)

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    helper(neighbor)

        helper(start)

    def bfs(self, start):
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)

        while queue:
            curr_node = queue.popleft()
            print(curr_node)
            for neighbor in self.adj_list[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# g.dfs(1)
g.bfs(1)
