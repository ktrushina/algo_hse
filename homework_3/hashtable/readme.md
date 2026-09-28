# общая логика
                    HashTable
                        │
                        ↓
              ┌─────────────────┐
              │ list: table     │
              └────────┬────────┘
                       │
                       ↓
              hash(key) % capacity
                       │
                       ↓
                  нужный index
                       │
              ┌────────┴────────┐
              ↓                 ↓
          свободно            занято
              │                 │
              ↓                 ↓
       [key, value]       index + 1
                                │
                                ↓
                         снова проверяем
                                │
                                ↓
                         linear probing



size / capacity >= 0.7. -> resize()-> capacity × 2 -> новая пустая list -> rehash всех элементов       
       
