
class Node:
    """Узел AVL-дерева."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    """AVL-дерево с операциями вставки, удаления и поиска."""

    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node is not None else 0

    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right),
        )

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        # Правый поворот вокруг node.
        new_root = node.left
        middle = new_root.right

        new_root.right = node
        node.left = middle

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rotate_left(self, node):
        # Левый поворот вокруг node.
        new_root = node.right
        middle = new_root.left

        new_root.left = node
        node.right = middle

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rebalance(self, node):
        # Обновляем высоту после изменения поддерева.
        self._update_height(node)
        balance = self._balance_factor(node)

        # Левое поддерево слишком высокое.
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Правое поддерево слишком высокое.
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, value):
        """Вставляет значение, игнорируя дубликаты."""

        def _insert(node, value):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            else:
                return node

            return self._rebalance(node)

        self.root = _insert(self.root, value)

    def delete(self, value):
        """Удаляет значение, если оно есть в дереве."""

        def _min_node(node):
            while node.left is not None:
                node = node.left
            return node

        def _delete(node, value):
            if node is None:
                return None

            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # Узел без детей или с одним ребёнком.
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                # Два ребёнка: заменяем следующим по величине.
                successor = _min_node(node.right)
                node.value = successor.value
                node.right = _delete(node.right, successor.value)

            return self._rebalance(node)

        self.root = _delete(self.root, value)

    def search(self, value):
        """Проверяет наличие значения в дереве."""
        node = self.root

        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right

        return False
