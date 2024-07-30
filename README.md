# Pokemon Data Processing Project

## Overview

This project involves fetching data from the Pokémon API, processing it using Apache Spark on Databricks, and storing it in a XYZ database. The project is structured to work within the Azure free tier, using Databricks for data processing and XYZ for local storage.

## Project Structure

pokemon_project/
├── data/
│ └── (store downloaded data here)
├── notebooks/
│ └── (store Databricks notebooks here)
├── src/
│ ├── init.py
│ ├── data_acquisition.py
│ ├── data_processing.py
│ ├── storage.py
│ └── analytics.py
├── requirements.txt
└── README.md

## Setup

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)
- VSCode (optional, for development)

# Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Dependencies

pip install -r requirements.txt