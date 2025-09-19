import os
import requests
import pandas as pd
import numpy as np

def fetch_sample_data():
    url = "https://api.eia.gov/series/?api_key=YOUR_API_KEY&series_id=EBA.TEX-ALL.D.H"

    try:
        r = requests.get(url).json()
        if "series" in r:
            data = r["series"][0]["data"]
            df = pd.DataFrame(data, columns=["datetime", "demand"])
            df["datetime"] = pd.to_datetime(df["datetime"])
            df = df.sort_values("datetime")
            return df
        else:
            # API call didn’t return expected data
            print(f"⚠️ EIA API error: {r}")
            raise ValueError("API response missing 'series' key")

    except Exception as e:
        print(f"⚠️ Falling back due to error: {e}")

        # Try to load local CSV
        dummy_path = os.path.join(os.path.dirname(__file__), "..", "data", "dummy_demand.csv")
        if os.path.exists(dummy_path):
            df = pd.read_csv(dummy_path, parse_dates=["datetime"])
            return df
        else:
            print("⚠️ Dummy CSV not found. Generating synthetic data...")

            # Generate 48 hours of fake hourly demand data
            dates = pd.date_range(end=pd.Timestamp.now(), periods=48, freq="H")
            demand = np.random.randint(40000, 60000, size=len(dates))
            df = pd.DataFrame({"datetime": dates, "demand": demand})
            return df
