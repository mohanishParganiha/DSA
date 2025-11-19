import heapq

trips = [[10, 5, 7], [10, 3, 4], [7, 1, 8], [6, 3, 4]]
capacity = 24


def poolingCar(trips: list[list[int]],  capacity: int) -> bool:
    trips = sorted(trips, key=lambda x: x[1])
    dropOffMap = []
    heapq.heapify(dropOffMap)

    passengerSeated = 0

    for num_passenger, pick_up,  drop_off in trips:
        while dropOffMap and dropOffMap[0][0] <= pick_up:
            passengerSeated -= heapq.heappop(dropOffMap)[1]

        passengerSeated += num_passenger
        heapq.heappush(dropOffMap, (drop_off, num_passenger))

        if passengerSeated > capacity:
            return False

    if passengerSeated <= capacity:
        return True


print(poolingCar(trips, capacity))
