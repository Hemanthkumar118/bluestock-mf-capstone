"""
Live NAV Fetch Script

Purpose:
Downloads latest NAV history from MFAPI
and stores it in the raw data folder.

Author: Hemanth Kumar
"""

import requests
import pandas as pd

# Sample mutual fund AMFI codes
codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

# Download NAV data
for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{code}_live_nav.csv",
        index=False
    )

    print(f"{code} downloaded successfully")