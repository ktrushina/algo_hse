from merge_lists import Node, merge_with_dummy, merge_without_dummy

def create_list(values):
    head = None
    current = None

    for value in values:
        new_node = Node(value)

        if head is None:
            head = new_node
        else:
            current.next = new_node

        current = new_node

    return head

def to_list(head):
    result = []

    while head is not None:
        result.append(head.data)
        head = head.next

    return result

def test_merge_with_dummy():
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])

    result = merge_with_dummy(list1, list2)

    assert to_list(result) == [1, 1, 2, 3, 4, 4]

def test_merge_without_dummy():
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])

    result = merge_without_dummy(list1, list2)

    assert to_list(result) == [1, 1, 2, 3, 4, 4]

def test_first_list_empty():
    list1 = None
    list2 = create_list([1, 3, 5])

    assert to_list(merge_with_dummy(list1, list2)) == [1, 3, 5]
    assert to_list(merge_without_dummy(list1, list2)) == [1, 3, 5]

def test_second_list_empty():
    list1 = create_list([1, 2, 4])
    list2 = None

    assert to_list(merge_with_dummy(list1, list2)) == [1, 2, 4]
    assert to_list(merge_without_dummy(list1, list2)) == [1, 2, 4]

def test_both_lists_empty():
    assert merge_with_dummy(None, None) is None
    assert merge_without_dummy(None, None) is None

def test_one_element_lists():
    list1 = create_list([2])
    list2 = create_list([1])

    assert to_list(merge_with_dummy(list1, list2)) == [1, 2]
    assert to_list(merge_without_dummy(list1, list2)) == [1, 2]
