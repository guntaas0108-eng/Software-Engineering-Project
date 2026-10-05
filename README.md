# Real Estate Price Prediction and Marketplace Platform (EstatePulse)

> **Course:** UCS503P (Software Engineering) — Thapar Institute of Engineering and Technology  
> **Submitted to:** Ms. Anushka  
> **Authors:** Guntaas Singh (1024030108), Haneesh (1024030112), Atiksh Gupta (102303133), Dhruv Rajput (1024030538)

---

## 📌 Project Overview

**EstatePulse** is a responsive web-based real estate marketplace system designed to eliminate valuation uncertainty and communication fragmentation in property transactions. The platform integrates:
1. **Property Listing Portal:** Submission with category (Commercial, Residential, Villa, Apartment, Entertainment), locality, and duplicate listing detection.
2. **Multiple Linear Regression Pricing Engine:** Predicts fair market price ($\hat{y} = \beta_0 + \sum \beta_i x_i$) and measures error via Mean Squared Error (MSE).
3. **Buyer Barometer:** Visual indicators and gauges highlighting properties selling below, at, or above estimated market rates.
4. **Integrated Communication:** Direct WhatsApp-like negotiation chat between buyers and sellers.
5. **Time-to-Appointment Tracking:** Evaluates the primary course metric—time from initial inquiry to confirmed site visit (target $\le 2$ hours).
6. **Payment Integration:** Simulated booking deposit / refundable visit token checkout.

---

## 🛠️ Architecture

A 3-tier decoupled architecture:
- **Frontend:** Single-page responsive web app (`HTML5`, `CSS3`, `Vanilla ES6+ JavaScript`).
- **Backend API:** Python `Flask` REST API with CORS support.
- **Machine Learning:** `scikit-learn` regression model evaluating property features and computing MSE, RMSE, MAE, and $R^2$.
- **Database:** `SQLite` with tables for properties, messages, appointments, and transactions.

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.10+ (Current venv configured with Python 3.14)

### 2. Activate Virtual Environment
```powershell
.\venv\Scripts\activate
```

### 3. Run Backend & Web App
```powershell
.\venv\Scripts\python.exe code\backend\app.py
```
Open your browser at: **[http://localhost:5000](http://localhost:5000)**

### 4. Run Automated Test Suite
```powershell
.\venv\Scripts\pytest.exe code\backend\tests -v
```

---

## 🧪 Evaluation Metrics (UCS503P)

| Evaluation Metric | Target / Benchmark | Implementation Status |
| :--- | :--- | :--- |
| **Primary: Time-to-Appointment** | Median $\le$ 2.0 hours | Instrument timestamps from initial chat inquiry to seller confirmation; live analytics dashboard. |
| **Prediction Accuracy (MSE)** | Variance within 10% | Multiple Linear Regression model with continuous validation; displays MSE, MAE, and $R^2$. |
| **Engagement Rate** | Chat negotiation usage | Integrated messaging channels on all property cards. |
| **Automated Testing** | CI-ready verification | Unit test suite covering ML prediction, REST endpoints, chat, and appointments. |
