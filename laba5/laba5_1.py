import numpy as np

payoff_matrix = np.array([[3, 7, 1, 3], [4, 8, 0, -6], [6, -9, -2, 4]])


minA = np.min(payoff_matrix, axis=1)
maxMinA = np.max(minA)


maxB = np.max(payoff_matrix, axis=0)
minMaxB = np.min(maxB)

print(f"Нижня ціна: {maxMinA}")
print(f"Верхня ціна: {minMaxB}")


pure_strategy_equilibrium = np.any(maxMinA == minMaxB)

if pure_strategy_equilibrium:
    print("Рівновага в чистих стратегіях існує.")
else:
    print("Рівновага в чистих стратегіях відсутня.")
