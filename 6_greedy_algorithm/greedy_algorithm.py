items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням calories/cost у порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    
    selected = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected.append(name)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected, total_cost, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    # DP таблиця: dp[i][w] = максимальні калорії, використовуючи перші i продуктів з бюджетом w
    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        item = items[names[i-1]]
        for w in range(budget+1):
            if item['cost'] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-item['cost']] + item['calories'])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлюємо вибрані страви
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(names[i-1])
            w -= items[names[i-1]]['cost']

    total_cost = sum(items[name]['cost'] for name in selected)
    total_calories = sum(items[name]['calories'] for name in selected)

    return selected[::-1], total_cost, total_calories  # перевертаємо список для правильного порядку

# Приклад використання
budget = 100

greedy_selection = greedy_algorithm(items, budget)
dp_selection = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print(f"Обрані страви: {greedy_selection[0]}, Вартість: {greedy_selection[1]}, Калорії: {greedy_selection[2]}")

print("\nДинамічне програмування:")
print(f"Обрані страви: {dp_selection[0]}, Вартість: {dp_selection[1]}, Калорії: {dp_selection[2]}")
