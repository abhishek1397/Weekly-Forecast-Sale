import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Sales Forecasting App", page_icon="📈", layout="centered")

# --- Load Model and Last Known Value ---
@st.cache_resource
def load_model_and_last_value():
    model = joblib.load('holt_winters_model.pkl')
    last_known_value = joblib.load('last_actual_value.pkl')
    return model, last_known_value

model, last_actual_value = load_model_and_last_value()

# --- App Title ---
st.title("📈 Sales Forecast App")
st.markdown("Predict future weekly sales using time series model.")

# --- User Inputs ---
st.subheader("🛠️ Configure Forecast")
start_date = st.date_input("Start forecast from:", datetime.today())
n_weeks = st.slider("Number of weeks to forecast:", min_value=1, max_value=52, value=12)

# --- Forecast Button ---
if st.button("🔮 Generate Forecast"):
    try:
        # Step 1: Forecast the DIFFERENCES
        forecast_diff = model.forecast(n_weeks)

        # Step 2: Convert to ACTUAL SALES
        forecast_sales = forecast_diff.cumsum() + last_actual_value

        # Step 3: Create weekly date range
        forecast_dates = pd.date_range(start=start_date, periods=n_weeks, freq='W')
        forecast_df = pd.DataFrame({
            'Week Starting': forecast_dates,
            'Predicted Sales': forecast_sales
        }).set_index('Week Starting')

        # Step 4: Show Result
        st.success("✅ Forecast generated successfully!")
        st.dataframe(forecast_df.style.format("{:,.2f}"))

        # Optional: Download as CSV
        csv = forecast_df.to_csv().encode('utf-8')
        st.download_button(
            label="📥 Download Forecast as CSV",
            data=csv,
            file_name='weekly_sales_forecast.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"⚠️ An error occurred during forecasting: {str(e)}")

# --- Footer ---
st.markdown("---")
st.caption("Made by Abhishek Sharma | © 2025 Sales AI")
st.markdown("🔗 View Source Code on [GitHub](https://github.com/abhishek1397)")
