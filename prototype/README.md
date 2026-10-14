# EstatePulse — Prototype Version (SEO, Security & Accessibility)

This directory preserves the complete standalone prototype of **EstatePulse** developed during Sprint 3 / Conversation 1 (`EstatePulse-SEO-Test`).

---

## 📌 Prototype Overview

The prototype showcases specialized web quality, security, and accessibility features alongside the core real estate marketplace:
- **Interactive AI Assistant Tips Widget:** Floating button with rotating real estate market tips and guidance.
- **Form Validation & Multi-Step Progress Tracker:** 3-step progress bar, character countdown, real-time input validation, and submit button loading states.
- **Enhanced Security Headers:** Strict Content Security Policy (CSP), X-Frame-Options (DENY), HSTS, and X-Content-Type-Options.
- **SEO & Web Standards:** Auto-generated `/robots.txt`, XML sitemap (`/sitemap.xml`), canonical links, and Open Graph meta tags.
- **Legal & Error Pages:** Dedicated `/privacy-policy` page and custom 404 error page with animated illustration.
- **Mobile Sticky Navigation:** 1-thumb bottom navigation bar.

---

## 🚀 How to Run the Prototype Independently

The prototype is configured to run on **port 5001** so it will not conflict with your main project on port 5000:

```powershell
# From project root:
.\venv\Scripts\python.exe prototype/code/backend/app.py
```
Open **[http://localhost:5001](http://localhost:5001)** in your browser.

---

## 📂 Directory Layout

```plaintext
prototype/
├── code/
│   ├── backend/
│   │   ├── app.py           # Backend with security headers, robots, sitemap, privacy & 404
│   │   ├── database.py      # SQLite schema and sample seeds
│   │   ├── ml_model.py      # Multiple Linear Regression predictor
│   │   └── tests/           # Automated test suites
│   └── frontend/
│       ├── index.html       # Prototype SPA with AI tips widget, multi-step form & mobile nav
│       ├── style.css        # Prototype styling
│       └── app.js           # Prototype frontend controller
└── README.md                # This documentation file
```
