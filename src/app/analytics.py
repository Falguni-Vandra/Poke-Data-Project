from pyspark.sql import SparkSession
import pandas as pd


class DataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze_data(self) -> None:
        """Perform basic data analysis."""
        self._print_basic_info()
        self._print_type_distribution()
        self._print_name_length_distribution()
        self._print_missing_values()
        self._print_summary_statistics()
        self._run_spark_analytics()

    def _print_basic_info(self) -> None:
        """Print basic information about the DataFrame."""
        print("Basic Information:")
        print(self.df.info())
        print(f"Number of pokemon: {len(self.df)}")

    def _print_type_distribution(self) -> None:
        """Print distribution of Pokémon types."""
        if 'type' in self.df.columns:
            type_counts = self.df['type'].value_counts()
            print("\nPokémon Type Distribution:")
            print(type_counts)

    def _print_name_length_distribution(self) -> None:
        """Print distribution of Pokémon name lengths."""
        if 'name' in self.df.columns:
            self.df['name_length'] = self.df['name'].apply(len)
            length_distribution = (
                self.df['name_length']
                .value_counts()
                .sort_index()
            )
            print("\nPokémon Name Length Distribution:")
            print(length_distribution)

    def _print_missing_values(self) -> None:
        """Print count of missing values in each column."""
        missing_values = self.df.isnull().sum()
        print("\nMissing Values:")
        print(missing_values)

    def _print_summary_statistics(self) -> None:
        """Print summary statistics."""
        if 'name_length' in self.df.columns:
            summary = self.df['name_length'].describe()
            print("\nSummary Statistics for Name Lengths:")
            print(summary)

    def _run_spark_analytics(self) -> None:
        """Perform advanced analytics using Spark."""
        spark = SparkSession.builder.appName('PokemonAnalytics').getOrCreate()
        spark_df = spark.createDataFrame(self.df)
        count = spark_df.count()
        print(f"\nNumber of Pokémon (Spark): {count}")
