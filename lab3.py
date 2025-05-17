def find_initial_arrangement(n):
    if n % 2 != 0:
        raise ValueError("Количество карточек должно быть четным для чередования цветов")
    
    table = []
    for i in range(n, 0, -1):
        if i % 2 == 0:
            table.insert(0, 'B')
        else:
            table.insert(0, 'W')
        

        if len(table) > 1:
            last_card = table.pop()
            table.insert(0, last_card)
    
    return table


n = 8
initial_arrangement = find_initial_arrangement(n)
print("Исходное расположение карточек в стопке:")
print(initial_arrangement)

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
