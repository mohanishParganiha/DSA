class Node:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = Node
            current_node = current_node.children[c]
        current_node.is_end_of_word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ans = []
        root = Trie()
        for word in words:
            root.add(word)

        word = ""

        def dfs(r, c, current_node):
            if current_node.is_end_of_word:
                ans.append(word)
                word = ""
                return

            if r < 0 or r >= len(board) or col < 0 or col >= len(board[0]) or board[r][c] not in current_node.childrend:
                return

            current_node = current_node.children[board[r][c]]
            word += board[r][c]

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r+dr, c+dc, current_node)

            board[r][c] = temp
            return

        dfs(0, 0, root)
        return ans
