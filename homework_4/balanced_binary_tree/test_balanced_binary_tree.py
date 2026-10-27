
import pytest
from solution import Node, is_balanced

#покрываю тестами баланс по высоте, не св-ва bst (это покрывали в др заданиях)

def test_empty_tree():
    """Пустое дерево считается сбалансированным"""
    assert is_balanced(None) is True


def test_single_node():
    """Дерево из одного узла"""
    root = Node(10)
    assert is_balanced(root) is True


def test_two_children():
    """У корня есть два листа"""
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    assert is_balanced(root) is True


def test_balanced_complete_tree():
    """Полное сбалансированное дерево"""
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    assert is_balanced(root) is True


def test_left_subtree_taller_by_one():
    """Разница высот у корня равна одному"""
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.right = Node(15)

    assert is_balanced(root) is True


def test_right_subtree_taller_by_one():
    """Симметричный случай: правая сторона выше на один"""
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.right = Node(20)

    assert is_balanced(root) is True


def test_unbalanced_at_root():
    """Дисбаланс непосредственно у корня"""
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    root.right = Node(15)

    assert is_balanced(root) is False


def test_unbalanced_deep_in_left_subtree():
    """Корень сбалансирован по высотам, но левое поддерево — нет."""
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)

    root.right = Node(20)
    root.right.left = Node(15)
    root.right.left.left = Node(12)
    root.right.right = Node(25)

    assert is_balanced(root) is False


def test_unbalanced_deep_in_right_subtree():
    """Проверяем нарушение глубоко в правом поддереве"""
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    root.right.right = Node(20)
    root.right.right.right = Node(25)

    assert is_balanced(root) is False


def test_left_skewed_tree():
    """Все узлы, кроме последнего, имеют только левого ребёнка"""
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.left.left = Node(2)

    assert is_balanced(root) is False


def test_right_skewed_tree():
    """Все узлы образуют цепочку вправо"""
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)

    assert is_balanced(root) is False


def test_balanced_tree_with_negative_values():
    """Значения узлов не влияют на баланс"""
    root = Node(0)
    root.left = Node(-10)
    root.right = Node(10)
    root.left.left = Node(-20)
    root.right.right = Node(20)

    assert is_balanced(root) is True


def test_unbalanced_subtree_with_other_branch():
    """Одна сбалансированная ветка не компенсирует дисбаланс в другой"""
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)

    root.left.left = Node(5)
    root.left.left.left = Node(2)

    root.right.right = Node(40)

    assert is_balanced(root) is False


def test_tree_balanced_at_root_but_not_inside():
    """Проверяем, что недостаточно оценить только корень"""
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)

    root.left.left = Node(3)
    root.left.left.left = Node(1)

    root.right.right = Node(25)

    assert is_balanced(root) is False


def test_unbalanced_by_more_than_two_levels():
    """Большая разница высот"""
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(2)
    root.left.left.left.left = Node(1)
    root.right = Node(15)

    assert is_balanced(root) is False

def test_balanced_tree_that_is_not_bst():
    """Баланс зависит от структуры, а не от порядка значений."""
    root = Node(10)
    root.left = Node(100)
    root.right = Node(-100)
    root.left.left = Node(200)

    assert is_balanced(root) is True
