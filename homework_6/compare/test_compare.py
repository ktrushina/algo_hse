import pytest

from compare import mergesort_recursive, partition, quicksort_recursive, timed

SORTS = [mergesort_recursive, quicksort_recursive]


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("nums", [
    pytest.param([], id="empty"),
    pytest.param([8], id="single"),
    pytest.param([2, 1], id="reversed-pair"),
    pytest.param([4] * 30, id="all-equal"),
    pytest.param([-4, 0, -4, 7, 1], id="negative-with-duplicates"),
    pytest.param(list(range(1200)), id="ascending"),
    pytest.param(list(range(50, -1, -1)), id="descending"),
    pytest.param([3, -1, 0, 4] * 64 + [-2], id="odd-length"),
])
def test_sort_returns_sorted_copy(sort, nums):
    fresh = nums.copy()
    result = sort(fresh)
    assert result == sorted(nums)
    assert fresh == nums
    assert result is not fresh


@pytest.mark.parametrize("sort", SORTS)
def test_large_input_with_repeated_descending_blocks(sort):
    nums = list(range(100, 0, -1)) * 1000
    assert sort(nums.copy()) == sorted(nums)


def test_partition_rechecks_swapped_value_and_preserves_neighbors():
    nums = [90, 4, 1, 5, 2, 3, 91]
    assert partition(nums, 1, 5, 3) == (3, 3)
    assert nums == [90, 1, 2, 3, 5, 4, 91]


def test_partition_groups_all_equal_values():
    nums = [7] * 40
    assert partition(nums, 0, 39, 7) == (0, 39)


def test_timer_forwards_arguments_and_returns_elapsed_seconds():
    @timed
    def plus(a, b=0):
        return a + b

    result, seconds = plus(3, b=4)
    assert result == 7
    assert seconds >= 0
