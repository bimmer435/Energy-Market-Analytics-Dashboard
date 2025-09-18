import pandas as pd
import requests
import os

def fetch_sample_data():
    # First try fetching from EIA API (requires API key)
    url = "https://api.eia.gov/series/?api_key=YOUR_API_KEY&series_id=EBA.TEX-ALL.D.H"
    try:
        r = requests.get(url).json()
        data = r['series'][0]['data']
        df = pd.DataFrame(data, columns=['datetime', 'demand'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.sort_values('datetime')
        return df
    except Exception as e:
        # fallback to bundled dummy dataset
        dummy_path = os.path.join(os.path.dirname(__file__), "..", "data", "dummy_demand.csv")
        df = pd.read_csv(dummy_path, parse_dates=["datetime"])
        return df
