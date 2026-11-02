
import pytest
from solution import permutations


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([], [[]]),
        ([-1, 0], [[-1, 0], [0, -1]]),
        ([1, 1], [[1, 1], [1, 1]]),
        (
            [1, 1, 2],
            [
                [1, 1, 2],
                [1, 2, 1],
                [1, 1, 2],
                [1, 2, 1],
                [2, 1, 1],
                [2, 1, 1],
            ],
        ),
        ([5, 5, 5], [[5, 5, 5]] * 6),
    ],
)
def test_expected_permutations(nums, expected):
    assert permutations(nums) == expected


@pytest.mark.parametrize(
    "nums, expected_count",
    [
        ([], 1),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([1, 2, 3, 4, 5], 120),
    ],
)
def test_number_of_permutations(nums, expected_count):
    assert len(permutations(nums)) == expected_count


def test_all_permutations_unique():
    result = permutations([1, 2, 3, 4])

    assert len(result) == len(set(tuple(p) for p in result))


def test_all_elements_present():
    nums = [1, 2, 3, 4]
    result = permutations(nums)

    assert all(sorted(p) == sorted(nums) for p in result)
    assert all(len(p) == len(nums) for p in result)


def test_original_list_unchanged():
    nums = [3, 1, 2]
    permutations(nums)

    assert nums == [3, 1, 2]


def test_input_order_preserved():
    result = permutations([3, 1, 2])

    assert result[0] == [3, 1, 2]
    assert result[-1] == [2, 1, 3]


def test_independent_result_lists():
    result = permutations([1, 2, 3])

    result[0][0] = 100

    assert result[1] == [1, 3, 2]


def test_result_independent_of_input():
    nums = [1, 2]
    result = permutations(nums)

    nums[0] = 99

    assert result == [[1, 2], [2, 1]]


def test_exact_trace(capsys):
    assert permutations([1, 2]) == [[1, 2], [2, 1]]

    trace = capsys.readouterr().out.splitlines()

    assert trace == [
        "→ backtrack([])",
        "  → backtrack([1])",
        "    → backtrack([1, 2])",
        "    ← backtrack = None",
        "  ← backtrack = None",
        "  → backtrack([2])",
        "    → backtrack([2, 1])",
        "    ← backtrack = None",
        "  ← backtrack = None",
        "← backtrack = None",
    ]


def test_trace_depth(capsys):
    permutations([1, 2, 3])
    trace = capsys.readouterr().out.splitlines()

    assert trace[0] == "→ backtrack([])"
    assert "      → backtrack([1, 2, 3])" in trace
    assert trace[-1] == "← backtrack = None"


def test_trace_empty_list(capsys):
    assert permutations([]) == [[]]

    trace = capsys.readouterr().out.splitlines()

    assert trace == [
        "→ backtrack([])",
        "← backtrack = None",
    ]


def test_repeated_calls(capsys):
    first = permutations([1, 2])
    capsys.readouterr()

    second = permutations([0, 1])
    trace = capsys.readouterr().out.splitlines()

    assert first == [[1, 2], [2, 1]]
    assert second == [[0, 1], [1, 0]]
    assert trace[0] == "→ backtrack([])"
