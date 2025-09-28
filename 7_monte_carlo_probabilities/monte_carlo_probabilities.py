import random
import matplotlib.pyplot as plt

# Кількість ітерацій (кількість кидків кубиків)
num_simulations = 100000

# Словник для підрахунку кількості випадків кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sum_counts[total] += 1

# Обчислення ймовірностей
monte_carlo_probabilities = {k: v / num_simulations for k, v in sum_counts.items()}

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Виведення результатів
print("Сума\tМонте-Карло ймовірність\tАналітична ймовірність")
for total in range(2, 13):
    mc_prob = monte_carlo_probabilities[total] * 100
    an_prob = analytical_probabilities[total] * 100
    print(f"{total}\t{mc_prob:.2f}%\t\t\t{an_prob:.2f}%")

# Візуалізація
sums = list(range(2, 13))
mc_values = [monte_carlo_probabilities[i] for i in sums]
an_values = [analytical_probabilities[i] for i in sums]

plt.bar(sums, mc_values, width=0.4, label="Монте-Карло", alpha=0.7, align='edge')
plt.bar([x-0.4 for x in sums], an_values, width=0.4, label="Аналітична", alpha=0.7, align='edge')
plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні двох кубиків")
plt.xticks(sums)
plt.legend()
plt.show()
