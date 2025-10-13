"""
give :
    we have a input stream of task = ['A','A','B','C']
    we have integer n , which indecates number of interval i have to skip before doing same task
        i.e , n = 2, after first 'A' we have to wait for 2 interval , same for 'B',
    so cpu is allowed to be idel, the
    for above eg. the cpu will handle task like 'A'->'B'->'C'->'A'
    output = 4 (4 steps )

    another eg : tasks = ["A","A","A","B","B","B"], n = 2
    then for above:
            'A'->'B'->idel->'A'->'B'->idel->'A'->'B'
            output = 8

    to solve this problem , is to use priority queue
    1)we create a max_heap of frequency of task items,
    2) we create a cooldown_queue , the items which will go in follow (time_ready,task,freq)
    3)each iteration we go through whole queue and filter out task which have
                time_ready == time and push them onto max-heap
    4) we pop from max-heap if there is something on max-heap
                ->if we get something from max-heap
                        we decrement frequecy and store it one cooldown_queue
                        cooldown_queue.append([time_ready,task,freq])
                ->if the max-heap is empty we skip to next time by settings time variable
                time = cooldown_queue[0][0] -> get time for task


"""
import heapq
from collections import deque, Counter


def taskScheduler(tasks: list[str], n: int) -> int:
    countdown_q = deque()
    max_freq_heap = [(-freq, task)for task, freq in Counter(tasks).items()]
    heapq.heapify(max_freq_heap)
    time = 0
    while countdown_q or max_freq_heap:
        while countdown_q and countdown_q[0][0] <= time:
            item = countdown_q.popleft()
            heapq.heappush(max_freq_heap, (item[2], item[1]))

        if max_freq_heap:
            freq, task = heapq.heappop(max_freq_heap)
            freq += 1
            if freq != 0:
                countdown_q.append([time+n+1, task, freq])

            time += 1

        else:
            time = countdown_q[0][0]

    return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(taskScheduler(tasks, n))
