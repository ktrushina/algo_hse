from timeit import default_timer


def merge(left, right):
    """ cлить два отсортированных списка """
    result = []
    # i и j указывают на первые ещё не взятые числа в левой и правой половинках
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


def mergesort_recursive(nums):
    # пустой список и список из одного элемента уже отсортированы
    if len(nums) < 2:
        return nums.copy()
    mid = len(nums) // 2
    # сначала сортируем каждую половину отдельно, затем сливаем их
    left = mergesort_recursive(nums[:mid])
    right = mergesort_recursive(nums[mid:])
    return merge(left, right)


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


def quicksort_recursive(nums):
    a = nums.copy()

    def sort(lo, hi):
        while lo < hi:
            lt, gt = partition(a, lo, hi, a[hi])
            # меньшая часть уходит в рекурсию, большая остаётся в цикле
            # сравниваем длины частей. Новый вызов получит не больше половины элементов
            if lt - lo < hi - gt:
                sort(lo, lt - 1)
                lo = gt + 1
            else:
                sort(gt + 1, hi)
                hi = lt - 1

    sort(0, len(a) - 1)
    return a


def timed(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        return result, default_timer() - start
    return wrapper


if __name__ == "__main__":
    cases = {
        "По возрастанию": list(range(2500)),
        "Все равны": [7] * 2500,
    }
    methods = [timed(mergesort_recursive), timed(quicksort_recursive)]
    for name, nums in cases.items():
        expected = sorted(nums)
        samples = [[], []]
        for run in range(7):
            # чередуем порядок запуска двух сортировок в соседних повторах
            for i in ((0, 1) if run % 2 == 0 else (1, 0)):
                result, seconds = methods[i](nums)
                assert result == expected
                samples[i].append(seconds * 1000)
        # среднее по всем запускам каждого метода, в миллисекундах
        merge_ms, quick_ms = [sum(times) / len(times) for times in samples]
        print(f"{name} | {merge_ms:.3f} | {quick_ms:.3f}")
