
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
    ],
)
def test_expected_permutations(nums, expected, capsys):
    assert permutations(nums) == expected
    capsys.readouterr()


def test_number_of_permutations(capsys):
    assert len(permutations([1, 2, 3, 4])) == 24
    capsys.readouterr()


def test_all_permutations_unique(capsys):
    result = permutations([1, 2, 3])
    capsys.readouterr()

    assert len(result) == len(set(tuple(p) for p in result))


def test_original_list_unchanged(capsys):
    nums = [1, 2, 3]
    permutations(nums)
    capsys.readouterr()

    assert nums == [1, 2, 3]


def test_independent_result_lists(capsys):
    result = permutations([1, 2, 3])
    capsys.readouterr()

    result[0][0] = 100

    assert result[1] == [1, 3, 2]


def test_exact_trace(capsys):
    assert permutations([1, 2]) == [[1, 2], [2, 1]]

    trace = capsys.readouterr().out.splitlines()

    assert trace == [
        '→ backtrack([])',
        '  → backtrack([1])',
        '    → backtrack([1, 2])',
        '    ← backtrack = None',
        '  ← backtrack = None',
        '  → backtrack([2])',
        '    → backtrack([2, 1])',
        '    ← backtrack = None',
        '  ← backtrack = None',
        '← backtrack = None',
    ]


def test_trace_depth(capsys):
    permutations([1, 2, 3])
    trace = capsys.readouterr().out.splitlines()

    assert trace[0] == '→ backtrack([])'
    assert '      → backtrack([1, 2, 3])' in trace
    assert trace[-1] == '← backtrack = None'


def test_repeated_calls(capsys):
    first = permutations([1, 2])
    capsys.readouterr()

    second = permutations([0, 1])
    trace = capsys.readouterr().out.splitlines()

    assert first == [[1, 2], [2, 1]]
    assert second == [[0, 1], [1, 0]]
    assert trace[0] == '→ backtrack([])'
