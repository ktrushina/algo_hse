def two_sum(arr, k):
    seen = {}

    for i, num in enumerate(arr):
        needed = k - num

        if needed in seen:
            return seen[needed], i

        seen[num] = i
