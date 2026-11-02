
from tracer import tracer


def permutations(nums):
    """Возвращает все перестановки элементов списка nums."""
    result = []
    used = [False] * len(nums)

    @tracer
    def backtrack(current):
        # Если выбрали все элементы, сохраняем готовую перестановку.
        if len(current) == len(nums):
            result.append(current.copy())
            return

        # Перебираем элементы исходного списка.
        for i in range(len(nums)):
            if not used[i]:
                # Отмечаем элемент как использованный.
                used[i] = True
                current.append(nums[i])

                # Продолжаем строить перестановку.
                backtrack(current)

                # Отменяем выбор и пробуем следующий элемент.
                current.pop()
                used[i] = False

    backtrack([])
    return result
