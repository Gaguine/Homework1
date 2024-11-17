import pandas as pd
# Task 1
def create_companyDF(income,expenses,years) -> pd.DataFrame:
    company_DF = pd.DataFrame({
        "Income":income,
        "Expences":expenses
    },index=years)
    return company_DF

income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]
print(create_companyDF(income,expenses,years))