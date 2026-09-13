def is_palindrome(num):
    orig_num = num
    rev_num = 0

    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10

    return orig_num == rev_num
