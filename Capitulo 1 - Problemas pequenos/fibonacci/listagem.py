from functools import lru_cache
from typing import Dict, Generator


def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


memo_fib3: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo_fib3:
        memo_fib3[n] = fib3(n - 1) + fib3(n - 2)
    return memo_fib3[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


def fib5(n: int) -> int:
    if n == 0:
        return n
    last_n: int = 0
    next_n: int = 1
    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
    return next_n


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last_n: int = 0
    next_n: int = 1
    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
        yield next_n
