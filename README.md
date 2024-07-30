# Pokémon Data Project

This project involves fetching, processing, storing, and analyzing Pokémon data.

## Project Structure

- `src/`: Contains source code for data acquisition, processing, storage, and analytics.
- `data/`: Contains raw and cleaned data files.
- `tests/`: Contains unit tests for the project.

## Setup

1. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Fetch and Clean Data:**

    ```bash
    python src/data_acquisition.py
    python src/data_processing.py
    ```

3. **Store Data:**

    ```bash
    python src/storage.py
    ```

4. **Perform Analytics:**

    ```bash
    python src/analytics.py
    ```

5. **Run Tests:**

    ```bash
    pytest
    ```

## Requirements

- Python 3.x
- `requests`
- `pandas`
- `sqlite3`
- `pyspark`
- `pytest`