
import pytest

from tree_traversal import BST


def build_bst(values):
    """Создаёт bst из списка значений"""
    tree = BST()
    for value in values:
        tree.insert(value)
    return tree


# пустое дерево
def test_empty_tree():
    tree = BST()

    assert tree.root is None

    assert tree.preorder() == []
    assert tree.inorder() == []
    assert tree.postorder() == []
    assert tree.reverse_preorder() == []
    assert tree.reverse_inorder() == []
    assert tree.reverse_postorder() == []


# дерево из одного элемента
def test_single_node():
    tree = build_bst([5])

    expected = [5]

    assert tree.preorder() == expected
    assert tree.inorder() == expected
    assert tree.postorder() == expected
    assert tree.reverse_preorder() == expected
    assert tree.reverse_inorder() == expected
    assert tree.reverse_postorder() == expected


# все шесть обходов обычного дерева
def test_all_traversals():
    tree = build_bst([8, 4, 12, 2, 6, 10, 14])

    assert tree.preorder() == [8, 4, 2, 6, 12, 10, 14]
    assert tree.inorder() == [2, 4, 6, 8, 10, 12, 14]
    assert tree.postorder() == [2, 6, 4, 10, 14, 12, 8]

    assert tree.reverse_preorder() == [8, 12, 14, 10, 4, 6, 2]
    assert tree.reverse_inorder() == [14, 12, 10, 8, 6, 4, 2]
    assert tree.reverse_postorder() == [14, 10, 12, 6, 2, 4, 8]


# все элементы вставляются в возрастающем порядке
# получается дерево только с правыми потомками
def test_right_skewed_tree():
    tree = build_bst([1, 2, 3, 4, 5])

    assert tree.preorder() == [1, 2, 3, 4, 5]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [5, 4, 3, 2, 1]

    assert tree.reverse_preorder() == [1, 2, 3, 4, 5]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_postorder() == [5, 4, 3, 2, 1]


# все элементы вставляются в убывающем порядке
# получается дерево только с левыми потомками
def test_left_skewed_tree():
    tree = build_bst([5, 4, 3, 2, 1])

    assert tree.preorder() == [5, 4, 3, 2, 1]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [1, 2, 3, 4, 5]

    assert tree.reverse_preorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_postorder() == [1, 2, 3, 4, 5]


#повторная вставка существующего значения
def test_duplicate_values():
    tree = build_bst([5, 3, 7, 3, 5, 7])

    assert tree.inorder() == [3, 5, 7]
    assert len(tree.inorder()) == 3


#отрицательные числа и ноль
def test_negative_numbers_and_zero():
    tree = build_bst([0, -5, 5, -10, -2, 2, 10])

    assert tree.inorder() == [-10, -5, -2, 0, 2, 5, 10]
    assert tree.reverse_inorder() == [10, 5, 2, 0, -2, -5, -10]


#вставка в разные поддеревья
def test_insert_into_different_subtrees():
    tree = build_bst([10, 5, 15, 3, 7, 12, 18])

    tree.insert(6)
    tree.insert(8)
    tree.insert(11)
    tree.insert(13)

    assert tree.inorder() == [3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 18]

    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15
    assert tree.root.left.right.left.value == 6
    assert tree.root.right.left.left.value == 11


# вставка в уже существующее пустое поддерево
def test_insert_into_empty_subtree():
    tree = build_bst([10])

    tree.insert(5)
    tree.insert(15)

    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

    assert tree.inorder() == [5, 10, 15]


# вставка в пустое дерево
def test_insert_into_empty_tree():
    tree = BST()
    tree.insert(42)

    assert tree.root is not None
    assert tree.root.value == 42
    assert tree.inorder() == [42]


# большое дерево с несбалансированной структурой
def test_large_skewed_tree():
    values = list(range(1, 51))
    tree = build_bst(values)

    assert tree.inorder() == values
    assert tree.reverse_inorder() == values[::-1]
    assert tree.preorder() == values
    assert tree.reverse_preorder() == values

    #при последовательной вставке дерево — цепочка
    assert tree.postorder() == values[::-1]
    assert tree.reverse_postorder() == values[::-1]


# проверка, что обходы не изменяют дерево
def test_traversals_do_not_modify_tree():
    tree = build_bst([8, 4, 12, 2, 6, 10, 14])

    before = tree.inorder()

    tree.preorder()
    tree.postorder()
    tree.reverse_preorder()
    tree.reverse_inorder()
    tree.reverse_postorder()

    assert tree.inorder() == before


# каждый узел посещается ровно один раз
def test_each_node_visited_once():
    tree = build_bst([8, 4, 12, 2, 6, 10, 14])
    expected_values = [2, 4, 6, 8, 10, 12, 14]

    methods = [
        tree.preorder,
        tree.inorder,
        tree.postorder,
        tree.reverse_preorder,
        tree.reverse_inorder,
        tree.reverse_postorder,
    ]

    for method in methods:
        result = method()
        assert len(result) == len(expected_values)
        assert sorted(result) == expected_values
