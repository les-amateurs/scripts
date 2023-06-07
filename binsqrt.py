import sys
sys.setrecursionlimit(5000)

def binsqrt(low, high, n, power):
    if high >= low:
        mid = (high + low) // 2
        if mid ** power == n:
            return mid
        elif mid ** power > n:
            return binsqrt(low, mid - 1, n, power)
        else:
            return binsqrt(mid + 1, high, n, power)
    else:
        return -1
#inaccurate mode
def flrsqrt(low, high, n, power):
    if high >= low:
        mid = (high + low) // 2
        if mid ** power == n:
            return mid
        elif mid ** power > n:
            return flrsqrt(low, mid - 1, n, power)
        else:
            return flrsqrt(mid + 1, high, n, power)
    else:
        return high

def ceilsqrt(low, high, n, power):
    if high >= low:
        mid = (high + low) // 2
        if mid ** power == n:
            return mid
        elif mid ** power > n:
            return ceilsqrt(low, mid - 1, n, power)
        else:
            return ceilsqrt(mid + 1, high, n, power)
    else:
        return low
