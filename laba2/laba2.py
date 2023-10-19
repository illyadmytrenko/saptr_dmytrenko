matrixExpertOne = [[1, 3, 3, 5, 7, 5, 3, 5], [0.333, 1, 2, 4, 5, 3, 2, 3], [0.333, 0.5, 1, 4, 5, 3, 2, 3],
                  [0.2, 0.25, 0.25, 1, 3, 2, 1, 2], [0.142, 0.2, 0.2, 0.333, 1, 0.5, 0.333, 0.5],
                  [0.2, 0.333, 0.333, 0.5, 2, 1, 0.333, 1], [0.333, 0.5, 0.5, 1, 3, 3, 1, 3],
                  [0.2, 0.333, 0.333, 0.5, 2, 1, 0.333, 1]]

matrixExpertTwo = [[1, 2, 2, 4, 5, 1, 7, 5], [0.5, 1, 1, 3, 3, 1, 4, 3], [0.5, 1, 1, 3, 4, 0.5, 2, 4],
                  [0.25, 0.333, 0.333, 1, 2, 0.333, 1, 2], [0.2, 0.333, 0.25, 0.5, 1, 0.25, 0.333, 1],
                  [1, 1, 2, 3, 4, 1, 6, 8], [0.142, 0.25, 0.5, 1, 3, 0.166, 1, 1], [0.2, 0.333, 0.25, 0.5, 1, 0.125, 1, 1]]

print("Матриця оцінок критеріїв експертів:")
print("1 Експерт:")
for i in range(len(matrixExpertOne)):
   print(matrixExpertOne[i])
   
print("2 Експерт:")
for i in range(len(matrixExpertTwo)):
   print(matrixExpertTwo[i])


def getWeight(matrix: list): 
   sum = 0;
   arrayWi = []
   arrayWnorm = []
   for i in range(len(matrix)):
      temp = 1;
      for j in range(len(matrix[i])):
         temp *= matrix[i][j]
      Wi = temp ** (1./len(matrix))
      arrayWi.append(Wi);
      sum += Wi
   matrix.append(arrayWi)
   for i in range(len(arrayWi)):
      arrayWnorm.append(arrayWi[i]/sum)
   matrix.append(arrayWnorm)


getWeight(matrixExpertOne)
getWeight(matrixExpertTwo)

print("Пріорітетність критеріїв 1 експерту у вигляді масиву:\n", matrixExpertOne[len(matrixExpertOne) - 1])
print("Пріорітетність критеріїв 2 експерту у вигляді масиву:\n", matrixExpertTwo[len(matrixExpertTwo) - 1])

arrayMo = []
for i in range(len(matrixExpertOne[len(matrixExpertOne) - 1])):
   arrayMo.append((matrixExpertOne[len(matrixExpertOne) - 1][i] * matrixExpertTwo[len(matrixExpertOne) - 1][i]) ** (1./2))
print("Середнє значення пріорітетності критеріїв у вигляді масиву:\n", arrayMo)


matrixAlternativesExpertOne = [[[1, 5, 3], [0.2, 1, 0.333], [0.333, 3, 1]], [[1, 5, 3], [0.2, 1, 0.333], [0.333, 3, 1]],
                              [[1, 1, 2], [1, 1, 2], [0.5, 0.5, 1]], [[1, 2, 0.2], [0.5, 1, 0.142], [5, 7, 1]],
                              [[1, 0.5, 4], [2, 1, 8], [0.25, 0.125, 1]], [[1, 0.5, 4], [2, 1, 7], [0.25, 0.142, 1]],
                              [[1, 0.333, 3], [3, 1, 9], [0.333, 0.111, 1]], [[1, 0.5, 4], [2, 1, 7], [0.25, 0.142, 1]]]

print("Матриця оцінок альтернатив 1 експерту:")
for i in range(len(matrixAlternativesExpertOne)):
   print(matrixAlternativesExpertOne[i])

matrixAlternativesExpertTwo = [[[1, 7, 5], [0.142, 1, 0.5], [0.2, 2, 1]], [[1, 3, 0.333], [0.333, 1, 0.333], [3, 3, 1]],
                              [[1, 0.5, 2], [2, 1, 4], [0.5, 0.25, 1]], [[1, 1, 0.2], [1, 1, 0.2], [5, 5, 1]],
                              [[1, 0.333, 1], [3, 1, 8], [1, 0.125, 1]], [[1, 0.5, 6], [2, 1, 9], [0.166, 0.111, 1]], 
                              [[1, 0.333, 5], [3, 1, 9], [0.2, 0.111, 1]], [[1, 0.5, 4], [2, 1, 7], [0.25, 0.142, 1]]]

print("Матриця оцінок альтернатив 2 експерту:")
for i in range(len(matrixAlternativesExpertTwo)):
   print(matrixAlternativesExpertTwo[i])

for i in range(len(matrixAlternativesExpertOne)):
   getWeight(matrixAlternativesExpertOne[i])

print("Пріорітетність альтернатив 1 експерту у вигляді матриці:")
for i in range(len(matrixAlternativesExpertOne)):
   print(matrixAlternativesExpertOne[i][len(matrixAlternativesExpertOne[i]) - 1])

for i in range(len(matrixAlternativesExpertTwo)):
   getWeight(matrixAlternativesExpertTwo[i])
   
print("Пріорітетність альтернатив 2 експерту у вигляді матриці:")
for i in range(len(matrixAlternativesExpertTwo)):
   print(matrixAlternativesExpertTwo[i][len(matrixAlternativesExpertTwo[i]) - 1])


matrixMaxAlternatives = []
for i in range(len(matrixAlternativesExpertOne[0][len(matrixAlternativesExpertOne[i]) - 1])):
   temp = []
   for j in range(len(matrixAlternativesExpertOne)):
      if (matrixAlternativesExpertOne[j][len(matrixAlternativesExpertOne[j]) - 1][i] > matrixAlternativesExpertTwo[j][len(matrixAlternativesExpertTwo[j]) - 1][i]):
         maxAlternative = matrixAlternativesExpertOne[j][len(matrixAlternativesExpertOne[j]) - 1][i]
      else:
         maxAlternative = matrixAlternativesExpertTwo[j][len(matrixAlternativesExpertTwo[j]) - 1][i]
      temp.append(maxAlternative)
   matrixMaxAlternatives.append(temp)

print("Матриця максимальних пріорітетів альтернатив:")
for i in range(len(matrixMaxAlternatives)):
   print(matrixMaxAlternatives[i])


resultPrevios = 0
for i in range(len(matrixMaxAlternatives)):
   result = 0
   for j in range(len(matrixAlternativesExpertOne)):
      result += matrixMaxAlternatives[i][j] * arrayMo[j]
   print("Варіант ", i + 1, " - ", result)
   if resultPrevios > result:
      result = resultPrevios
      continue
   resultPrevios = result
   number = i + 1
print(
   "Найкращий варіант - ",
   str(number),
   ". Глобальний пріорітет альтернатив = ",
   str(result),
)