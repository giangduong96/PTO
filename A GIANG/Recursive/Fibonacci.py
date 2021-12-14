def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b , a)

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (bad_fibonacci(n-2) + bad_fibonacci(n-1))

if __name__ == '__main__':
    print(good_fibonacci(9))
    print(bad_fibonacci(8))