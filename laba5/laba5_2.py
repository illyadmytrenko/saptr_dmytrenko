import numpy as np

payoff_matrix = np.array([[20, 10], [10, 30]])

probability = 0.5

expected_payoff = payoff_matrix * probability

optimal_strategy = np.argmax(expected_payoff, axis=1)

print("Матриця платежів:")
print(payoff_matrix)
print("\nОчікуваний прибуток фермера:")
print(expected_payoff)
print(
    "\nОптимальна стратегія фермера (кількість акрів у відсотках під культурами I та II):"
)
print(optimal_strategy)
