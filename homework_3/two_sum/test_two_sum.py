from two_sum import two_sum


def test_two_sum():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)


def test_same_numbers():
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_negative_numbers():
    assert two_sum([-3, 4, 2, 7], 1) == (0, 1)


def test_pair_at_end():
    assert two_sum([1, 2, 8, 9], 17) == (2, 3)


def test_unsorted_array():
    assert two_sum([10, 1, 6, 3], 9) == (1, 3)
