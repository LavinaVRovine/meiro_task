import pandas as pd
from sqlalchemy import JSON, Integer, create_engine


engine = create_engine('postgresql://postgres:postgres@localhost:5436/meiro')


if __name__ == '__main__':

    df: pd.DataFrame = pd.read_json('data/data.ndjson.gz', lines=True)

    pps = df["products"].explode(["products"])
    user_columns = df["user"].apply(lambda x: list(x.keys())).explode().unique()
    product_columns = pps.apply(lambda x: list(x.keys())).explode().unique()
    print(f"These are user columns:{user_columns}")
    print(f"These are product columns: {product_columns}")

    df.to_sql("raw", con=engine, dtype=dict(
        id=Integer, created=Integer, products=JSON, user=JSON
    ), if_exists="replace", index=False)
