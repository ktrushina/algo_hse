
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root):
    stack = [(root, float('-inf'), float('inf'))]  #(узел, нижняя граница, верхняя граница)

    while stack:
        node, low, high = stack.pop()

        if node is None:
            continue

        #значение должно строго находиться между границами
        if not low < node.value < high:
            return False

        #добавляем в стек правое и левое поддеревья
        #левое кладём последним, чтобы оно проверялось первым
        stack.append((node.right, node.value, high))
        stack.append((node.left, low, node.value))

    return True
