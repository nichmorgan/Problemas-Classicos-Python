import math

from calculating_pi import calculating_pi


def test_calculating_pi():
    assert abs(calculating_pi(int(1e5)) - math.pi) < 1e-4
