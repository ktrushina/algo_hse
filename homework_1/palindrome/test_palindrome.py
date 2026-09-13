from palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome(1551) is True


def test_not_palindrome():
    assert is_palindrome(97) is False


def test_single_digit():
    assert is_palindrome(1) is True


def test_two_digit_palindrome():
    assert is_palindrome(77) is True


def test_zero():
    assert is_palindrome(0) is True


def test_long_palindrome():
    assert is_palindrome(123454321) is True


def test_long_not_palindrome():
    assert is_palindrome(12345) is False
