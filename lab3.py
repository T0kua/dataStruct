from collections import deque

def build_initial_stack(n):
    table = deque(['W' if i % 2 == 0 else 'B' for i in range(n)])
    stack = []
    
    while table:
        if stack:
            last_card = stack.pop()
            stack.insert(0, last_card)
        stack.insert(0, table.pop())
    
    return stack

# Проверка
n = int(input(">>"))
initial_stack = build_initial_stack(n)
print("Исходная стопка:", initial_stack)

def simulate_layout(stack):
    table = []
    temp_stack = deque(stack.copy())
    while temp_stack:
        table.append(temp_stack.popleft())
        if temp_stack:
            temp_stack.append(temp_stack.popleft())
    return table

layout = simulate_layout(initial_stack)
print("Раскладка на столе:", layout)
print("Чередование цветов:", all(layout[i] != layout[i+1] for i in range(len(layout)-1)))
