# Pokémon Data Project

This project involves fetching, processing, storing, and analyzing Pokémon data.

## Project Structure

- `src/`: Contains source code for data acquisition, processing, storage, and analytics.
- `data/`: Contains raw and cleaned data files.
- `tests/`: Contains unit tests for the project.
- `dist/`: Contains distribution files (e.g., wheel files) for the packaged library.

## Setup

1. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

2. **Build and Package the Library:**

    To build the package and create distribution files, run:

    ```bash
    python setup.py sdist bdist_wheel
    ```

    The wheel and source distribution files will be created in the `dist/` directory.

3. **Fetch and Clean Data:**

    ```bash
    python src/app/data_acquisition.py
    python src/app/data_processing.py
    ```

4. **Store Data:**

    ```bash
    python src/storage/sqlite_storage.py
    ```

5. **Perform Analytics:**

    ```bash
    python src/app/analytics.py
    ```

6. **Run Tests:**

    ```bash
    pytest
    ```

## Requirements

- Python 3.11 or higher
- `requests`
- `pandas`
- `pyspark`
- `pytest`
- `pylint`

## Usage

After installing the package, you can use the Pokémon library as a command-line tool. For example, you can run:

```bash
pokemon-library