import sys
import os

# Ensure src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import pandas as pd
from storage import store_data_to_sqlite

def test_store_data_to_sqlite():
    test_data = {'name': ['pikachu', 'bulbasaur'], 'url': ['url1', 'url2']}
    df = pd.DataFrame(test_data)
    store_data_to_sqlite(df, 'test_pokemon', 'test_pokemon_data.db')
    
    import sqlite3
    conn = sqlite3.connect('test_pokemon_data.db')
    query = "SELECT * FROM test_pokemon"
    df_db = pd.read_sql(query, conn)
    conn.close()
    
    assert not df_db.empty
    assert list(df_db.columns) == ['name', 'url']
    assert len(df_db) == 2