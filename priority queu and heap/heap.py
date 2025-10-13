

class KthLargest:
    """
    To make min heap we make a Binary Tree with ceratin properites ,
        properties  of binary tree for min heap

        1) all the child node are less than parent node

        2) if we pop , we remove top root node,
            2.1) after poping root node, we take last node and put that into root node
                and readjust the tree to follow (1) property

        3) the tree is represented with array , the array is indexed by 1 not by 0
            3.1)the left child can be found by equation i*2 (where i is index in array)
            3.2)the right child can be ofund by equation i*2 +1 (where i is index)
            3.3) the parent of child can be found by floor(i/2) ,
                 i.e. 4/2 -> floor(2)->2, 5/2->floor(2.5)->2
            3.4) for 0 indexed arrays , left child = (i*2) +1 and right child = (i*2 +1) +1 and parent = (i-1)//2

        4) we create a new internal function that we use to optimize the tree ,
                every time we add new item , we add it to last node and then call optimize
                if the new item does not follow first tree propertie ,
            4.1) this new internal function calculate the parent (by (3.3)) and swap them ,
                  we dont call this function if the new item if if follows first tree property

    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.array = []

        for num in nums:

            self.array.append(num)
            child = len(self.array) - 1  # child index on 0 indexed array
            parent = (child - 1) // 2  # parent index on 0 indexed arrray
            if len(self.array) > 1:
                self._optimize_(child, parent)

    def add(self, val: int) -> int:
        # add functionality to return kth largest element . remove parent node one by one and optimize the nodes
        self.array.append(val)
        child = len(self.array) - 1
        parent = (child - 1) // 2

        if len(self.array) > 1:
            self._optimize_(child, parent)

    def _optimize_(self, child: int, parent: int):

        while self.array[child] > self.array[parent]:
            temp = self.array[child]
            self.array[child] = self.array[parent]
            self.array[parent] = temp

            child = parent
            parent = child // 2


priority_queue = KthLargest(3, [4, 5, 8, 2])
print(priority_queue.add(25))
