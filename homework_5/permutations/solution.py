
from tracer import tracer


def permutations(nums):
    """Возвращает все перестановки элементов списка."""
    result = []
    used = [False] * len(nums)

    @tracer
    def backtrack(current):
        # Если выбраны все элементы, сохраняем перестановку.
        if len(current) == len(nums):
            result.append(current.copy())
            return

        # Перебираем элементы исходного списка.
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True

                # Добавляем элемент в текущую перестановку.
                current.append(nums[i])

                # Передаём копию, чтобы трассировка показывала
                # состояние на момент рекурсивного вызова.
                backtrack(current.copy())

                # Отменяем выбор и пробуем другой элемент.
                current.pop()
                used[i] = False

    backtrack([])
    return result
