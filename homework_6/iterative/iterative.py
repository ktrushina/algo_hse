def merge(left, right):
    """ cлить два отсортированных списка """
    result = []
    # i и j указывают на первые ещё не взятые числа в левой и правой половинах
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # одна половина закончилась. Остаток другой уже отсортирован
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort_iterative(nums):
    a = nums.copy()
    # width — длина уже отсортированного блока. Начинаем с одиночных элементов
    width = 1
    while width < len(a):
        # за один шаг сливаем два соседних блока, поэтому шаг равен 2 * width
        for start in range(0, len(a), 2 * width):
            mid = start + width
            end = start + 2 * width
            a[start:end] = merge(a[start:mid], a[mid:end])
        # после слияния пар на следующем проходе можно брать блоки вдвое длиннее
        width *= 2
    return a


def partition(a, lo, hi, pivot):
    """ разбить включительный диапазон и вернуть границы блока равных """
    # i проверяет очередное число. Слева от lt уже лежат числа меньше опорного,
    # справа от gt — больше. От i до gt включительно числа ещё нужно проверить
    lt = i = lo
    gt = hi
    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
            # пришедшее справа значение ещё нужно проверить
        else:
            i += 1
    # теперь все числа от lt до gt включительно равны опорному
    return lt, gt


def quicksort_iterative(nums):
    a = nums.copy()
    # в стеке храним границы участков, которые ещё предстоит отсортировать
    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        lt, gt = partition(a, lo, hi, a[hi])
        # блок равных уже на своём месте. Осталось обработать участки по бокам
        left = (lo, lt - 1)
        right = (gt + 1, hi)
        # стек LIFO: положим большую часть первой, чтобы меньшую взять сразу
        if lt - lo < hi - gt:
            stack.extend((right, left))
        else:
            stack.extend((left, right))
    return a
