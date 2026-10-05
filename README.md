# EstatePulse | Real Estate Price Prediction & Marketplace Platform

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI Pipeline](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Tests: Pytest](https://img.shields.io/badge/tests-8%20passed-success.svg)](code/backend/tests)
[![Course](https://img.shields.io/badge/Course-UCS503P%20Software%20Engineering-orange.svg)](project-proposal/Software_Eng_Project.pdf)

> **Course:** UCS503P (Software Engineering) — Thapar Institute of Engineering and Technology  
> **Submitted to:** Ms. Anushka  
> **Authors:** Guntaas Singh (1024030108), Haneesh (1024030112), Atiksh Gupta (102303133), Dhruv Rajput (1024030538)

---

## 📌 Project Overview

**EstatePulse** is a full-stack, responsive web platform designed to eliminate market opacity and reduce coordination friction in property transactions. The application pairs a **Multiple Linear Regression Pricing Engine** with an intuitive **Buyer Barometer**, an in-app **WhatsApp-style negotiation chat**, and an automated **site visit scheduler** instrumented for fast **Time-to-Appointment** measurement.

---

## 🗂️ Repository Directory Structure

```plaintext
Software-Engineering-Project-main/
├── .github/
│   ├── workflows/
│   │   └── ci.yml               # Automated CI test & lint workflow
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md        # Bug tracking template
│   │   └── feature_request.md   # Feature request template
│   └── pull_request_template.md # Standard PR checklist
├── code/
│   ├── backend/
│   │   ├── app.py               # Flask REST API & static server
│   │   ├── database.py          # SQLite schema, seeds, CRUD
│   │   ├── ml_model.py          # Linear Regression, MSE, Buyer Barometer
│   │   └── tests/
│   │       ├── test_api.py      # Endpoints, chat, appointments tests
│   │       └── test_ml_model.py # ML accuracy & Barometer tests
│   └── frontend/
│       ├── index.html           # Modern single-page web app
│       ├── style.css            # Responsive styles & Barometer UI
│       └── app.js               # Frontend controller & API client
├── docs/                        # MkDocs system documentation
│   ├── index.md                 # Project overview
│   ├── architecture.md          # 3-tier architecture & database schema
│   ├── ml-model.md              # Mathematical equations & metrics
│   ├── api-reference.md         # Complete REST API docs
│   └── evaluation-metrics.md    # Time-to-Appointment criteria
├── journals/                    # Team sprint logs
│   ├── sprint-1-proposal-and-setup.md
│   └── sprint-2-prototype-development.md
├── project-proposal/            # Approved course proposal
│   ├── main_s.tex               # Proposal LaTeX source
│   └── Software_Eng_Project.pdf # Compiled proposal PDF
├── project-report-prototype-stage/
│   └── prototype_stage_report.md# Milestone report
├── project-report-final/
│   └── final_report_outline.md  # Final evaluation deliverable roadmap
├── Makefile                     # Build & execution automation
├── mkdocs.yml                   # MkDocs configuration
├── pyproject.toml               # Python project configuration & pytest
├── requirements.txt             # Pip dependencies
├── CONTRIBUTING.md              # Collaboration guidelines
├── LICENSE                      # MIT Open Source License
└── README.md                    # Main repository documentation
```

---

## 🏗️ Architecture

```
+--------------------------------------------------------------+
|                   Client Tier (Frontend SPA)                 |
|       HTML5 / CSS3 / ES6+ JavaScript / Buyer Barometer       |
+------------------------------+-------------------------------+
                               | HTTP REST / JSON
                               v
+--------------------------------------------------------------+
|                     Application & ML Tier                    |
|        Flask 3.x API / Scikit-Learn Linear Regression        |
+------------------------------+-------------------------------+
                               | SQLite3
                               v
+--------------------------------------------------------------+
|                      Persistence Tier                        |
|       Properties / Messages / Appointments / Payments        |
+--------------------------------------------------------------+
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.10+ (Current venv configured with Python 3.14)

### 2. Set Up Environment & Install Dependencies
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Automated Tests
```powershell
.\venv\Scripts\pytest.exe code\backend\tests -v
```

### 4. Start Application
```powershell
.\venv\Scripts\python.exe code\backend\app.py
```
Open **[http://localhost:5000](http://localhost:5000)** in your browser.

---

## 🧪 Evaluation Metrics (UCS503P)

| Metric | Target | Implementation Status |
| :--- | :--- | :--- |
| **Primary: Time-to-Appointment** | Median $\le$ 2.0 hours | Captured via timestamps ($t_0 \to t_1$) on inquiry and confirmed visit. |
| **Prediction Accuracy (MSE)** | Variance within 10% | Multiple Linear Regression with MSE, RMSE, and $R^2$ diagnostics. |
| **Engagement Rate** | Negotiation chat usage | In-app messaging threads on all listings. |
| **Automated Verification** | CI/CD on every push | GitHub Actions test pipeline configured and passing. |

---

## 👥 Team & Contributions

| Member | Roll Number | Primary Focus Areas |
| :--- | :--- | :--- |
| **Guntaas Singh** | 1024030108 | Full-Stack Integration, Buyer Barometer UI, Proposal Drafting |
| **Haneesh** | 1024030112 | Machine Learning Model, Mathematical Evaluation & Regression Engine |
| **Atiksh Gupta** | 102303133 | Negotiation Chat Engine, Database Architecture & API Endpoints |
| **Dhruv Rajput** | 1024030538 | Site Visit Scheduler, CI/CD Pipeline, Automated Test Suite |

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
