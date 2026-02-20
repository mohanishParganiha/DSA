def activitySelection(activities: list):
    activities.sort(key=lambda x: x[1])

    selected = []
    start_timer = 0

    for i in range(len(activities)):
        if activities[i][0] >= start_timer:
            selected.append(activities[i])
            start_timer = activities[i][1]
    return len(selected), selected


activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
count, selected_activities = activitySelection(activities)
print(f"Count: {count}")
print(f"Selected: {selected_activities}")
