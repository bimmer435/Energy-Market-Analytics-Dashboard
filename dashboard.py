import streamlit as st
import plotly.express as px
from etl import fetch_sample_data
from forecasting import forecast_demand

st.set_page_config(page_title="Energy Market Dashboard", layout="wide")

st.title("⚡ Energy Market Analytics Dashboard")

# Load data
df = fetch_sample_data()
st.subheader("Raw Demand Data")
st.dataframe(df.tail(10))

# Plot historical demand
fig = px.line(df, x="datetime", y="demand", title="Hourly Demand")
st.plotly_chart(fig, use_container_width=True)

# Forecast
forecast = forecast_demand(df)
fig2 = px.line(forecast, x="ds", y="yhat", title="24h Forecasted Demand")
fig2.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Lower Bound')
fig2.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Upper Bound')
st.plotly_chart(fig2, use_container_width=True)
