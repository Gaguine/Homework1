import pandas as pd
import os

from pandas.core.interchange.dataframe_protocol import DataFrame


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


# Task 2
script_dir = os.path.dirname(__file__)
melb_data = pd.read_csv(f'{script_dir}/pandas_data.csv', sep=',')

print(f"Цена объекта под индексом 15 :{melb_data['Price'][16]}")
print(f"Объект под индексом 90 был продан в: {melb_data['Date'][91]}")


# Task 3
no_toilet = melb_data[melb_data['Bathroom']==0]
Nelson_3_mil = melb_data[(melb_data['SellerG'] == "Nelson") & (melb_data["Price"]>3000000.0)]

print(f"У {len(no_toilet)} объектов недвижимости отсутствуют ванные комнаты.")
print(f" Риелтор Nelson продал {len(Nelson_3_mil)} объектов недвижимости. ")


# Task 4
def delete_columns(df:DataFrame,col:list):
    for key in col:
        if key in df:
            df = df.drop(key, axis=1)
        else:
            return None
    return df

df = melb_data
col = ['Suburb',"Address"]
print(delete_columns(df,col))