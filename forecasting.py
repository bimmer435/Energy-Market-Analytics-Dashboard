import pandas as pd
from prophet import Prophet

def forecast_demand(df):
    df_prophet = df.rename(columns={'datetime': 'ds', 'demand': 'y'})
    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
