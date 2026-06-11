"""
Data Ingestion Script

Purpose:
Reads all CSV files from the raw data folder
and displays basic dataset information.

Author: Hemanth Kumar
"""

import pandas as pd
from pathlib import Path

# Location of raw datasets
raw_path = Path("data/raw")

# Read every CSV file
for file in raw_path.glob("*.csv"):

    print("=" * 70)
    print(f"FILE: {file.name}")

    # Load dataset
    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("Columns:", len(df.columns))
    print("Missing Values:")
    print(df.isnull().sum().sum())
    print()