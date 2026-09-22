class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data): #добавляем в конец
        new_node = Node(data) #создаем новый узел

        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node #прицепляем новый узел после последнего
            self.last = new_node #сдвигаем last на новый узел

        self.size += 1

    def dequeue(self): #забрать из начала
        if self.first is None:
            raise IndexError("queue is empty")

        data = self.first.data #сохраняем данные из первого узла
        self.first = self.first.next
        self.size -= 1

        if self.first is None: #например, если очередь опустела
            self.last = None

        return data

    def peek(self): #получаем первый элемент, НЕ удаляя
        if self.first is None:
            raise IndexError("queue is empty")

        return self.first.data

    def is_empty(self):
        return self.first is None

    def __len__(self):
        return self.size
