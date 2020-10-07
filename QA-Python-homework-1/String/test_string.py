import pytest
import random


def test_1(rand_str):
    assert rand_str * 3 == rand_str + rand_str + rand_str


@pytest.mark.parametrize('i', (' ' + 'string', ' ' * random.randint(1, 10) + 'string', ' ' * 10 + 'string'))
def test_2(i):
    assert i.lstrip() == 'string'


def test_3(rand_str):
    a = rand_str
    assert a[:] == a


def test_4(rand_str):
    assert len(rand_str) == 16


class TestClass:
    def test_5(self, rand_str):
        line = rand_str
        with pytest.raises(IndexError):
            assert line[17]
