import pytest
from solution import Node, is_valid_bst

def test_empty_tree():
    assert is_valid_bst(None) is True


def test_single_node():
    assert is_valid_bst(Node(5)) is True


def test_valid_bst():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    assert is_valid_bst(root) is True


def test_invalid_deep_node():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(12)

    assert is_valid_bst(root) is False


def test_invalid_right_subtree():
    root = Node(10)
    root.right = Node(15)
    root.right.left = Node(8)

    assert is_valid_bst(root) is False


def test_duplicate_values(): #предполагаю что дубликаты запрещены (как в моей реализации BST.insert())
    root = Node(10)
    root.left = Node(10)

    assert is_valid_bst(root) is False



# нарушение глубоко в левом поддереве
def test_invalid_deep_left_subtree():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.right = Node(12)

    # 12 находится в левом поддереве 10, поэтому это ошибка
    assert is_valid_bst(root) is False


# нарушение глубоко в правом поддереве
def test_invalid_deep_right_subtree():
    root = Node(10)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.left.left = Node(8)

    # 8 меньше 10, но находится в правом поддереве 10
    assert is_valid_bst(root) is False


# сложное, но корректное BST
def test_valid_complex_bst():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)

    root.left.left = Node(5)
    root.left.right = Node(15)
    root.left.right.left = Node(12)
    root.left.right.right = Node(17)

    root.right.left = Node(25)
    root.right.right = Node(40)
    root.right.left.left = Node(22)
    root.right.left.right = Node(27)

    assert is_valid_bst(root) is True


# дубликат не у непосредственного потомка
def test_duplicate_deep_in_subtree():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(8)
    root.left.right.right = Node(10)

    assert is_valid_bst(root) is False


# отрицательные числа и ноль
def test_valid_negative_numbers():
    root = Node(0)
    root.left = Node(-10)
    root.right = Node(10)
    root.left.left = Node(-20)
    root.left.right = Node(-5)
    root.right.left = Node(5)
    root.right.right = Node(20)

    assert is_valid_bst(root) is True


# отрицательное значение нарушает границу предка
def test_invalid_negative_value():
    root = Node(-10)
    root.right = Node(0)
    root.right.left = Node(-15)

    # -15 находится в правом поддереве -10,
    # хотя должно быть больше -10
    assert is_valid_bst(root) is False


# очень большие целые числа
def test_very_large_integers():
    a = 10**100
    b = 10**200
    c = 10**300

    root = Node(b)
    root.left = Node(a)
    root.right = Node(c)

    assert is_valid_bst(root) is True


# несбалансированное корректное дерево
def test_valid_skewed_tree():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    root.right.right.right.right = Node(5)

    assert is_valid_bst(root) is True


# корень допустим, но левое поддерево нарушает
# ограничение более высокого предка
def test_ancestor_constraint_violation():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)

    root.left.right = Node(40)
    root.left.right.right = Node(45)
    root.left.right.right.right = Node(55)

    # 55 больше 50, но находится в левом поддереве 50
    assert is_valid_bst(root) is False
