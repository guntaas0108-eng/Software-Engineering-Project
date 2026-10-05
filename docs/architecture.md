# System Architecture

EstatePulse employs a 3-tier decoupled architecture designed for high scalability, separation of concerns, and ease of deployment in accordance with educational operational constraints.

---

## 🏗️ 3-Tier Architecture Overview

```
+-------------------------------------------------------------+
|                  Client / Presentation Layer                |
|  - Responsive Single-Page Application (HTML5 / CSS3 / ES6) |
|  - Buyer Barometer Gauge, Chat Views, Analytics Dashboard   |
+------------------------------+------------------------------+
                               | REST API / JSON
                               v
+-------------------------------------------------------------+
|                     Application & ML Tier                   |
|  - Python Flask Web Framework                               |
|  - Scikit-Learn Multiple Linear Regression Engine           |
|  - Duplicate Listing Detector & Appointment Scheduler       |
+------------------------------+------------------------------+
                               | SQLite Driver
                               v
+-------------------------------------------------------------+
|                      Persistence Tier                       |
|  - SQLite Relational Database Engine                        |
|  - Tables: properties, messages, appointments, payments     |
+-------------------------------------------------------------+
```

---

## 🗄️ Database Schema Design

### 1. `properties`
Stores physical attributes, pricing, and cached ML valuation results.
- `id` (INTEGER PRIMARY KEY)
- `title`, `description`, `property_type`, `city`, `locality`
- `area_sqft`, `bedrooms`, `bathrooms`, `property_age`, `has_parking`, `furnishing`
- `price`, `predicted_price`, `barometer_score`, `barometer_verdict`
- `seller_name`, `seller_phone`, `created_at`

### 2. `messages`
Maintains conversational threads per property for buyer-seller negotiation.
- `id` (INTEGER PRIMARY KEY)
- `property_id` (FOREIGN KEY)
- `sender_type` ('buyer' | 'seller' | 'system')
- `sender_name`, `message_text`, `timestamp`

### 3. `appointments`
Tracks site visit requests and time-to-appointment duration.
- `id` (INTEGER PRIMARY KEY)
- `property_id` (FOREIGN KEY)
- `buyer_name`, `buyer_phone`, `visit_date`, `visit_time`, `notes`
- `status` ('pending' | 'confirmed')
- `first_inquiry_timestamp`, `confirmed_timestamp`, `time_to_appointment_seconds`

### 4. `payments`
Maintains records of visit booking tokens.
- `id` (INTEGER PRIMARY KEY)
- `property_id`, `appointment_id`, `buyer_name`, `amount`, `payment_method`
- `transaction_id`, `payment_status`, `timestamp`
