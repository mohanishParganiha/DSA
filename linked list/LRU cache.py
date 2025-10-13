from typing import Optional


class ListNode:
    def __init__(self, val: int, key: int, prev: Optional["ListNode"], next: Optional["ListNode"]):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

    def __delattr__(self, name):
        pass


class LRUCache:
    def __init__(self, capacity: int):

        self.capacity = capacity

        self.head = ListNode(-1, -1, None, None)
        self.tail = ListNode(-1, -1, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hash_map = dict()

    def get(self, key: int) -> int:
        if key in self.hash_map:
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        def put_if_hash_map_not_at_full_capacity(key: int, value: int) -> None:
            temp = ListNode(value, key, None, None)
            temp1 = self.tail.prev
            temp1.next = temp
            temp.prev = temp1
            temp.next = self.tail
            self.tail.prev = temp

            self.hash_map[key] = temp

        if key in self.hash_map:
            self.hash_map[key].val = value

        else:
            if len(self.hash_map) < self.capacity:
                put_if_hash_map_not_at_full_capacity(key, value)

            else:
                lru_node_key = self.head.next.key
                self.hash_map.pop(lru_node_key)
                node_after_lru_node = self.head.next.next
                self.head.next = node_after_lru_node
                node_after_lru_node.prev = self.head
                del self.head.next

                put_if_hash_map_not_at_full_capacity(key, value)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
