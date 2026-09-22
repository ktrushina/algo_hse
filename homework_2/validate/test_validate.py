from validate import validate

def test_valid_sequence():
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]

    assert validate(pushed, popped) is True

def test_invalid_sequence():
    pushed = [1, 2, 3]
    popped = [3, 1, 2]

    assert validate(pushed, popped) is False

def test_same_order():
    pushed = [1, 2, 3]
    popped = [1, 2, 3]

    assert validate(pushed, popped) is True

def test_reverse_order():
    pushed = [1, 2, 3]
    popped = [3, 2, 1]

    assert validate(pushed, popped) is True

def test_single_element():
    pushed = [1]
    popped = [1]

    assert validate(pushed, popped) is True

def test_different_lengths():
    assert validate([1, 2, 3], [1, 2, 1]) is True
