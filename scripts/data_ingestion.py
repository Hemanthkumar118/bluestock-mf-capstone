import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

for file in raw_path.glob("*.csv"):
    print("="*70)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("Columns:", len(df.columns))
    print("Missing Values:")
    print(df.isnull().sum().sum())

    print()