import pandas as pd


class DataProcessor:
    """Processes Pokémon data."""

    def __init__(self, data_frame: pd.DataFrame):
        self.df = data_frame

    def process_data(self) -> pd.DataFrame:
        """Process the DataFrame and return a processed DataFrame."""
        # Example processing
        self.df['name'] = self.df['name'].str.title()
        return self.df

# Need to build more on this script
