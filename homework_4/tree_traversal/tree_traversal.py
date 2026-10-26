class Node: #узел
    def __init__(self, value):
        self.value = value #значение которое храним в узле 
        self.left = None #ссылка на левого потомка
        self.right = None #ссылка на  правого потомка


class BST:
    def __init__(self):
        self.root = None #корень дерева; изначально дерево пустое

    def insert(self, value): #если дерево пустое, новый узел становится корнем
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root #начинаем поиск места для нового элемента с корня

        while True:
            #если новое значение меньше текущего, оно должно находиться в левом поддереве
            if value < current.value:
                if current.left is None:
                    #если место свободно, вставляем новый узел
                    current.left = Node(value)
                    return
                #иначе продолжаем поиск в правом поддереве  
                current = current.left

            #если новое значение больше текущего, оно должно находится в правом поддереве
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

            else: 
                #если значение уже есть в дереве, не добавляем дубликат
                return

    #прямой обход: корень -> левое поддерево -> правое поддерево
    def preorder(self):
        result = [] #порядок посещения узлов

        def traverse(node):
            if node is None: #нет узла, значит нечего и обходить
                return

            result.append(node.value) #сначала посещаем текущий узел
            traverse(node.left) #затем обходим левое поддерево
            traverse(node.right) #после этого обходим правое поддерево

        traverse(self.root) #начинаем обход с корня
        return result

    #симметричный обход: левое поддерево -> корень -> правое поддерево
    def inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left) #сначала левое поддерево
            result.append(node.value) #затем текущий узел
            traverse(node.right) #в конце правое поддерево

        traverse(self.root)
        return result

    #обратный обход: левое поддерево -> правое поддерево -> корень
    def postorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left) #сначала левое поддерево
            traverse(node.right) #затем правое поддерево
            result.append(node.value) #текущий узел посещаем последним

        traverse(self.root)
        return result

    #обратный preorder: корень -> правое поддерево -> левое поддерево
    def reverse_preorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            result.append(node.value) #сначала текущий узел
            traverse(node.right) #затем правое поддерево
            traverse(node.left)  #после левое поддерево

        traverse(self.root)
        return result

    #обратный inorder: правое поддерево -> корень -> левое поддерево
    def reverse_inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.right)
            result.append(node.value)
            traverse(node.left)

        traverse(self.root)
        return result

    #обратный postorder: правое поддерево -> левое поддерево -> корень
    def reverse_postorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.right)
            traverse(node.left)
            result.append(node.value)

        traverse(self.root)
        return result
