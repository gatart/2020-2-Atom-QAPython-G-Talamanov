import pytest
import random


class TestClass:
    def test_1(self, rand_set):
        a = {random.randint(100, 200) for i in range(10)}
        assert rand_set.isdisjoint(a)


def test_2(rand_set):
    a = rand_set.copy()
    assert a == rand_set


def test_3(rand_set):
    with pytest.raises(KeyError):
        assert rand_set.remove(random.randint(100, 200))


def test_4(rand_set):
    assert not rand_set.clear()


@pytest.mark.parametrize('i', ({random.randint(-4, 0) in range(10)},
                               {random.randint(1, 100)}, {random.randint(100, 200)}))
def test_5(i, rand_set):
    assert (rand_set | i) & rand_set == rand_set

