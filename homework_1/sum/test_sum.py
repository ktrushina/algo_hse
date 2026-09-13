from sum import max_even_sum


def test_even_sum():
    assert max_even_sum([5, 7, 13, 2, 14]) == 36


def test_only_odd_number():
    assert max_even_sum([3]) == 0


def test_all_even():
    assert max_even_sum([2, 4, 6]) == 12


def test_odd_sum():
    assert max_even_sum([1, 2, 4]) == 6


def test_one_odd_number():
    assert max_even_sum([5, 2, 4]) == 6


def test_multiple_odd_numbers():
    assert max_even_sum([3, 5, 7, 2]) == 14
