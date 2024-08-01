from src.app.analytics import DataAnalyzer
from src.app.data_acquisition import PokemonDataFetcher
from src.app.data_processing import DataProcessor
from src.storage.mongoDB_storage import MongoDBStorage
from src.storage.postgres_storage import PostgreSQLStorage
from src.storage.sqlite_storage import SQLiteStorage
from concurrent.futures import ThreadPoolExecutor


def main():
    # Configuration
    API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    SQLITE_DB_PATH = "pokemon_data.db"
    MONGO_DB_NAME = "pokemon_db"
    MONGO_COLLECTION_NAME = "pokemon"
    POSTGRES_DB_URL = "postgresql://user:password@localhost:5432/pokemon_db"

    # Step 1: Fetch Data
    fetcher = PokemonDataFetcher(API_URL)
    df = fetcher.fetch_data()

    # Step 2: Process Data
    processor = DataProcessor(df)
    processed_df = processor.process_data()

    # Step 3: Store Data in SQLite, MongoDB, and PostgreSQL
    sqlite_storage = SQLiteStorage(processed_df, SQLITE_DB_PATH)
    mongo_storage = MongoDBStorage(
        processed_df,
        MONGO_DB_NAME,
        MONGO_COLLECTION_NAME
    )
    postgres_storage = PostgreSQLStorage(processed_df, POSTGRES_DB_URL)

    # Use ThreadPoolExecutor to run the storage tasks in parallel
    with ThreadPoolExecutor() as executor:
        executor.submit(sqlite_storage.store_data)
        executor.submit(mongo_storage.store_data)
        executor.submit(postgres_storage.store_data)

    # Step 4: Analyze Data
    analyzer = DataAnalyzer(processed_df)
    analyzer.analyze_data()


if __name__ == "__main__":
    main()
