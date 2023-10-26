import pandas as pd

def get_expected_income_for_row(table):
   result = []

   for row in table:
         income = (2400 - 1500) * row[3] - row[4] * 1500
         result.append(income)
   return result


def get_full_income(table, expected_income):
   result = 0

   for i, row in enumerate(table):
        result += row[0] * expected_income[i]
   return result


def_A = pd.read_excel("satpr3.xlsx", sheet_name="8",
                        skiprows=0, nrows=3, usecols="F:J")
def_B = pd.read_excel("satpr3.xlsx", sheet_name="8",
                        skiprows=5, nrows=3, usecols="F:J")
def_C = pd.read_excel("satpr3.xlsx", sheet_name="8",
                        skiprows=10, nrows=3, usecols="F:J")

A = def_A.to_numpy()
B = def_B.to_numpy()
C = def_C.to_numpy()

# print(A)
# print(B)
# print(C)

expected_income_A = get_expected_income_for_row(A)
expected_income_B = get_expected_income_for_row(B)
expected_income_C = get_expected_income_for_row(C)


print("Масив очікуваного чистого доходу для альтернативи A:\n", expected_income_A)
print("Масив очікуваного чистого доходу для альтернативи B:\n", expected_income_B)
print("Масив очікуваного чистого доходу для альтернативи C:\n", expected_income_C)

result_A = get_full_income(A, expected_income_A)
result_B = get_full_income(A, expected_income_B)
result_C = get_full_income(A, expected_income_C)

print("Очікуваний чистий дохід для альтернативи A:\n", result_A)
print("Очікуваний чистий дохід для альтернативи B:\n",result_B)
print("Очікуваний чистий дохід для альтернативи C:\n",result_C)

