import heapq


tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]

tasks = [[item[0], item[1], idx] for idx, item in enumerate(tasks)]
tasks.sort(reverse=True)
print(tasks)

processing_que = []
heapq.heapify(processing_que)

curr_time = 0
output = []

while tasks or processing_que:
    while tasks and tasks[-1][0] <= curr_time:
        enque_time, processing_time, idx = tasks.pop()
        heapq.heappush(processing_que, (processing_time, idx))

    if processing_que:
        min_processing_time, index = heapq.heappop(processing_que)
        curr_time += min_processing_time
        output.append(index)
    else:
        curr_time = tasks[-1][0]


print(output)
