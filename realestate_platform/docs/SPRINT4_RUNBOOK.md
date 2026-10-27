# PropertyPulse Sprint 4 — Completion Runbook

## Sprint goal
Deliver authenticated buyer–seller messaging, site-visit appointment requests and decisions, appointment audit history, and a measurable time-to-appointment metric without breaking the Sprint 1–3 marketplace.

## Implemented in this snapshot
- Conversations tied to a property and its buyer/seller.
- Authenticated inbox and conversation pages.
- HTTP message submission fallback and Django Channels WebSocket messaging.
- Participant checks for conversation pages and WebSocket connections.
- Message timestamps and read timestamps when the other participant opens the thread.
- Buyer requests a future site visit; seller confirms or declines; buyer or seller can cancel a requested/confirmed visit.
- Appointment status events with actor and timestamp.
- Staff-only appointment metrics page, including median time from first message to seller confirmation.
- Django admin screens for conversations, messages, appointments, and appointment events.

## 1. Prepare local environment
Use Python 3.11 (matches CI) and a virtual environment. Run commands from the folder containing `manage.py`.

### macOS / Linux
```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

### Windows PowerShell
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
Copy-Item .env.example .env
```

For local SQLite evaluation, set `DB_ENGINE=sqlite` in `.env`. For the team's PostgreSQL setup, configure `DB_ENGINE=postgresql` and the `DB_*` variables. Never commit `.env` or real secrets.

## 2. Run checks
```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test
```

If `makemigrations --check --dry-run` reports model changes, inspect them and create a migration only after reviewing the diff. Do not delete existing migrations or the database to silence an error.

Create an administrator for the metrics page and Django admin if needed:
```bash
python manage.py createsuperuser
```

Start the ASGI-capable development server:
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Chat routes are documented in `SPRINT4_IMPLEMENTATION.md`.

## 3. Required manual acceptance tests
Use two separate browser profiles (or one normal and one private window) and two different accounts. One account must own the property and the other must be the buyer.

| ID | Test | Expected result | Evidence to record |
|---|---|---|---|
| S4-01 | Anonymous user opens `/chat/` | Redirected to login | Screenshot or test output |
| S4-02 | Buyer opens a property and starts chat | One conversation opens for that buyer/property | Conversation ID |
| S4-03 | Buyer sends a message while seller thread is open | Message appears in both sessions without manual refresh when WebSocket is connected | Screenshot/video |
| S4-04 | Non-participant tries to open a conversation URL | Access denied (404) | Test output |
| S4-05 | Buyer submits blank message | Message is not saved | Test output |
| S4-06 | Buyer requests a future site visit | Status is `Requested`; audit event is created | Appointment ID/status |
| S4-07 | Seller confirms request | Status becomes `Confirmed`; `confirmed_at` is set; event is created | Appointment ID/status |
| S4-08 | Seller declines request | Status becomes `Declined`; event is created | Appointment ID/status |
| S4-09 | Buyer or seller cancels a requested/confirmed visit | Status becomes `Cancelled`; event is created | Appointment ID/status |
| S4-10 | Attempt to confirm as buyer or request as seller | Request is rejected | Test output |
| S4-11 | Staff opens `/chat/metrics/appointments/`; ordinary user tries it | Staff sees metrics; ordinary user is denied | Screenshot/test output |
| S4-12 | Reload conversation after sending messages | Messages persist in database and display in chronological order | Screenshot |
| S4-13 | Run full Django tests and CI workflow | All tests and lint checks pass | CI run URL / terminal output |

**Do not mark a test passed without observing the expected result.** Record failures as bugs, fix them, and rerun the affected test plus the full suite.

## 4. WebSocket deployment note
The in-memory Channels layer is suitable for a single local development process. For multi-worker deployment, configure Redis through `REDIS_URL`. When testing across two laptops, both users must access the same deployed/LAN-reachable server; `127.0.0.1` on one laptop is not reachable from the other laptop.

## 5. Definition of Done
- [ ] `python manage.py check` passes.
- [ ] Migration check passes with no unexpected changes.
- [ ] Database migrations apply successfully.
- [ ] Full automated test suite passes.
- [ ] All manual acceptance tests S4-01 through S4-13 are recorded.
- [ ] Buyer and seller real-time messaging verified in separate sessions.
- [ ] Appointment transitions and audit events verified.
- [ ] Staff-only metrics permissions verified.
- [ ] CI is green on the team repository.
- [ ] Sprint 4 demo and weekly journal reflect only work actually completed.

## Current verification status for this archive
Python syntax compilation succeeded during archive inspection. Django runtime checks, automated tests, database migration checks, and two-session live WebSocket testing could not be executed in the current environment because Django and project dependencies were not installed and package downloads were unavailable. Therefore Sprint 4 is **implementation-present but not yet verified complete** until the checks above pass on the team's machine or CI.
