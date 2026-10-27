# PropertyPulse — Sprint 4 implementation notes

## Scope delivered in this code snapshot

- Buyer–seller conversations tied to a property, with one conversation per buyer/property pair.
- Authenticated inbox and conversation thread pages.
- HTTP message submission fallback and WebSocket live messaging through Django Channels.
- WebSocket access limited to authenticated conversation participants and validated host origins.
- Buyer-requested site visits, seller confirm/decline, and buyer/seller cancellation while a visit is pending or confirmed.
- Appointment status audit events with actor and timestamps.
- Time-to-appointment measurement from a conversation's first message to seller confirmation; staff-only median metrics page.
- Django admin registration for conversations, messages, appointments, and appointment events.
- Navigation and property detail call-to-action links into chat.

## Data model

- `Conversation`: property, buyer, seller, creation/update timestamps, first message timestamp.
- `Message`: conversation, sender, body, creation timestamp, read timestamp.
- `Appointment`: conversation, requester, requested visit time, status, confirmation timestamp, notes.
- `AppointmentEvent`: audit record for appointment status changes.

## Setup

1. Install `requirements.txt`.
2. Configure `.env`; use `DB_ENGINE=sqlite` for local evaluation or PostgreSQL for the team's normal environment.
3. Run `python manage.py migrate`.
4. Run `python manage.py runserver` (Daphne is included in `INSTALLED_APPS` so the development server supports ASGI/WebSockets).
5. Sign in as a buyer and use a property detail page to message its seller. Test live messaging with a second browser/session signed in as the seller.

For multiple application workers, configure Redis using `REDIS_URL=redis://127.0.0.1:6379/0`. The in-memory channel layer is only suitable for local single-process development.

## Routes

- `/chat/` — inbox
- `/chat/start/<property_id>/` — start or reopen a property conversation
- `/chat/<conversation_id>/` — conversation thread and appointment panel
- `/chat/<conversation_id>/appointments/request/` — buyer appointment request endpoint
- `/chat/appointments/<appointment_id>/<confirm|decline|cancel>/` — appointment state transition
- `/chat/metrics/appointments/` — staff-only metrics
- `/ws/chat/<conversation_id>/` — WebSocket endpoint

## Validation status

Python syntax compilation completed successfully for the project. The full Django checks, migrations, HTTP tests, and live WebSocket integration tests could not be executed in this environment because Django and its compatible dependencies were not installed, internet access was unavailable for installation, and the only bundled environment found was Windows-specific. Do not describe this snapshot as fully runtime-tested until `python manage.py check`, `python manage.py makemigrations --check`, `python manage.py migrate`, `python manage.py test`, and a two-session WebSocket smoke test have passed on the team's machine/CI.
