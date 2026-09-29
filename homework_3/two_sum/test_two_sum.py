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


def test_minimal_array():
    assert two_sum([3, 4], 7) == (0, 1)


def test_zero_and_negative():
    assert two_sum([0, -1, 5, 2], 1) == (0, 3)


def test_two_zeros():
    assert two_sum([0, 5, 0, 3], 0) == (0, 2)


def test_duplicate_number_pairs_with_itself():
    assert two_sum([5, 1, 5, 2], 10) == (0, 2)


def test_pair_with_repeated_number_not_first_occurrence():
    assert two_sum([3, 5, 3, 5], 8) == (0, 1)


def test_large_numbers():
    assert two_sum([1_000_000_000, 2, 3, 999_999_997], 1_999_999_997) == (0, 3)


def test_result_indices_ascending():
    result = two_sum([8, 1, 2, 9], 3)
    assert result[0] < result[1]


def test_three_element_array():
    assert two_sum([2, 7, 11], 9) == (0, 1)
