import pytest

from stack import Stack
from queue import Queue

#проверяем push&pop
def test_stack_push_and_pop():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

  #проверяем, что последний положенный достанется первым, а первый положенный последним
    assert stack.pop() == 3 
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_stack_peek():
    stack = Stack()

    stack.push(10)
    stack.push(20)

  #проверяем верхний элемент без удаления
    assert stack.peek() == 20
    assert len(stack) == 2

def test_stack_empty():
    stack = Stack()

  #пустой только что созданный стек
    assert stack.is_empty()

    stack.push(1)
    assert not stack.is_empty()

  #забрали единственный элемент, должно стать пусто
    stack.pop()
    assert stack.is_empty()

def test_queue_enqueue_and_dequeue():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

def test_queue_peek():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

  #проверяю, что peek вернет первый элемент(10), а не последний
    assert queue.peek() == 10
    assert len(queue) == 2

def test_queue_empty():
    queue = Queue()

  #только что создали очередь - она пустая
    assert queue.is_empty()

  #после enqueue очередь непустая 
    queue.enqueue(1)
    assert not queue.is_empty()
  
#забрали единственный элемент, теперь снова пусто
    queue.dequeue()
    assert queue.is_empty()

