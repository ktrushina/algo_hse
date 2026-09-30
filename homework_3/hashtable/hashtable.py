#делала через линейное пробирование

class HashTable:
    """
    Хеш-таблица для хранения пар «ключ–значение»

    Использует открытую адресацию и линейное пробирование
    для разрешения коллизий. При заполнении таблица
    автоматически увеличивается в два раза.

    Parameters
    ----------
    capacity : int, default=8
        Начальный размер хеш-таблицы.

    max_load_factor : float, default=0.7
        Максимально допустимый коэффициент заполнения
        При достижении этого значения таблица расширяется

    Notes
    -----
    Для хранения данных используется только list
    Каждая занятая ячейка содержит пару [key, value]
    """

    # Специальный маркер для ячейки, из которой элемент был удалён.
    # Он нужен, чтобы поиск мог продолжить проход по цепочке
    # после удаления элемента.
    DELETED = object()

    def __init__(self, capacity=8, max_load_factor=0.7):
        """
        Создаёт пустую хеш-таблицу

        Parameters
        ----------
        capacity : int, default=8
            Начальный размер таблицы

        max_load_factor : float, default=0.7
            Коэффициент заполнения, при достижении которого
            таблица автоматически увеличивается

        Raises
        ------
        ValueError
            Если capacity меньше или равен 0 или
            max_load_factor находится вне диапазона (0, 1)
        """
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        if not 0 < max_load_factor < 1:
            raise ValueError("max_load_factor must be between 0 and 1")

        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.size = 0

        # Основное хранилище хеш-таблицы.
        # None означает, что ячейка никогда не использовалась.
        self.table = [None] * capacity

    def _get_index(self, key):
        """
        Вычисляет начальный индекс для ключа.

        Parameters
        ----------
        key : hashable
            Ключ, для которого необходимо найти индекс

        Returns
        -------
        int
            Индекс ячейки в диапазоне от 0 до capacity - 1
        """
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        """
        Добавляет пару «ключ–значение» в таблицу

        Если ключ уже существует, его значение обновляется.
        При возникновении коллизии используется линейное
        пробирование: проверяются следующие ячейки по порядку.

        Если коэффициент заполнения достигает заданного
        максимума, таблица автоматически увеличивается

        Parameters
        ----------
        key : hashable
            Ключ элемента.

        value : object
            Значение, связанное с ключом

        Examples
        --------
        >>> table = HashTable()
        >>> table["apple"] = 10
        >>> table["apple"]
        10

        >>> table["apple"] = 20
        >>> table["apple"]
        20
        """
        # Если таблица заполнена слишком сильно,
        # увеличиваем её перед добавлением нового элемента
        if self.size / self.capacity >= self.max_load_factor:
            self._resize()

        index = self._get_index(key)

        # Проверяем ячейки, начиная с рассчитанного индекса
        for _ in range(self.capacity):
            cell = self.table[index]

            # Ячейка свободна — сохраняем новый элемент
            if cell is None:
                self.table[index] = [key, value]
                self.size += 1
                return

            # Ключ уже существует — обновляем значение
            if cell is not self.DELETED and cell[0] == key:
                cell[1] = value
                return

            # Коллизия: переходим к следующей ячейке
            # % capacity позволяет вернуться в начало таблицы
            index = (index + 1) % self.capacity

        # В нормальной работе это практически недостижимо,
        # поскольку таблица автоматически расширяется
        raise RuntimeError("Hash table is full")

    def __getitem__(self, key):
        """
        Возвращает значение, связанное с ключом

        Поиск начинается с хеш-индекса ключа и при коллизии
        продолжается с помощью линейного пробирования

        Parameters
        ----------
        key : hashable
            Ключ, значение которого необходимо найти

        Returns
        -------
        object
            Значение, связанное с ключом.

        Raises
        ------
        KeyError
            Если ключ отсутствует в таблице

        Examples
        --------
        >>> table = HashTable()
        >>> table["apple"] = 10
        >>> table["apple"]
        10
        """
        index = self._get_index(key)

        for _ in range(self.capacity):
            cell = self.table[index]

            # Если встретили полностью пустую ячейку,
            # ключ не может находиться дальше по цепочке
            if cell is None:
                raise KeyError(key)

            # DELETED пропускаем и продолжаем поиск
            if cell is not self.DELETED and cell[0] == key:
                return cell[1]

            # Переходим к следующей ячейке
            index = (index + 1) % self.capacity

        raise KeyError(key)

    def __delitem__(self, key):
        """
        Удаляет элемент по указанному ключу

        Удалённая ячейка помечается специальным значением
        DELETED вместо None. Это необходимо для сохранения
        корректности поиска элементов, расположенных дальше
        из-за коллизий

        Parameters
        ----------
        key : hashable
            Ключ элемента, который необходимо удалить

        Raises
        ------
        KeyError
            Если ключ отсутствует в таблице

        Examples
        --------
        >>> table = HashTable()
        >>> table["apple"] = 10
        >>> del table["apple"]
        >>> "apple" in table
        False
        """
        index = self._get_index(key)

        for _ in range(self.capacity):
            cell = self.table[index]

            # Пустая ячейка означает, что ключ отсутствует
            if cell is None:
                raise KeyError(key)

            # Найден нужный ключ — помечаем ячейку как удалённую
            if cell is not self.DELETED and cell[0] == key:
                self.table[index] = self.DELETED
                self.size -= 1
                return

            # Продолжаем линейное пробирование
            index = (index + 1) % self.capacity

        raise KeyError(key)

    def __contains__(self, key):
        """
        Проверяет наличие ключа в таблице

        Parameters
        ----------
        key : hashable
            Ключ, наличие которого необходимо проверить

        Returns
        -------
        bool
            True, если ключ существует, иначе False

        Examples
        --------
        >>> table = HashTable()
        >>> table["apple"] = 10
        >>> "apple" in table
        True
        >>> "banana" in table
        False
        """
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __len__(self):
        """
        Возвращает количество элементов в таблице

        Returns
       Количество сохранённых пар «ключ–значение» (int)

        Examples
        --------
        >>> table = HashTable()
        >>> table["apple"] = 10
        >>> len(table)
        1
        """
        return self.size

    def _resize(self):
        """
        Увеличивает размер таблицы в два раза

        После изменения размера старые индексы становятся
        недействительными, поэтому все существующие элементы
        заново хешируются и помещаются в новую таблицу

        Удалённые элементы с маркером DELETED не переносятся
        """
        old_table = self.table

        # Увеличиваем ёмкость таблицы в два раза
        self.capacity *= 2

        # Создаём новое пустое хранилище
        self.table = [None] * self.capacity

        # Сбрасываем количество элементов
        self.size = 0

        # Заново добавляем все существующие элементы
        # При этом для каждого элемента вычисляется новый индекс
        for cell in old_table:
            if cell is not None and cell is not self.DELETED:
                key, value = cell
                self[key] = value
