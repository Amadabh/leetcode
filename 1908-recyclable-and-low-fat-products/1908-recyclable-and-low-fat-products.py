import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    return pd.DataFrame(df["product_id"][(df["low_fats"] == "Y") & (df["recyclable"]=="Y")])
    