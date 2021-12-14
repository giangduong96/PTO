def getSum(a: int, b: int):
    mask = 0xFFFFFFFF

    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    max_int = 0x7FFFFFFF

    return a if a < max_int else ~(a ^ mask)


print(getSum(-1, 4))

# best
def getSum1(a: int, b: int) -> int:
    x, y = abs(a), abs(b)
    # ensure x >= y
    if x < y:
        return getSum(b, a)
    sign = 1 if a > 0 else -1

    if a * b >= 0:
        # sum of two positive integers
        while y:
            x, y = x ^ y, (x & y) << 1
    else:
        # difference of two positive integers
        while y:
            x, y = x ^ y, ((~x) & y) << 1

    return x * sign

print(getSum1(-1, 4))
print(~100)