def max_even_sum(num):
    total = sum(num)

    if total % 2 == 0:
        return total

    min_odd_num = min(number for number in num if number % 2 != 0)

    return total - min_odd_num
