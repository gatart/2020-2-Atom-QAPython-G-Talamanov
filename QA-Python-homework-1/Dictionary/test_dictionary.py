import pytest
import random


def test_1(rand_dict):
    c = rand_dict.copy()
    assert c == rand_dict


def test_2(rand_dict):
    assert rand_dict.clear() != rand_dict


class TestClass:
    def test_3(self, rand_dict):
        assert rand_dict.items()


@pytest.mark.parametrize('i', (0, random.randint(1,4), 4))
def test_4(i, rand_dict):
    assert rand_dict.pop(i)


@pytest.mark.parametrize('i', (0, random.randint(1,4), 4))
def test_5(i, rand_dict):
    assert rand_dict.get(i)

