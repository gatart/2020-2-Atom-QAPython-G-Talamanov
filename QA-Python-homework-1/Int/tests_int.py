import random
import math
import pytest


def test_1(random_int):
    print(random_int)
    assert math.sqrt(random_int) >= 0


def test_2(random_int):
    with pytest.raises(ZeroDivisionError):
        assert random_int / 0


def test_3(random_int):
    assert (random_int + 1).bit_length() != 0


class TestClass:
    def test_4(self, random_int):
        assert ~random_int != random_int


@pytest.mark.parametrize('i', (5, random.randint(6, 100), 100))
def test_5(i, random_int):
    with pytest.raises(ZeroDivisionError):
        assert random_int / 0
        assert i / 0
