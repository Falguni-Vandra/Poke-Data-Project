import sqlite3
import pandas as pd
import pytest
import os
from src.storage import store_data_to_sqlite

@pytest.fixture
def sample_pokemon_data():
    """Fixture for providing sample Pokémon data."""
    return pd.DataFrame({
        'name': ['Bulbasaur', 'Ivysaur'],
        'type': ['Grass', 'Grass']
    })

def test_store_data_to_sqlite(sample_pokemon_data):
    """Test storing Pokémon data to SQLite."""
    test_db_path = "test_pokemon_data.db"

    # Ensure the database file does not exist before the test
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    # Store the sample data
    store_data_to_sqlite(sample_pokemon_data, test_db_path)
    
    # Verify data stored correctly
    conn = sqlite3.connect(test_db_path)
    result_df = pd.read_sql_query("SELECT * FROM pokemon", conn)
    conn.close()

    # Clean up: Remove the test database file
    os.remove(test_db_path)

    # Assertions
    assert not result_df.empty
    assert len(result_df) == len(sample_pokemon_data)
    assert set(result_df['name']) == set(sample_pokemon_data['name'])
    assert set(result_df['type']) == set(sample_pokemon_data['type'])
