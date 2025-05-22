import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_orders = pd.merge(company[company['name'] == 'RED'], orders, on='com_id', how='inner')
    red_sales_ids = red_orders['sales_id'].unique()

    return sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]