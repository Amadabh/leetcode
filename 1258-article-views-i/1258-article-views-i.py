import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(views["author_id"][views["author_id"] == views["viewer_id"]].unique())
    df = df.rename(columns={0:"id"})
    df = df.sort_values(by="id")
    return df