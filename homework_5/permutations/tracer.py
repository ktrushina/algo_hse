
def tracer(func):
    """Выводит входы и успешные возвраты рекурсивной функции с отступами"""
    depth = [0]

    def wrapper(*args, **kwargs):
        # Формируем аргументы в порядке их передачи
        arguments = [repr(arg) for arg in args]
        arguments += [f"{name}={value!r}" for name, value in kwargs.items()]

        # Отступ соответствует глубине рекурсии
        indent = "  " * depth[0]
        print(f"{indent}→ {func.__name__}({', '.join(arguments)})")

        depth[0] += 1

        try:
            # Выполняем исходную функцию
            result = func(*args, **kwargs)

            # Выводим результат и возвращаем его
            print(f"{indent}← {func.__name__} = {result!r}")
            return result
        finally:
            # Восстанавливаем глубину даже при ошибке
            depth[0] -= 1

    # Сохраняем имя и документацию функции
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper
