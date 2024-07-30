import pytest
import pandas as pd
import sqlite3
from src.storage import store_data_to_sqlite

@pytest.fixture
def sample_data():
    """Fixture for providing sample data."""
    return pd.DataFrame({
        'name': ['Bulbasaur', 'Ivysaur'],
        'type': ['Grass', 'Grass']
    })

def test_store_data_to_sqlite(sample_data):
    """Test storing data to SQLite."""
    db_path = "test_pokemon_data.db"
    store_data_to_sqlite(sample_data, db_path)
    
    # Verify data stored correctly
    conn = sqlite3.connect(db_path)
    result = pd.read_sql_query("SELECT * FROM pokemon", conn)
    conn.close()

    assert not result.empty
    assert len(result) == len(sample_data)
    assert set(result['name']) == set(sample_data['name'])