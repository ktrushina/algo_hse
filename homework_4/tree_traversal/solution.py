class Node:
    """Узел дерева: значение и ссылки на левого и правого потомков"""

    __slots__ = ("value", "left", "right")

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        """Вставляет значение"""
        if value is None or value != value:  # value != value истинно только для NaN
            raise ValueError("None и NaN нельзя хранить в BST")

        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return  # значение уже есть

    def _walk(self, order: str, mirror: bool) -> list[int]:
        """Итеративный обход со стеком пар (узел, раскрыт_ли)

        Пара (узел, False) означает узел ещё не раскрыт»: при извлечении
        он заменяется тремя действиями (N, L, R) в нужном порядке.
        Пара (узел, True) означает посетить узел: значение пишется в result.
        mirror=True меняет местами L и R
        """
        result: list[int] = []
        stack = [(self.root, False)] if self.root is not None else []

        while stack:
            node, expanded = stack.pop()
            if expanded:
                result.append(node.value)
                continue

            first, second = (node.right, node.left) if mirror else (node.left, node.right)
            visit = (node, True)
            if order == "pre":
                actions = [visit, (first, False), (second, False)]
            elif order == "in":
                actions = [(first, False), visit, (second, False)]
            else:  # "post"
                actions = [(first, False), (second, False), visit]

            # Стек LIFO: кладём в обратном порядке, чтобы первым снялось actions[0]
            for item in reversed(actions):
                if item[0] is not None:
                    stack.append(item)

        return result

    def preorder(self) -> list[int]:
        """N → L → R."""
        return self._walk("pre", mirror=False)

    def inorder(self) -> list[int]:
        """L → N → R (по возрастанию)."""
        return self._walk("in", mirror=False)

    def postorder(self) -> list[int]:
        """L → R → N."""
        return self._walk("post", mirror=False)

    def reverse_preorder(self) -> list[int]:
        """N → R → L."""
        return self._walk("pre", mirror=True)

    def reverse_inorder(self) -> list[int]:
        """R → N → L (по убыванию)."""
        return self._walk("in", mirror=True)

    def reverse_postorder(self) -> list[int]:
        """R → L → N."""
        return self._walk("post", mirror=True)
