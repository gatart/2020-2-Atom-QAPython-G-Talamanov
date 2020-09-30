import pytest
import random


def test_1(rand_list):
    a = rand_list
    x = random.randint(100, 200)
    a.append(x)
    assert a.count(x) == 1


class TestClass:
    def test_2(self, rand_list):
        a = rand_list
        a.reverse()
        a.reverse()
        assert a == rand_list


@pytest.mark.parametrize('i', (0, random.randint(1, 4), 4))
def test_3(i, rand_list):
    with pytest.raises(ValueError):
        assert rand_list.remove(100)


def test_4(rand_list):
    a = rand_list.copy()
    assert a == rand_list


def test_5(rand_list):
    a = rand_list
    x = random.randint(100, 200)
    a.insert(3, x)
    assert a.count(x) == 1
