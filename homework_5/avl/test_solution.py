
import random

import pytest

from solution import AVL


def inorder(node):
    """Возвращает значения дерева в порядке возрастания."""
    if node is None:
        return []

    return (
        inorder(node.left)
        + [node.value]
        + inorder(node.right)
    )


def check_avl(node):
    """Проверяет высоты и баланс всех узлов дерева."""
    if node is None:
        return 0

    left_height = check_avl(node.left)
    right_height = check_avl(node.right)

    assert abs(left_height - right_height) <= 1
    assert node.height == 1 + max(left_height, right_height)

    return node.height


def assert_valid_tree(tree, expected):
    """Проверяет содержимое дерева и свойства AVL."""
    assert inorder(tree.root) == sorted(expected)
    check_avl(tree.root)


def test_empty_tree():
    tree = AVL()

    assert tree.root is None
    assert tree.search(10) is False

    tree.delete(10)
    assert_valid_tree(tree, [])


def test_single_element():
    tree = AVL()

    tree.insert(10)

    assert tree.search(10) is True
    assert tree.search(20) is False
    assert_valid_tree(tree, [10])

    tree.delete(10)

    assert tree.root is None
    assert tree.search(10) is False


@pytest.mark.parametrize(
    "values, expected_root",
    [
        ([30, 20, 10], 20),  # LL
        ([10, 20, 30], 20),  # RR
        ([30, 10, 20], 20),  # LR
        ([10, 30, 20], 20),  # RL
    ],
)
def test_insert_rotations(values, expected_root):
    tree = AVL()

    for value in values:
        tree.insert(value)

    assert tree.root.value == expected_root
    assert_valid_tree(tree, values)


def test_insert_many_sorted_values():
    tree = AVL()

    for value in range(100):
        tree.insert(value)

    assert_valid_tree(tree, range(100))
    assert tree.search(0) is True
    assert tree.search(99) is True
    assert tree.search(100) is False


def test_insert_duplicates():
    tree = AVL()

    for value in [10, 20, 10, 20, 10]:
        tree.insert(value)

    assert_valid_tree(tree, [10, 20])


def test_negative_and_zero_values():
    tree = AVL()

    for value in [-10, 0, 5, -20]:
        tree.insert(value)

    assert_valid_tree(tree, [-20, -10, 0, 5])


def test_delete_leaf():
    tree = AVL()

    for value in [20, 10, 30]:
        tree.insert(value)

    tree.delete(10)

    assert tree.search(10) is False
    assert_valid_tree(tree, [20, 30])


def test_delete_node_with_one_child():
    tree = AVL()

    for value in [20, 10, 30, 25]:
        tree.insert(value)

    tree.delete(30)

    assert tree.search(30) is False
    assert_valid_tree(tree, [10, 20, 25])


def test_delete_node_with_two_children():
    tree = AVL()

    for value in [20, 10, 30, 25, 40]:
        tree.insert(value)

    tree.delete(30)

    assert tree.search(30) is False
    assert_valid_tree(tree, [10, 20, 25, 40])


def test_delete_root():
    tree = AVL()

    for value in [20, 10, 30]:
        tree.insert(value)

    tree.delete(20)

    assert tree.search(20) is False
    assert_valid_tree(tree, [10, 30])


def test_delete_missing_value():
    tree = AVL()

    for value in [10, 20, 30]:
        tree.insert(value)

    tree.delete(999)

    assert_valid_tree(tree, [10, 20, 30])


def test_delete_rebalances_tree():
    tree = AVL()

    for value in [4, 2, 5, 1, 3]:
        tree.insert(value)

    tree.delete(5)

    assert tree.root.value == 2
    assert_valid_tree(tree, [1, 2, 3, 4])


def test_delete_all_elements():
    tree = AVL()
    values = [50, 20, 70, 10, 30, 60, 80]

    for value in values:
        tree.insert(value)

    for value in values:
        tree.delete(value)
        assert_valid_tree(
            tree,
            [x for x in values if tree.search(x)],
        )

    assert tree.root is None


def test_repeated_operations():
    tree = AVL()

    tree.insert(10)
    tree.insert(20)
    tree.delete(10)
    tree.insert(10)
    tree.delete(20)
    tree.delete(20)

    assert_valid_tree(tree, [10])


def test_random_operations():
    rng = random.Random(42)
    tree = AVL()
    expected = set()

    for _ in range(200):
        value = rng.randrange(-50, 51)

        if rng.choice([True, False]):
            tree.insert(value)
            expected.add(value)
        else:
            tree.delete(value)
            expected.discard(value)

        assert_valid_tree(tree, expected)

        for x in range(-50, 51):
            assert tree.search(x) == (x in expected)
