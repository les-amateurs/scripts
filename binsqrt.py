def binsqrt(low, high, n, power):
    if high >= low:
        mid = (high + low) // 2
        if mid ** power == n:
            return mid
        elif mid ** power > n:
            return binary_search(low, mid - 1, n, power)
        else:
            return binary_search(mid + 1, high, n, power)
    else:
        return -1

