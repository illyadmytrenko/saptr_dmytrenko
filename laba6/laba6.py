import itertools
import numpy as np

distances = np.array(
    [[68, 72, 75, 83], [56, 60, 58, 63], [38, 40, 35, 45], [47, 42, 40, 45]]
)


bases = [0, 1, 2, 3]
consumers = [0, 1, 2, 3]


all_permutations = list(itertools.permutations(consumers))
alternates = []
min_total_distance = float("inf")


for perm in all_permutations:
    current_distance = 0

    for base, consumer in zip(bases, perm):
        current_distance += distances[base][consumer]

    if current_distance == min_total_distance:
        alternates.append(perm)

    if current_distance < min_total_distance:
        min_total_distance = current_distance
        alternates.clear()
        alternates.append(perm)


print("Мінімальна загальна дальність транспортування:", min_total_distance)
print("Оптимальні розподіли замовлень за базами збуту:")
for alternate in alternates:
    for base in alternate:
        base += 1
        print(base, end=" ")
    print()
