import sqlite3
import pandas as pd

def store_data_to_sqlite(df: pd.DataFrame, db_path: str) -> None:
    """Stores DataFrame into SQLite database."""
    conn = sqlite3.connect(db_path)
    df.to_sql('pokemon', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_pokemon_data.csv")
    store_data_to_sqlite(df, "pokemon_data.db")