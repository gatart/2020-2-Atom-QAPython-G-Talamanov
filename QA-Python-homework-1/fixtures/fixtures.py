import pytest
import random
import string


@pytest.fixture()
def random_int():
    print('entering')
    yield random.randint(5, 100)
    print('exiting')


@pytest.fixture()
def rand_str():
    yield ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))


@pytest.fixture()
def rand_dict():
    yield {a: random.randint(1, 100) for a in range(5)}


@pytest.fixture()
def rand_list():
    yield [random.randint(1, 100) in range(5)]


@pytest.fixture()
def rand_set():
    yield {random.randint(1, 100) for i in range(10)}
