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


def kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k должно лежать в диапазоне от 1 до длины списка")
    a = nums.copy()
    # при порядке по возрастанию максимум стоял бы на индексе n − 1,
    # второй по величине — на n − 2, а k-й — на n − k
    target = len(a) - k
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        # опорный — последний элемент текущего диапазона
        pivot = a[hi]
        lt, gt = partition(a, lo, hi, pivot)
        # target — индекс во всём списке. При сужении поиска меняются только границы
        if target < lt:
            hi = lt - 1
        elif target > gt:
            lo = gt + 1
        else:
            # искомая позиция попала в блок равных, значит, ответ — опорное значение
            return pivot
