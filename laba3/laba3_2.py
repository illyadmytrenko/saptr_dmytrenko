import pandas as pd

def get_expected_income_for_row(table, range):
   result = []

   for row in table:
         fine = 1000 * (row[0] - range) * 10
         if(fine < 0): fine = 0

         allowance = 500 * (range - row[0]) * 10
         if(allowance < 0): allowance = 0

         income = allowance - fine;
         result.append(income)
   return result


def get_full_income(table, expected_income):
   result = 0

   for i, row in enumerate(table):
        result += row[1] * expected_income[i]
   return result


def_A = pd.read_excel("satpr3.xlsx", sheet_name="10",
                        skiprows=0, nrows=4, usecols="E:H")
def_B = pd.read_excel("satpr3.xlsx", sheet_name="10",
                        skiprows=6, nrows=4, usecols="E:H")
def_C = pd.read_excel("satpr3.xlsx", sheet_name="10",
                        skiprows=12, nrows=4, usecols="E:H")

range_A = 0.8;
range_B = 1.2;
range_C = 1.4;

A = def_A.to_numpy()
B = def_B.to_numpy()
C = def_C.to_numpy()

# print(A)
# print(B)
# print(C)

expected_income_A = get_expected_income_for_row(A, range_A)
expected_income_B = get_expected_income_for_row(B, range_B)
expected_income_C = get_expected_income_for_row(C, range_C)


print("Масив очікуваного чистого доходу для альтернативи A:\n", expected_income_A)
print("Масив очікуваного чистого доходу для альтернативи B:\n", expected_income_B)
print("Масив очікуваного чистого доходу для альтернативи C:\n", expected_income_C)

result_A = get_full_income(A, expected_income_A)
result_B = get_full_income(A, expected_income_B)
result_C = get_full_income(A, expected_income_C)

print("Очікуваний чистий дохід для альтернативи A:\n", result_A)
print("Очікуваний чистий дохід для альтернативи B:\n",result_B)
print("Очікуваний чистий дохід для альтернативи C:\n",result_C)

