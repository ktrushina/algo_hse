class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def merge_with_dummy(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

def merge_without_dummy(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.data <= list2.data:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return head
