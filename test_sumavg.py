from sumavg import sum_list, avg_list
import pytest

def test_normal():
    assert sum_list([10, 20, 30]) == 60
    assert avg_list([2, 4, 6]) == 4.0

def test_empty():
    with pytest.raises(ValueError):
        sum_list([])

def test_invalid():
    with pytest.raises(ValueError):
        avg_list([1, "a", 3])
