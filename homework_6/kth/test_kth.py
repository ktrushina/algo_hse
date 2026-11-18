from itertools import product

import pytest

from kth import kth_largest


@pytest.mark.parametrize("nums,k,expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
])
def test_examples(nums, k, expected):
    assert kth_largest(nums, k) == expected


@pytest.mark.parametrize("length", range(1, 6))
def test_all_ranks_on_small_inputs(length):
    for values in product((-2, 0, 3), repeat=length):
        for k, expected in enumerate(sorted(values, reverse=True), 1):
            nums = list(values)
            assert kth_largest(nums, k) == expected, (values, k)
            assert nums == list(values)


@pytest.mark.parametrize("nums,k", [([], 1), ([1], 0), ([1, 2], 3), ([1], -1)])
def test_invalid_rank(nums, k):
    with pytest.raises(ValueError):
        kth_largest(nums, k)


@pytest.mark.parametrize("k,expected", [(2, 4), (4, 2)])
def test_rank_on_each_side_of_first_pivot(k, expected):
    assert kth_largest([4, 1, 5, 2, 3], k) == expected


@pytest.mark.parametrize("k", [2, 4])
def test_rank_at_edges_of_equal_block(k):
    assert kth_largest([5, 1, 5, 9, 5], k) == 5


@pytest.mark.parametrize("k,expected", [(50000, 7), (50001, 0)])
def test_large_input_at_boundary_between_duplicate_values(k, expected):
    nums = [7, -2, 7, 0] * 25000
    assert kth_largest(nums, k) == expected
