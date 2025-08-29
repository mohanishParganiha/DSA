target = 10
position = [6, 8]
speed = [3, 2]

sorted_car_pos_and_speed = sorted(zip(position, speed))

time = [(target-p)/s for p, s in sorted_car_pos_and_speed]
print(time)
ans = 0

while len(time) > 1:
    lead = time.pop()
    if lead < time[-1]:  # if lead(car with heighest position) arrive faster than
        # second lead(time[-1],car with second heighest position) then lead cant be caught
        ans += 1
    else:
        time[-1] = lead  # if not then second lead caught the lead and
        # will travel with the speed of lead i.e slower car's speed

print(ans + bool(time))
