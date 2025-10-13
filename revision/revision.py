asteroids = [5, 10, -5]


def asteroidCollisions(asteroids: list[int]) -> list[int]:
    ans = []

    for asteroid in asteroids:

        while ans and asteroid < 0 < ans[-1]:
            prev_asteroid = ans.pop()
            if abs(asteroid) > abs(prev_asteroid):
                ans.append(asteroid)
            elif abs(prev_asteroid) > abs()
