# Walmart Sales Forecasting Project

This repository contains my approach towards forecasting Walmart weekly sales using a combination of classical machine learning and time series models. The project focuses on improving accuracy measured by Weighted Mean Absolute Error (WMAE).

---

## 🚀 Project Approach and Models Tried

### 1. Random Forest Regression (Baseline ML Model)

- **Goal**: Predict weekly sales using store, department, and various engineered features.
- **Features included**: Store info, department, promotional markdowns, CPI, unemployment, holidays, and time-based features (month, week).
- **Experiment Variations**:
  - Without month column — WMAE: 5494 (poor performance, missing key temporal info)
  - Whole data with month column — WMAE: 2450 (big improvement)
  - Whole data + feature selection — WMAE: 1801 (best RF result, improved by selecting important features)
  - Feature selection but without month — WMAE: 2093 (month column is crucial)

**Insight**: Time-based features such as month significantly improve performance. Feature selection helped reduce noise and improved WMAE.

---

### 2. Time Series Modeling

After the baseline ML models, I explored classical time series methods to capture seasonality and trends more explicitly:

- **ARIMA**:
  - Used for modeling and forecasting sales.
  - Results were irregular and unstable, likely due to complex seasonality and multiple stores/departments.

- **Exponential Smoothing (Holt-Winters)**:
  - Applied additive trend and seasonality.
  - Achieved a significantly better WMAE of approximately **840.68**, outperforming the Random Forest baseline.

---

## 🧠 Key Takeaways

- Traditional ML models like Random Forest provide a strong baseline but struggle to fully capture temporal dependencies without explicit time series features.
- Incorporating seasonality and trend with Holt-Winters Exponential Smoothing drastically improves forecast accuracy.
- ARIMA requires careful parameter tuning and may be less robust for this multi-store, multi-department dataset.
- Feature engineering, including time features and promotions, is crucial for both ML and TS models.

---

## 📈 Future Work

- Experiment with hybrid models combining ML and time series (e.g., using residuals of Holt-Winters as features).
- Try advanced boosting methods like LightGBM or XGBoost with more date-based features.
- Explore deep learning models such as LSTM or Temporal Convolutional Networks.
- Automate hyperparameter tuning and cross-validation for robust evaluation.

---

## 📂 Files and Structure

- `train.csv`, `test.csv`, `stores.csv`, `features.csv`: Dataset files used for modeling.
- Model scripts and notebooks for Random Forest, ARIMA, and Holt-Winters experiments.
- Streamlit app for interactive forecasting using the Holt-Winters model.

---

## 📬 Author

**Abhishek Sharma**  
[GitHub Profile](https://github.com/abhishek1397)

---

Feel free to explore and contribute!  
