"""
the qustion asks us to find the redundant connection (redundant edge ) in a given graph , baisically ask us
to remove this extra edge which makes the graph cyclic , and turn this graph into acyclic graph.

also if there are multiple answers , return the answer that occurs last in the input.

methodology ,
we start dfs , and traverse through until we find circle. if we find circle , we add that parent and node to as tuple into answer list
then we return the last element of this answer list. ->>> this method wont work it will give wrong answers
why ? becasue if we look at edges = [[1, 2],[1,3],[2,3]], we will get [1,3] whichis worng anwer casue 1,3 doesnot appears at last of input list.

so we approach with another method , we check for loops as we build the graph adjacency list , this way we knwo which edge(according to input list)
we are on . and we will append all the cyclic edges onto a stack and pop the top one out.
step1-> build empty adjacency list,
step 2 -> iterate through all the edges , for loop
step 3-> before adding to to adjacency list we check if this edge forms a loop
step 4-> if this forms a loop add to stack , skip this step if loop does not forms
step 5-> add this edge to graph even if its redundant edge
"""

edges = edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]


def redundantConnection(edges: list[list[int]]) -> list[int]:

    def has_cycle(start: int, target: int) -> bool:
        seen_set = set()  # cannot be global. why? one node can have many connection(not cyclic) and it will give false positives,   # space:O(n) worst case
        # Each edge check needs a fresh seen_set to avoid false positives

        # # below if statement is redundant , we already check it in dfs
        # if start == target:  # for self loop immedeate return
        #     return True

        def dfs(node):  # time : O(v+e)
            if node == target:  # check to see if we reached the target if so then there already exist a connection so return true
                return True
            if node in seen_set:  # if the node already exist in seen-set , its a different loop , return false to break infinite loop
                return False
            seen_set.add(node)  # add node before branching out in neighbors
            for neighbor in adjacency_list[node]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(start)

    redundant_edge = []
    # space : O(n+e)-> worst case if all node are connected to each other then O(n*n)
    adjacency_list = {node: [] for node in range(1, len(edges)+1, 1)}
    for node1, node2 in edges:  # O(n)
        # O(v+e)nodes and edges add till now -> worst case the last edge is redundant then O(V+E) all the edges and nodes
        if has_cycle(node1, node2):
            redundant_edge = [node1, node2]
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)

    return redundant_edge


print(redundantConnection(edges))
