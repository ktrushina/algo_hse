class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None #вершина стека, указывает на посл доб эл-т
        self.size = 0 #количество элементов

    def push(self, data): #положить элемент
        new_node = Node(data) #создаем новый узел
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self): #достаем элемент
        if self.top is None:
            raise IndexError("stack is empty")

        data = self.top.data #берем значение из вершины
        self.top = self.top.next #сдвигаем вершину вниз
        self.size -= 1
        return data

    def peek(self): #в отличие от pop НЕ удаляем
        if self.top is None:
            raise IndexError("stack is empty")

        return self.top.data

    def is_empty(self): #пуст ли стек
        return self.top is None

    def __len__(self):
        return self.size
