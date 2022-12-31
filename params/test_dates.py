import pytest
from datetime import datetime, timedelta

data = [
    (datetime(2022, 12, 21), datetime(2022, 12, 20), timedelta(1)),
    (datetime(2022, 12, 20), datetime(2022, 12, 21), timedelta(1)),
]
@pytest.mark.parametrize("a, b, expected", data)
def test_delat(a, b, expected):
    diff = a - b
    assert diff == expected