import pytest

from fibonacci.listagem import *

n_target = 25
target_result = 75025


def test_fib1():
    with pytest.raises(RecursionError):
        fib1(n_target)


def test_fib2(benchmark):
    assert benchmark(fib2, n_target) == target_result


def test_fib3(benchmark):
    assert benchmark(fib3, n_target) == target_result


def test_fib4(benchmark):
    assert benchmark(fib4, n_target) == target_result


def test_fib5(benchmark):
    assert benchmark(fib5, n_target) == target_result


def test_fib6(benchmark):
    assert list(benchmark(fib6, n_target)).pop() == target_result
