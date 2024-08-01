"""Stores DataFrame into SQLite database."""

import sqlite3
import pandas as pd


class SQLiteStorage:
    """Handles storage of DataFrame into SQLite database."""

    def __init__(self, df: pd.DataFrame, db_path: str):
        self.df = df
        self.db_path = db_path

    def store_data(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self.df.to_sql('pokemon', conn, if_exists='replace', index=False)
