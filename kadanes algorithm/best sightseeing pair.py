values = [2, 2, 1]


def maxScoreSightseeingPair(values):
    length = len(values)
    max_score = float('-inf')
    score = 0

    i = 0
    j = length-1

    if i < j:
        max_score = values[i] + values[j] + (i-j)

        if values[i] + values[j-1] + (i-j-1) >= values[i+1]+values[j] + (i+1-j):
            max_score = max(max_score, maxScoreSightseeingPair(values[i:j]))
        else:

            max_score = max(
                max_score, maxScoreSightseeingPair(values[i+1:j+1]))

    return max_score


print(maxScoreSightseeingPair(values))
