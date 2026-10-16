from lp import is_leap_year

def test_leap():
    assert is_leap_year(2024) == True

def test_not_leap():
    assert is_leap_year(2023) == False
