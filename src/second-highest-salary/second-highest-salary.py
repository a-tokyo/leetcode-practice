import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    top2 = employee["salary"].drop_duplicates().nlargest(2)
    second = top2.iloc[1] if len(top2) == 2 else None
    return pd.DataFrame({"SecondHighestSalary": [second]})