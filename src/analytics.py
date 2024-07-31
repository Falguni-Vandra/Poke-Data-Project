"""Load data from SQLite and perform basic analytics."""

from pyspark.sql import SparkSession

def perform_analytics():
    # Start Spark session
    spark = SparkSession.builder.appName('PokemonAnalytics').getOrCreate()

    # Load data into Spark DataFrame
    df = spark.read.format('jdbc').options(
        url = "jdbc:sqlite:pokemon_data.db",
        driver="org.sqlite.JDBC",
        dbtable="pokemon"
    ).load()

    # Perform analytics (e.g., count number of Pokémon)
    count = df.count()
    print(f'Number of Pokemon: {count}')

if __name__ == '__main__':
    perform_analytics()

# more analytics
# change storage mongoDB & postgres
# parellel process data
# create nested folder for each file
# build classes & objects
# setup file
# build poke Lib and package it in wheel file
