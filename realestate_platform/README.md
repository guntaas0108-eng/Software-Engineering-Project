# PropertyPulse — Real Estate Price Prediction & Marketplace Platform

UCS503P Software Engineering project (TIET). "PropertyPulse" is a placeholder
working name — rename it anywhere you like, it has no effect on functionality.

This repo currently implements **Sprint 0 + Sprint 1** — the MVP defined in
the proposal (section 9.1): property submission, ML price prediction, the
Buyer Barometer, basic logging, and CI. Sprints 2-6 (auth polish, buyer
search, chat, payments, admin dashboard) get built on top of this
incrementally — see the Scrum handbook for the full roadmap.

## 1. Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # then edit .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

For a quick local run without installing Postgres, set `DB_ENGINE=sqlite`
in `.env` — everything else works the same. Postgres is the intended
production/staging database per the proposal.

## 2. Where each person's work lives

| Person | Area | Main files |
|---|---|---|
| 1 — ML & Dataset | Price prediction | `ml_predictor/` |
| 2 — Backend/DB/Seller | Models, auth, seller flows | `properties/models.py`, `accounts/`, `config/settings.py` |
| 3 — Frontend/Buyer/Barometer | UI | `templates/`, `properties/templates/`, `static/` |
| 4 — Chat/Appointments/Payments/Admin | CI/CD now; `chat/`, `payments/` from Sprint 4 | `.github/workflows/ci.yml` |

## 3. Adding your trained Hugging Face model

This is the one manual step Person 1 needs to do after training:

1. Train the model:
   ```bash
   cd ml_predictor/train
   pip install -r requirements-train.txt
   python train_model.py --data your_dataset.csv --out model.joblib
   ```
   (Adjust `FEATURE_COLUMNS` / `TARGET_COLUMN` at the top of `train_model.py`
   if your dataset's column names differ.)

2. Push it to the Hugging Face Hub:
   ```bash
   python push_to_hf.py --repo-id your-username/realestate-price-predictor --file model.joblib
   ```

3. In the Django project's `.env`, set:
   ```
   HF_MODEL_REPO_ID=your-username/realestate-price-predictor
   HF_MODEL_FILENAME=model.joblib
   HF_TOKEN=            # only needed if the repo is private
   ```

That's it — `ml_predictor/model_loader.py` downloads and caches the model
the first time a prediction is requested. No other code changes needed.
Re-run `push_to_hf.py` any time you retrain; restart the server (or call
`reload_model()`) to pick up the new version.

## 4. Running tests

```bash
python manage.py test
```

The same checks run automatically in GitHub Actions on every push — see
`.github/workflows/ci.yml`.

## 5. Project roadmap

See **"UCS503P — Agile Scrum Project Plan & Documentation Handbook.docx"**
for the full 12-week sprint plan, the product backlog, and the weekly
document templates you'll submit alongside this code.


## Sprint 4 — chat and site-visit appointments

1. Install dependencies with `pip install -r requirements.txt`.
2. For a quick local setup, set `DB_ENGINE=sqlite` in `.env`; PostgreSQL remains the recommended team configuration.
3. Run `python manage.py migrate`, then `python manage.py runserver`.
4. Sign in as a buyer, open a listing owned by another user, and choose **Message seller / arrange a visit**. Open the same conversation as the seller in another browser/session to test live messages.
5. The buyer can request a future visit; the seller can confirm or decline. Staff can view the time-to-appointment metric at `/chat/metrics/appointments/`.

Local development uses an in-memory Channels layer and supports one server process. For multi-worker staging/production, set `REDIS_URL` (for example `redis://127.0.0.1:6379/0`) and serve `config.asgi:application` with an ASGI server. The metrics page measures elapsed time from a conversation's first message to appointment confirmation; it does not claim the proposal's target has already been achieved.
