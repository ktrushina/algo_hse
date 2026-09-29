def two_sum(arr, k):
        """
    Находит индексы двух элементов массива, сумма которых равна k

    Args:
        arr: список целых чисел
        k: искомая сумма двух элементов

    Returns:
        Кортеж из двух индексов найденных элементов
    """
    seen = {}

    for i, num in enumerate(arr):
        needed = k - num

        if needed in seen:
            return seen[needed], i

        seen[num] = i

