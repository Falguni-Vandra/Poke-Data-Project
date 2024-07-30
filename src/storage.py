from sqlalchemy import create_engine
import pandas as pd

def create_sqlite_engine(db_file='pokemon_data.db'):
    return create_engine(f'sqlite:///{db_file}')

def store_data_to_sqlite(df, table_name, db_file='pokemon_data.db'):
    engine = create_sqlite_engine(db_file)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def main():
    df = pd.read_csv('data/pokemon_data.csv')
    store_data_to_sqlite(df, 'pokemon')

if __name__ == '__main__':
    main()