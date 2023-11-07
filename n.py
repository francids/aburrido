def fibo(n) -> list[int]:
    fib: list[int] = [0, 1]
    for x in range(n):
        fib.append(fib[-2] + fib[-1])
    return fib


print(fibo(10))


def fibo_pos(n) -> int:
    fib: list[int] = [0, 1]
    for x in range(n):
        fib.append(fib[-2] + fib[-1])
    return fib[-1]


print(fibo_pos(10))


def is_fibo(n) -> bool:
    if n < 0:
        return False
    fib: list[int] = [0, 1]
    for x in range(n):
        fib.append(fib[-2] + fib[-1])
        if fib[-1] > n:
            return False
        if fib[-1] == n:
            return True
    return False


print(f"55 is fibo? {is_fibo(55)}")
print(f"60 is fibo? {is_fibo(60)}")
