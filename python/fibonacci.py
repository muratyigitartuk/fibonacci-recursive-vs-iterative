def fib_recursive_memo(n, memo=None):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
        return n
    result = fib_recursive_memo(n - 1, memo) + fib_recursive_memo(n - 2, memo)
    memo[n] = result
    return result


def fib_iterative(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a