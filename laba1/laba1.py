class Program:
    def Main(self):
        print("Задача 1.")
        task1 = Task1()
        task1.getTheBestOption()
        print("Задача 2.")
        task2 = Task2()
        task2.getTheBestOption()

class Task1:
    def __init__(self):
        self.matrix = [
            [3, 7, 2, 9],
            [8, 7, 2, 6],
            [4, 8, 3, 5],
            [9, 6, 5, 4]
        ]
        self.weight = [8, 9, 6, 7]

    def getTheBestOption(self):
        number = 0
        resultPrevios = 0
        result = 0
        for i in range(len(self.matrix)):
            result = 0
            for j in range(len(self.matrix[i])):
                result += self.matrix[i][j] * self.weight[j]
            if resultPrevios > result:
                result = resultPrevios
                continue
            resultPrevios = result
            number = i + 1
        print("Найкращий варіант - " + str(number) + ". Максимальна функція корисності = " + str(result))

class Task2:
    def __init__(self):
        self.matrix = [
            [85, 30, 22, 0.65, 6],
            [60, 20, 10, 0.6, 7],
            [30, 12, 5, 0.45, 5],
            [75, 24, 13, 0.7, 8],
            [40, 15, 7, 0.55, 7]
        ]
        self.weight = [7, 5, 6, 8, 6]

    def getTheBestOption(self):
        number = 0
        resultPrevios = 0
        result = 0
        for i in range(len(self.matrix)):
            result = 0
            for k in range(len(self.matrix[i])):
                min_val = float('inf')
                max_val = float('-inf')
                for j in range(len(self.matrix)):
                    if self.matrix[j][k] < min_val:
                        min_val = self.matrix[j][k]
                    if self.matrix[j][k] > max_val:
                        max_val = self.matrix[j][k]
                result += (self.matrix[i][k] - min_val) / (max_val - min_val) * self.weight[k]
            if resultPrevios > result:
                result = resultPrevios
                continue
            resultPrevios = result
            number = i + 1
        print("Найкращий варіант - " + str(number) + ". Максимальна функція корисності = " + str(result))

if __name__ == "__main__":
    program = Program()
    program.Main()
