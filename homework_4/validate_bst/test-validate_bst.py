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
