# ⚡ Energy Market Analytics Dashboard

An interactive dashboard built with Streamlit to visualize and forecast electricity demand using public energy market data (ERCOT/EIA).  
This project demonstrates **data engineering, forecasting, and deployment skills** end-to-end.

---

## 📸 Screenshots
*(Add your own screenshots after running the app locally or from the deployed version)*

Example:
![Dashboard Screenshot](docs/screenshot.png)

---

## ✨ Features
- Fetches energy demand data from EIA API (ERCOT) or uses a **dummy dataset** included in the repo
- Interactive **time-series visualizations** with Plotly
- **24-hour forecasting** using Facebook Prophet
- Ready-to-deploy on **Streamlit Cloud** or **Heroku**

---

## 🗂 Project Structure
```
energy-dashboard/
│
├── app/
│   ├── dashboard.py       # Streamlit app UI
│   ├── etl.py             # data ingestion logic
│   ├── forecasting.py     # forecasting models
│
├── data/
│   └── dummy_demand.csv   # bundled ERCOT-style sample dataset
│
├── requirements.txt       # dependencies
└── README.md              # project overview
```

---

## ⚡ Quickstart (Run Locally)

1. Clone the repo and install dependencies:
```bash
git clone https://github.com/YOUR_USERNAME/energy-dashboard.git
cd energy-dashboard
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app/dashboard.py
```

3. Open in your browser:  
`http://localhost:8501`

---

## 🌐 Deployment

### Option 1: Streamlit Cloud (easiest)
- Push this repo to GitHub
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Connect your repo and set the **entry point** to: `app/dashboard.py`

### Option 2: Heroku
- Add a `Procfile` with:
  ```
  web: streamlit run app/dashboard.py --server.port=$PORT
  ```
- Push to Heroku

---

## 📌 Notes
- Replace `YOUR_API_KEY` in `app/etl.py` with your EIA API key for live ERCOT data.  
- Dummy dataset ensures the app runs even without an API key.

---
