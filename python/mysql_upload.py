import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../data/cleaned_sales_data.csv")

engine = create_engine(
    "mysql+pymysql://root:root@localhost/sales_db"
)

df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data uploaded to MySQL successfully!")
