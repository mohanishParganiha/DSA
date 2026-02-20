import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKSortedLists(lists: list[ListNode]):
    min_heap = []
    counter = 0
    heapq.heapify(min_heap)
    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.val, counter, head))
            counter += 1

    dummy = ListNode(0)
    curr = dummy
    while min_heap:
        min_val, count, min_node = heapq.heappop(min_heap)
        curr.next = min_node
        curr = curr.next
        if min_node.next:
            heapq.heappush(min_heap, (min_node.next.val,
                           counter, min_node.next))
            counter += 1

    return dummy.next
