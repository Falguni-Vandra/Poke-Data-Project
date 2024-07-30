import requests
import pandas as pd

def fetch_pokemon_data(api_url: str) -> pd.DataFrame:
    """Fetches Pokémon data from the provided API URL and returns a DataFrame."""
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    
    # Extract relevant fields
    pokemon_list = data.get('results', [])
    df = pd.DataFrame(pokemon_list)
    
    return df

if __name__ == "__main__":
    API_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"
    df = fetch_pokemon_data(API_URL)
    df.to_csv("data/pokemon_data.csv", index=False)