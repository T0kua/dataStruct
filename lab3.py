def find_initial_arrangement(n):
    """
    Функция определяет исходное расположение карточек в стопке,
    чтобы при раскладывании они чередовались по цвету.
    
    Аргументы:
    n -- общее количество карточек (четное)
    
    Возвращает:
    Список, представляющий исходную стопку карточек,
    где 'W' - белая, 'B' - черная.
    """
    if n % 2 != 0:
        raise ValueError("Количество карточек должно быть четным для чередования цветов")
    
    # Имитируем процесс раскладывания в обратном порядке
    table = []
    for i in range(n, 0, -1):
        if i % 2 == 0:  # Четные позиции - черные (B)
            table.insert(0, 'B')
        else:            # Нечетные позиции - белые (W)
            table.insert(0, 'W')
        
        # Перемещаем последнюю карточку в начало (обратное действие)
        if len(table) > 1:
            last_card = table.pop()
            table.insert(0, last_card)
    
    return table

# Пример использования
n = 8  # Количество карточек (должно быть четным)
initial_arrangement = find_initial_arrangement(n)
print("Исходное расположение карточек в стопке:")
print(initial_arrangement)

# Проверка
def simulate_layout(arrangement):
    stack = arrangement.copy()
    table = []
    while stack:
        table.append(stack.pop(0))
        if stack:
            stack.append(stack.pop(0))
    return table

print("\nПроверка раскладывания:")
result = simulate_layout(initial_arrangement)
print(result)