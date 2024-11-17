import pandas as pd

def create_companyDF(income, expences, years):
    data = years

    df = pd.DataFrame(data, columns=['','Years'])

    print(df)

years = [2019,2020,2021,2022]
income = [12000,20000,14000,0]
expences = [100,200,300,101]

create_companyDF(income, expences, years)