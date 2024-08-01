"""Fetches Pokémon data from the provided API URL and returns a DataFrame."""

import requests
import pandas as pd


class PokemonDataFetcher:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_data(self) -> pd.DataFrame:
        response = requests.get(self.api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract relevant fields
        pokemon_list = data.get('results', [])
        df = pd.DataFrame(pokemon_list)

        return df
