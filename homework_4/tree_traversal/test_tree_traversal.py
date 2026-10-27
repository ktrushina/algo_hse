import random

import pytest

from solution import BST

METHODS = [
    "preorder",
    "inorder",
    "postorder",
    "reverse_preorder",
    "reverse_inorder",
    "reverse_postorder",
]

# Пример из README
README_VALUES = [8, 3, 10, 1, 6, 14, 4, 7, 13]
README_EXPECTED = {
    "preorder": [8, 3, 1, 6, 4, 7, 10, 14, 13],
    "inorder": [1, 3, 4, 6, 7, 8, 10, 13, 14],
    "postorder": [1, 4, 7, 6, 3, 13, 14, 10, 8],
    "reverse_preorder": [8, 10, 14, 13, 3, 6, 7, 4, 1],
    "reverse_inorder": [14, 13, 10, 8, 7, 6, 4, 3, 1],
    "reverse_postorder": [13, 14, 10, 7, 4, 6, 1, 3, 8],
}


def build_bst(values):
    """Создаёт BST из списка значений."""
    tree = BST()
    for value in values:
        tree.insert(value)
    return tree


def assert_valid_bst(tree):
    """Проверяет инвариант BST: для каждого узла min < value < max по всем предкам.

    Обход итеративный, чтобы сам хелпер не падал на глубоких деревьях.
    """
    stack = [(tree.root, None, None)] if tree.root is not None else []
    while stack:
        node, low, high = stack.pop()
        if low is not None:
            assert node.value > low
        if high is not None:
            assert node.value < high
        if node.left is not None:
            stack.append((node.left, low, node.value))
        if node.right is not None:
            stack.append((node.right, node.value, high))


# ---------- базовые случаи ----------

@pytest.mark.parametrize("method", METHODS)
def test_empty_tree(method):
    tree = BST()
    assert tree.root is None
    assert getattr(tree, method)() == []


@pytest.mark.parametrize("method", METHODS)
def test_single_node(method):
    assert getattr(build_bst([5]), method)() == [5]


@pytest.mark.parametrize("method", METHODS)
def test_readme_example(method):
    tree = build_bst(README_VALUES)
    assert getattr(tree, method)() == README_EXPECTED[method]
    assert_valid_bst(tree)


def test_readme_example_structure():
    tree = build_bst(README_VALUES)
    root = tree.root
    assert root.value == 8
    assert root.left.value == 3 and root.right.value == 10
    assert root.left.left.value == 1 and root.left.right.value == 6
    assert root.left.right.left.value == 4 and root.left.right.right.value == 7
    assert root.right.left is None and root.right.right.value == 14
    assert root.right.right.left.value == 13


def test_perfect_tree_all_traversals():
    tree = build_bst([8, 4, 12, 2, 6, 10, 14])
    assert tree.preorder() == [8, 4, 2, 6, 12, 10, 14]
    assert tree.inorder() == [2, 4, 6, 8, 10, 12, 14]
    assert tree.postorder() == [2, 6, 4, 10, 14, 12, 8]
    assert tree.reverse_preorder() == [8, 12, 14, 10, 4, 6, 2]
    assert tree.reverse_inorder() == [14, 12, 10, 8, 6, 4, 2]
    assert tree.reverse_postorder() == [14, 10, 12, 6, 2, 4, 8]


# ---------- вырожденные деревья ----------

def test_right_chain():
    tree = build_bst([1, 2, 3, 4, 5])
    assert tree.preorder() == [1, 2, 3, 4, 5]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_preorder() == [1, 2, 3, 4, 5]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_postorder() == [5, 4, 3, 2, 1]


def test_left_chain():
    tree = build_bst([5, 4, 3, 2, 1])
    assert tree.preorder() == [5, 4, 3, 2, 1]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [1, 2, 3, 4, 5]
    assert tree.reverse_preorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_postorder() == [1, 2, 3, 4, 5]


def test_zigzag_tree():
    # чередование лево/право: ловит сравнение с корнем вместо текущего узла
    tree = build_bst([10, 5, 7, 6, 8])
    assert tree.root.left.value == 5
    assert tree.root.left.right.value == 7
    assert tree.root.left.right.left.value == 6
    assert tree.root.left.right.right.value == 8
    assert tree.inorder() == [5, 6, 7, 8, 10]
    assert_valid_bst(tree)


def test_value_between_ancestors_goes_to_correct_side():
    # 6 < 10 и 6 > 5 и 6 < 7: путь root → 5 → 7 → левый потомок 7
    tree = build_bst([10, 5, 7])
    tree.insert(6)
    assert tree.root.left.right.left.value == 6
    assert_valid_bst(tree)


# ---------- глубина (ловушка рекурсии) ----------

@pytest.mark.parametrize("values", [
    list(range(1, 5001)),
    list(range(5000, 0, -1)),
])
@pytest.mark.parametrize("method", METHODS)
def test_deep_chain_does_not_overflow(values, method):
    tree = build_bst(values)
    result = getattr(tree, method)()
    assert len(result) == 5000
    assert sorted(result) == list(range(1, 5001))


def test_deep_chain_exact_order():
    n = 5000
    tree = build_bst(range(1, n + 1))
    assert tree.inorder() == list(range(1, n + 1))
    assert tree.reverse_inorder() == list(range(n, 0, -1))
    assert tree.postorder() == list(range(n, 0, -1))
    assert tree.preorder() == list(range(1, n + 1))


# ---------- дубликаты ----------

def test_duplicates_ignored():
    tree = build_bst([5, 3, 7, 3, 5, 7])
    assert tree.inorder() == [3, 5, 7]
    assert_valid_bst(tree)


def test_duplicate_into_empty_tree():
    tree = BST()
    tree.insert(5)
    tree.insert(5)
    assert tree.root.value == 5
    assert tree.root.left is None and tree.root.right is None
    assert tree.preorder() == [5]


def test_duplicate_deep_in_tree():
    tree = build_bst(README_VALUES)
    tree.insert(13)
    tree.insert(4)
    assert tree.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_duplicate_does_not_change_structure():
    tree = build_bst(README_VALUES)
    before = tree.preorder()
    for v in README_VALUES:
        tree.insert(v)
    assert tree.preorder() == before


# ---------- типы значений ----------

def test_negative_numbers_and_zero():
    tree = build_bst([0, -5, 5, -10, -2, 2, 10])
    assert tree.inorder() == [-10, -5, -2, 0, 2, 5, 10]
    assert tree.reverse_inorder() == [10, 5, 2, 0, -2, -5, -10]


def test_falsy_values():
    # ловит баги вида `if not value` и `if not current`
    tree = build_bst([0, -1, 1])
    assert tree.root.value == 0
    assert tree.inorder() == [-1, 0, 1]

    tree = build_bst([0.0, -0.5, 0.5])
    assert tree.root.value == 0.0
    assert tree.inorder() == [-0.5, 0.0, 0.5]

    tree = build_bst(["", "a", "B"])
    assert tree.root.value == ""
    assert tree.inorder() == ["", "B", "a"]


def test_floats():
    tree = build_bst([2.5, 1.5, 3.5, 2.25])
    assert tree.inorder() == [1.5, 2.25, 2.5, 3.5]


def test_strings():
    tree = build_bst(["m", "c", "x", "a", "d"])
    assert tree.inorder() == ["a", "c", "d", "m", "x"]
    assert tree.reverse_inorder() == ["x", "m", "d", "c", "a"]


def test_equal_numbers_of_different_types_are_duplicates():
    tree = build_bst([1, 1.0, True])
    assert len(tree.inorder()) == 1


def test_mixed_incomparable_types_raise_and_tree_stays_valid():
    tree = build_bst([1, 2])
    with pytest.raises(TypeError):
        tree.insert("a")
    assert tree.inorder() == [1, 2]


def test_nan_is_rejected():
    tree = BST()
    with pytest.raises(ValueError):
        tree.insert(float("nan"))
    assert tree.root is None


def test_nan_does_not_break_existing_tree():
    tree = build_bst([5, 3])
    with pytest.raises(ValueError):
        tree.insert(float("nan"))
    tree.insert(7)
    assert tree.inorder() == [3, 5, 7]


def test_none_is_rejected():
    tree = BST()
    with pytest.raises(ValueError):
        tree.insert(None)
    assert tree.root is None


# ---------- вставка ----------

def test_insert_into_empty_tree():
    tree = BST()
    tree.insert(42)
    assert tree.root.value == 42
    assert tree.inorder() == [42]


def test_insert_into_existing_empty_subtrees():
    tree = build_bst([10])
    tree.insert(5)
    tree.insert(15)
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15
    assert tree.inorder() == [5, 10, 15]


def test_insert_into_different_subtrees():
    tree = build_bst([10, 5, 15, 3, 7, 12, 18])
    for v in (6, 8, 11, 13):
        tree.insert(v)
    assert tree.inorder() == [3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 18]
    assert tree.root.left.right.left.value == 6
    assert tree.root.right.left.left.value == 11
    assert_valid_bst(tree)


def test_insert_after_traversal():
    tree = build_bst([2, 1])
    assert tree.inorder() == [1, 2]
    tree.insert(3)
    assert tree.inorder() == [1, 2, 3]


# ---------- свойства обходов ----------

@pytest.mark.parametrize("method", METHODS)
def test_repeated_calls_same_result(method):
    # ловит накопление состояния между вызовами (например, self.result)
    tree = build_bst(README_VALUES)
    first = getattr(tree, method)()
    second = getattr(tree, method)()
    assert first == second


@pytest.mark.parametrize("method", METHODS)
def test_returned_lists_are_independent(method):
    tree = build_bst(README_VALUES)
    first = getattr(tree, method)()
    first.append(999)
    assert 999 not in getattr(tree, method)()


def test_traversals_do_not_modify_tree():
    tree = build_bst(README_VALUES)
    before = tree.preorder()
    for method in METHODS:
        getattr(tree, method)()
    assert tree.preorder() == before
    assert_valid_bst(tree)


@pytest.mark.parametrize("method", METHODS)
def test_each_node_visited_exactly_once(method):
    tree = build_bst([8, 4, 12, 2, 6, 10, 14])
    result = getattr(tree, method)()
    assert sorted(result) == [2, 4, 6, 8, 10, 12, 14]


def test_mirror_identities():
    tree = build_bst(README_VALUES)
    assert tree.reverse_inorder() == tree.inorder()[::-1]
    assert tree.reverse_preorder() == tree.postorder()[::-1]
    assert tree.reverse_postorder() == tree.preorder()[::-1]


# ---------- случайные данные ----------

@pytest.mark.parametrize("seed", range(20))
def test_random_trees(seed):
    rng = random.Random(seed)
    values = [rng.randint(-50, 50) for _ in range(rng.randint(0, 80))]
    tree = build_bst(values)
    expected = sorted(set(values))

    assert tree.inorder() == expected
    assert tree.reverse_inorder() == expected[::-1]
    assert tree.reverse_inorder() == tree.inorder()[::-1]
    assert tree.reverse_preorder() == tree.postorder()[::-1]
    assert tree.reverse_postorder() == tree.preorder()[::-1]
    for method in METHODS:
        assert sorted(getattr(tree, method)()) == expected
    assert_valid_bst(tree)
