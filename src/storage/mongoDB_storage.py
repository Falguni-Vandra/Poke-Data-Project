from pymongo import MongoClient
import pandas as pd


class MongoDBStorage:
    def __init__(self, df: pd.DataFrame, db_name: str, collection_name: str):
        self.df = df
        self.db_name = db_name
        self.collection_name = collection_name

    def storage_data(self) -> None:
        client = MongoClient()
        db = client(self.db_name)
        collection = db(self.collection_name)
        collection.drop()
        data_dict = self.df.to_dict('records')
        collection.insert_many(data_dict)
