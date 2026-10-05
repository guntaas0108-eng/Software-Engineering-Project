# UCS503P Prototype Stage Report: EstatePulse

**Project Title:** Real Estate Price Prediction and Marketplace Platform  
**Authors:** Guntaas Singh, Haneesh, Atiksh Gupta, Dhruv Rajput  
**Submitted to:** Ms. Anushka, Thapar Institute of Engineering and Technology  

---

## 1. Executive Summary
This report presents the prototype stage implementation of **EstatePulse**, a web-based marketplace that addresses transparency and coordination delays in real estate transactions. All core deliverables outlined in the first iteration have been developed, tested, and integrated.

---

## 2. Implemented Prototype Architecture

### 2.1 Backend & Machine Learning Tier
- Framework: Python Flask REST API.
- Model: Multiple Linear Regression ($R^2 > 0.90$, low MSE) trained on physical property dimensions and locality attributes.
- Database: SQLite database storing listings, conversational threads, appointments, and payments.

### 2.2 Client-Side Interface
- Responsive Single-Page Application (SPA).
- **Buyer Barometer:** Visual indicators classifying listings into *Great Deal*, *Fair Market*, or *Premium*.
- **Integrated Chat:** WhatsApp-like negotiation interface.

### 2.3 Evaluation Instrumentation
- **Time-to-Appointment:** Fully instrumented via `first_inquiry_timestamp` and `confirmed_timestamp`.
- Real-time diagnostics dashboard tracking median time, MSE, and engagement rates.

---

## 3. Verification & Test Results
- Automated unit tests: 8/8 passed.
- Continuous Integration: GitHub Actions configured for multi-version verification.

---

## 4. Next Iteration Roadmap
- Live WebSocket push notifications for chat messages.
- Advanced property duplicate image hash matching.
- Expansion of training dataset with regional real estate registry benchmarks.
