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


def test_left_child_greater_than_parent():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(12)

    assert is_valid_bst(root) is False


def test_invalid_right_subtree():
    root = Node(10)
    root.right = Node(15)
    root.right.left = Node(8)

    assert is_valid_bst(root) is False


def test_duplicate_values(): #дубликаты запрещены: значения должны быть строго больше/меньше предков
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

def build_chain(values, side):
    """Цепочка узлов: каждый следующий узел — потомок предыдущего с указанной стороны"""
    root = Node(values[0])
    current = root
    for value in values[1:]:
        child = Node(value)
        setattr(current, side, child)
        current = child
    return root


# схема из README
def test_readme_scheme_valid():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)

    assert is_valid_bst(root) is True


# пошаговый пример из README
def test_readme_step_by_step_example():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.left.right.right = Node(22)

    # 22 больше корня 20, но находится в его левом поддереве
    assert is_valid_bst(root) is False


# то же дерево с корректным значением вместо 22
def test_readme_step_by_step_example_fixed():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.left.right.right = Node(17)

    assert is_valid_bst(root) is True


# дубликат в правом поддереве (равен нижней границе)
def test_duplicate_in_right_subtree():
    root = Node(10)
    root.right = Node(10)

    assert is_valid_bst(root) is False


# дубликат предка в правом поддереве не у непосредственного потомка
def test_duplicate_of_ancestor_in_right_subtree():
    root = Node(10)
    root.right = Node(15)
    root.right.left = Node(10)

    assert is_valid_bst(root) is False


# правый потомок меньше родителя
def test_right_child_less_than_parent():
    root = Node(10)
    root.right = Node(5)

    assert is_valid_bst(root) is False


# корректное дерево, растущее только влево
def test_valid_left_skewed_tree():
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.left.left = Node(2)
    root.left.left.left.left = Node(1)

    assert is_valid_bst(root) is True


# ноль как граница
def test_zero_as_boundary():
    root = Node(0)
    root.left = Node(-10)
    root.left.right = Node(5)  # 5 находится в левом поддереве 0

    assert is_valid_bst(root) is False

    root = Node(0)
    root.right = Node(10)
    root.right.left = Node(-5)  # -5 находится в правом поддереве 0

    assert is_valid_bst(root) is False


# глубина больше лимита рекурсии Python (около 1000)
def test_deep_right_chain_valid():
    root = build_chain(list(range(1, 5001)), "right")

    assert is_valid_bst(root) is True


def test_deep_left_chain_valid():
    root = build_chain(list(range(5000, 0, -1)), "left")

    assert is_valid_bst(root) is True


# нарушение границы предка в самом низу глубокой цепочки
def test_deep_chain_ancestor_violation_at_bottom():
    root = build_chain(list(range(5000, 1, -1)), "left")  # 5000, 4999, ..., 2

    bottom = root
    while bottom.left is not None:
        bottom = bottom.left

    # 4000 больше 2, но находится в левом поддереве 3
    bottom.right = Node(4000)

    assert is_valid_bst(root) is False


def test_invalid_deep_right_subtree_exceeds_ancestor():
    root = Node(10)
    root.right = Node(15)
    root.right.right = Node(20)
    root.right.right.left = Node(9)

    assert is_valid_bst(root) is False

def test_invalid_deep_left_subtree_below_ancestor():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.left.right = Node(7)

    assert is_valid_bst(root) is False
