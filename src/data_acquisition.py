import requests
import pandas as pd

def fetch_pokemon_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_data_to_csv(data, filename):
    df = pd.json_normalize(data)
    df.to_csv(filename, index=False)

def main():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100'
    data = fetch_pokemon_data(url)
    save_data_to_csv(data['results'], 'data/pokemon_data.csv')

if __name__ == '__main__':
    main()