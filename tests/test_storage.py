"""Unit tests for the SQLite storage functionality."""

import os
import sqlite3
import pandas as pd
import pytest
from src.storage.sqlite_storage import SQLiteStorage


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

    # Use the sample_data parameter from the fixture
    sample_data = sample_pokemon_data.copy()

    # Create an instance of SQLiteStorage and store the sample data
    sqlite_storage = SQLiteStorage(sample_data, test_db_path)
    sqlite_storage.store_data()

    # Verify data stored correctly
    conn = sqlite3.connect(test_db_path)
    result_df = pd.read_sql_query("SELECT * FROM pokemon", conn)
    conn.close()

    # Clean up: Remove the test database file
    os.remove(test_db_path)

    # Assertions
    assert not result_df.empty
    assert len(result_df) == len(sample_data)
    assert set(result_df['name']) == set(sample_data['name'])
    assert set(result_df['type']) == set(sample_data['type'])
