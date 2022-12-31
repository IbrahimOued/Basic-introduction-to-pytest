import pytest

@pytest.fixture
def sequence():
    return [1, 2, 3]

def test_sum():
    assert sum(sequence) == 6

def text_max():
    assert max(sequence) == 3