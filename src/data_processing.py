"""Cleans the Pokémon data from the CSV file and returns a DataFrame."""

import pandas as pd

def clean_pokemon_data(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    df = df.fillna('Unknown')

    return df

if __name__ == '__main__':
    df_inner = clean_pokemon_data('data/pokemon_data.csv')
    df_inner.to_csv('data/cleaned_pokemon_data.csv', index=False)
