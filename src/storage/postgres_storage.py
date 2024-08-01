from sqlalchemy import create_engine
import pandas as pd


class PostgreSQLStorage:
    def __init__(self, df: pd.DataFrame, db_url: str):
        self.df = df
        self.db_url = db_url

    def storage_data(self) -> None:
        engine = create_engine(self.db_url)
        self.df.to_sql('pokemon', engine, if_exists='replace', index=False)
