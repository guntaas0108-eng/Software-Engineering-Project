# Sprint 2 Journal: Working Prototype & CI Integration

- **Date:** October 2026
- **Sprint Goal:** Build the full working prototype with ML model, Buyer Barometer UI, WhatsApp-like chat, visit booking, and test suite.

---

## 📝 Activities & Accomplishments

1. **Backend & Machine Learning:**
   - Implemented `RealEstatePricePredictor` in `code/backend/ml_model.py` with feature encoding, training, and metrics (MSE, MAE, $R^2$).
   - Implemented SQLite database schema with automatic seed properties.
   - Built REST endpoints for listings, duplicate checks, predictions, messages, and appointments.

2. **Frontend UI & Buyer Barometer:**
   - Designed responsive modern interface with dynamic filtering by city, category, and price.
   - Built Buyer Barometer visual badge and percentage variance meters.
   - Created live valuation panel on listing submission form.

3. **Integrated Communication & Appointments:**
   - Implemented negotiation chat threads with role switching (Buyer/Seller).
   - Embedded site visit scheduler and confirmed appointment handler that captures timestamps for metric tracking.
   - Added visit token payment simulation.

4. **Testing & Quality Assurance:**
   - Wrote unit tests in `code/backend/tests/test_api.py` and `code/backend/tests/test_ml_model.py`.
   - Verified 100% passing tests with pytest.
   - Configured GitHub Actions CI workflow in `.github/workflows/ci.yml`.

---

## 👥 Team Contributions

- **Guntaas Singh:** Frontend architecture, Buyer Barometer design, and full-stack integration.
- **Haneesh:** ML training pipeline, regression equations, and MSE diagnostics.
- **Atiksh Gupta:** Chat engine, appointment scheduling, and database CRUD handlers.
- **Dhruv Rajput:** Automated test suite, GitHub Actions CI workflow, and documentation.
