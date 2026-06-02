import requests
import pandas as pd

codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in codes:

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{code}_live_nav.csv",
        index=False
    )

    print(f"{code} downloaded")