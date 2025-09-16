import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer
    return pd.DataFrame(df["name"][(df["referee_id"]!=2) | (df["referee_id"].isnull())])