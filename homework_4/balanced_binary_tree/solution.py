def is_balanced(root):
    """Возвращает True, если бинарное дерево сбалансировано по высоте."""
    def height(node):
        # None означает высоту 0
        # -1 означает, что поддерево несбалансировано
        if node is None:
            return 0

        # Считаем высоту левого поддерева
        left_height = height(node.left)

        # Если левое поддерево уже несбалансировано, возвращаем -1
        if left_height == -1:
            return -1

        # Считаем высоту правого поддерева
        right_height = height(node.right)

        # Если правое поддерево уже несбалансировано, возвращаем -1
        if right_height == -1:
            return -1

        # Проверяем разницу высот левого и правого поддеревьев
        if abs(left_height - right_height) > 1:
            return -1

        # Возвращаем высоту текущего поддерева
        return 1 + max(left_height, right_height)

    # Если высота равна -1, дерево несбалансировано
    return height(root) != -1
