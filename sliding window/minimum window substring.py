from collections import defaultdict, Counter


def minWindow(s: str, t: str):

    counter_t = Counter(t).items()
    counter_s = defaultdict(int)

    left = 0
    right = 0

    min_window = ""
    min_window_len = float('inf')

    def compare_counters(counter_s, counter_t):
        for key, value in counter_t:
            if counter_s[key] < value:
                return False
        return True

    for right in range(len(s)):
        if not compare_counters(counter_s, counter_t):
            counter_s[s[right]] += 1

        while compare_counters(counter_s, counter_t) and left <= right:
            if (right-left) < min_window_len:
                min_window_len = min(min_window_len, (right-left))
                min_window = s[left:right+1]
            counter_s[s[left]] -= 1
            left += 1

    return min_window


print(minWindow("a", "a"))
