
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root):
    def validate(node, low, high):
        if node is None:
            return True

        #значение должно строго находиться между границами
        if not low < node.value < high:
            return False

        #проверяем левое и правое поддеревья
        return (
            validate(node.left, low, node.value)
            and validate(node.right, node.value, high)
        )

    return validate(root, float('-inf'), float('inf'))
