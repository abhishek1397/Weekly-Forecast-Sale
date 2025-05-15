# 🧮 Walmart Sales Forecasting Web App using Holt-Winters

Forecast weekly sales using the Holt-Winters Exponential Smoothing model. This app allows users to interactively input forecasting parameters and view realistic, non-differenced sales predictions.

📍 **Live Demo**: [https://yourdomain.com](https://yourdomain.com)  
📁 **GitHub Profile**: [@abhishek1397](https://github.com/abhishek1397)

---

## 🚀 Features

- ✅ Realistic **sales prediction** (auto inverse-transformed from differenced data)
- 📅 **Date input** and custom forecast horizon
- 📦 Dockerized for **easy deployment**
- 🖥️ Streamlit-powered interactive web UI
- 🌍 Supports **custom domain** with **free SSL (Let's Encrypt)**
- 📈 Future-ready for deployment on **AWS EC2** with **Route 53** and **NGINX**

---

## 📸 Screenshots

> _Add screenshots here after running the app locally_

| Input Panel                        | Forecast Output                         |
|-----------------------------------|-----------------------------------------|
| ![Input](screenshots/input.png)   | ![Output](screenshots/output.png)       |

---

## 📂 Project Structure

```bash
.
├── app.py                      # Streamlit application
├── Dockerfile                  # Docker config
├── holt_winters_model.pkl      # Trained Holt-Winters model
├── last_actual_value.pkl       # Last known actual sales value (used for inverse diff)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
