# EstatePulse | AI-Powered Real Estate Marketplace & Valuation Platform
### *(Academically Cataloged as PropertyPulse — Course UCS 503 / UCS503P)*

[![CI Pipeline](https://img.shields.io/badge/CI-Passing-brightgreen.svg?style=flat-square&logo=githubactions)](.github/workflows/ci.yml)
[![Tests: Pytest](https://img.shields.io/badge/Tests-8%20Passed-success.svg?style=flat-square&logo=pytest)](code/backend/tests)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask%203.x-lightgrey.svg?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![ML Engine: Scikit--Learn](https://img.shields.io/badge/ML-Scikit--Learn%20Regression-orange.svg?style=flat-square&logo=scikitlearn)](https://scikit-learn.org/)
[![Database: SQLite](https://img.shields.io/badge/Database-SQLite3-003B57.svg?style=flat-square&logo=sqlite)](https://sqlite.org/)
[![Institution: TIET](https://img.shields.io/badge/Institution-Thapar%20Institute%20of%20Engineering%20%26%20Technology-red.svg?style=flat-square)](https://www.thapar.edu/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## 🏛️ Academic Course Context

| Parameter | Academic Record |
| :--- | :--- |
| **Course Code & Title:** | **UCS 503 / UCS503P — Software Engineering** |
| **Academic Department:** | Computer Science and Engineering Department |
| **Institution:** | Thapar Institute of Engineering and Technology, Patiala, Punjab |
| **Course Instructor / Evaluator:** | **Ms. Anushka** |
| **Academic Class / Group:** | **3C14**, BE Third Year, Computer Engineering (COE) |
| **Evaluation Milestone:** | Software Requirements Specification (SRS) & Milestone Review |
| **Document Release:** | **Version 1.0 (October 2026)** |

---

## 👥 Project Team & Responsibilities

| Member Name | University Roll No. | Primary Software Engineering Focus |
| :--- | :--- | :--- |
| **Guntaas Singh** | `1024030108` | Full-Stack Integration, Buyer Barometer UI, Proposal Drafting |
| **Haneesh** | `1024030112` | Machine Learning Model, Mathematical Evaluation & Regression Engine |
| **Dhruv Rajput** | `1024030538` | Database Architecture, Backend CRUD, Appointment Scheduling Engine |
| **Atiksh Gupta** | `102303133` | In-App Negotiation Chat, System Integration, Automated CI/CD Testing |

---

## 📋 Comprehensive Project Documentation

The repository maintains full software engineering artifacts compliant with IEEE/course requirements:

- 📕 [**Official Software Requirements Specification (SRS.pdf)**](SRS.pdf) *(or view in [docs/SRS.pdf](docs/SRS.pdf))*: Complete 17-page compiled academic document with cover page, Table of Contents, and high-resolution UML diagrams matching TIET course requirements.
- 📑 [**Software Requirements Specification (Markdown)**](SRS.md) *(or view in [docs/SRS.md](docs/SRS.md))*: Formal specification covering scope, user classes, functional & non-functional requirements, UML diagrams (Use Case, Class, Activity, Sequence), and mathematical models.
- 📜 [**Formal LaTeX SRS Source (docs/SRS.tex)**](docs/SRS.tex): Publication-grade LaTeX source ready for formal PDF compilation.
- 📑 [**Approved Course Proposal (PDF)**](project-proposal/Software_Eng_Project.pdf) & [**LaTeX Source**](project-proposal/main_s.tex): Approved problem statement and time-to-value heuristics.
- 📑 [**Prototype Stage Milestone Report**](project-report-prototype-stage/prototype_stage_report.md): Execution summary of core deliverables and verification benchmarks.
- 📑 [**System Architecture & Schema**](docs/architecture.md): 3-tier architectural breakdown and relational database specifications.
- 📑 [**REST API Documentation**](docs/api-reference.md): Endpoints, JSON payloads, response formats, and error handling.
- 📑 [**Machine Learning Formulation**](docs/ml-model.md): Multiple Linear Regression derivations, residual metrics, and synthetic seed datasets.
- 📑 [**Evaluation & Performance Metrics**](docs/evaluation-metrics.md): Time-to-Appointment attribution and measurement criteria.
- 📘 [**Team Engineering Journals**](journals/README.md): Individual student development logs for Sprints 1 through 4 (Weeks 1 to 5).

---

## 📌 Executive Summary & Problem Statement

In the modern real estate marketplace, transactions are plagued by three systemic failures:
1. **Opaque Pricing & Information Asymmetry:** Buyers lack objective, data-backed benchmarks to determine whether asking prices reflect authentic market valuation.
2. **Spam & Duplicate Listings:** Unverified broker networks spam platforms with repetitive entries, degrading database integrity.
3. **Fragmented Communication Channels:** Property inquiries often shift to phone calls, paper notes, or external messaging apps, causing lost context and scheduling delays.

### The EstatePulse Solution
**EstatePulse** introduces an integrated, engineering-centric web application combining:
- **Instant ML Valuation:** Multivariate regression computes a fair market valuation ($\hat{y}$) in $< 100\text{ms}$ upon property specification.
- **Buyer Barometer:** Visual classification (*Great Deal*, *Fair Market Price*, *Premium*) derived from statistical deviation between asking and model prices.
- **Automated Duplicate Detection:** Pre-submission text and dimensional matching alerts sellers to potential duplicates.
- **Contextual In-App Chat:** Dedicated WhatsApp-style conversational thread per property.
- **Site Visit Scheduling & Token Escrow:** Direct appointment booking with nominal token fee handling.
- **Empirical Metric Instrumentation:** Directly measures the primary academic metric: **Time-to-Appointment** ($T_{\text{appt}} = t_{\text{confirmed}} - t_{\text{inquiry}} \le 2$ hours target).

---

## 🏗️ 3-Tier System Architecture

EstatePulse employs a decoupled 3-tier architecture ensuring maintainability, portability, and low operational overhead:

```
+-------------------------------------------------------------------------+
|                       PRESENTATION TIER (Client SPA)                    |
|  - Semantic HTML5 / Responsive CSS3 (Mobile & Desktop Viewports)       |
|  - Vanilla ES6+ Asynchronous REST API Client                            |
|  - High-Contrast Real Estate Theme & Buyer Barometer Visualizer         |
+------------------------------------+------------------------------------+
                                     | HTTP / JSON REST APIs
                                     v
+-------------------------------------------------------------------------+
|                     APPLICATION & ML TIER (Python Flask)                |
|  - Flask 3.x WSGI Controller & Cross-Origin Resource Sharing (CORS)     |
|  - Scikit-Learn Multiple Linear Regression Engine (y_hat, MSE, R2)      |
|  - Duplicate Listing Detector & Appointment State Machine Engine        |
|  - Role-Based Access Controller (Buyer / Seller / Guest Browsing)       |
+------------------------------------+------------------------------------+
                                     | Parameterized SQL Queries
                                     v
+-------------------------------------------------------------------------+
|                       PERSISTENCE TIER (SQLite 3)                       |
|  - Normalized Tables: users, properties, messages, appointments, payments|
|  - Zero-Configuration Transactional Relational Storage (real_estate.db) |
+-------------------------------------------------------------------------+
```

---

## 📊 Mathematical Formulation & Metrics

### 1. Multiple Linear Regression Pricing Model
The baseline fair price ($\hat{y}$) is estimated using continuous physical features and one-hot encoded categorical parameters:
$$\hat{y} = \beta_0 + \sum_{i=1}^{n} \beta_i x_i + \epsilon$$

Where:
- $\hat{y}$ = Estimated fair valuation in INR.
- $\beta_0$ = Base intercept.
- $x_1, \dots, x_n$ = Vector of continuous features (*Area, Bedrooms, Bathrooms, Age, Parking*) and categorical indicators (*City, Category, Furnishing*).
- $\epsilon$ = Residual error term.

Model quality is verified via Mean Squared Error ($MSE$) and Coefficient of Determination ($R^2$):
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \qquad R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$

### 2. Buyer Barometer Variance Logic
$$\Delta\% = \left(\frac{P_{\text{asking}} - P_{\text{predicted}}}{P_{\text{predicted}}}\right) \times 100$$

- **$\Delta\% \le -10\%$**: **Great Deal** (Priced below market level; high buyer value).
- **$-10\% < \Delta\% \le +10\%$**: **Fair Market Price** (Accurately aligned with market expectations).
- **$\Delta\% > +10\%$**: **Premium / High** (Listed at a premium; negotiation advised).

### 3. Primary Academic Deliverable: Time-to-Appointment
$$T_{\text{appt}} = t_{\text{confirmed}} - t_{\text{first\_inquiry}}$$
- **Course Benchmark Target:** Median $T_{\text{appt}} \le 2.0\text{ hours}$ during pilot trials.
- **Attribution:** Automatically logged in SQLite database via UTC ISO-8601 timestamps.

---

## 🛠️ Technology Stack

| Layer | Technologies Used | Rationale |
| :--- | :--- | :--- |
| **Front-End** | Vanilla HTML5, Modern CSS3 (Flexbox/Grid), ES6+ JavaScript | Zero build tool dependencies; native browser performance; mobile responsive. |
| **Back-End** | Python 3.10+, Flask 3.x, Flask-CORS, Werkzeug | Lightweight, rapid prototyping, clean RESTful architecture. |
| **Machine Learning**| Scikit-learn 1.4+, NumPy, Joblib | Fast local inference ($< 100\text{ms}$); zero external paid cloud dependencies. |
| **Database** | SQLite 3 (relational engine with parameterized queries) | ACID compliance; zero administrative overhead; seamless portability. |
| **Testing & CI** | Pytest, GitHub Actions CI Pipeline | Automated regression testing on multi-version Python environments. |

---

## ⚡ Quickstart & Local Deployment

### 1. System Requirements
- Python 3.10 or higher.
- Git.

### 2. Clone the Repository
```bash
git clone https://github.com/guntaas0108-eng/Software-Engineering-Project.git
cd Software-Engineering-Project
```

### 3. Initialize Virtual Environment & Install Dependencies
```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Execute Automated Test Suite
```powershell
.\venv\Scripts\pytest.exe code\backend\tests -v
```
*Expected Output: `8 passed` across API routes, ML regression, and Buyer Barometer logic.*

### 5. Launch the Web Application
```powershell
.\venv\Scripts\python.exe code\backend\app.py
```
Open **[http://localhost:5000](http://localhost:5000)** in any modern web browser or mobile device connected to the local network.

---

## 📂 Repository Directory Layout

```plaintext
Software-Engineering-Project-main/
├── .github/
│   ├── workflows/
│   │   └── ci.yml               # Automated multi-version CI test pipeline
│   ├── ISSUE_TEMPLATE/          # Structured issue reporting templates
│   └── pull_request_template.md # Standard PR review checklist
├── code/
│   ├── backend/
│   │   ├── app.py               # Flask REST API controller & static file server
│   │   ├── database.py          # SQLite relational schema, seed generator, CRUD
│   │   ├── ml_model.py          # Multiple Linear Regression & Barometer logic
│   │   └── tests/
│   │       ├── test_api.py      # Automated API endpoint & appointment tests
│   │       └── test_ml_model.py # ML accuracy, MSE, and Barometer tests
│   └── frontend/
│       ├── index.html           # Semantic SPA with full-bleed real estate hero
│       ├── style.css            # High-contrast mobile-responsive CSS
│       └── app.js               # Client controller, asynchronous API client
├── docs/                        # Formal System Documentation (MkDocs & Academic)
│   ├── SRS.md                   # Software Requirements Specification (v1.0 Markdown)
│   ├── SRS.tex                  # Software Requirements Specification (LaTeX Source)
│   ├── architecture.md          # 3-tier architecture & data dictionary
│   ├── ml-model.md              # Mathematical derivations and formulas
│   ├── api-reference.md         # Comprehensive REST API specifications
│   └── evaluation-metrics.md    # Course metric attribution specifications
├── journals/                    # Individual Student Weekly Engineering Journals
│   ├── Guntaas_Singh_1024030108_Journal.md
│   ├── Haneesh_1024030112_Journal.md
│   ├── Dhruv_Rajput_1024030538_Journal.md
│   ├── Atiksh_102303133_Journal.md
│   └── README.md                # Engineering journal directory overview
├── project-proposal/            # Approved UCS503P Course Project Proposal
│   ├── Software_Eng_Project.pdf # Compiled proposal PDF
│   └── main_s.tex               # Proposal LaTeX source
├── project-report-prototype-stage/
│   └── prototype_stage_report.md# Mid-semester prototype deliverable report
├── project-report-final/
│   └── final_report_outline.md  # Final project roadmap
├── scripts/
│   └── archive/                 # Archived migration and utility scripts
├── CONTRIBUTING.md              # Git collaboration and branch workflow guidelines
├── LICENSE                      # MIT Open Source License
├── Makefile                     # Build, test, and run automation targets
├── mkdocs.yml                   # MkDocs documentation builder configuration
├── pyproject.toml               # Python project configuration & pytest settings
├── requirements.txt             # Managed Python dependencies
├── README.md                    # Primary repository documentation
└── SRS.md                       # Root-level copy of SRS Specification
```

---

## 📄 License
This project is licensed under the terms of the [MIT License](LICENSE).
