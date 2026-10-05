# REST API Reference

The backend exposes a JSON REST API on `http://localhost:5000/api`.

---

## 🏠 Properties

### `GET /api/properties`
Fetch filtered properties.
- **Query Parameters:** `city`, `property_type`, `barometer`, `search`, `min_price`, `max_price`.
- **Response:**
  ```json
  {
    "success": true,
    "count": 6,
    "data": [ ... ]
  }
  ```

### `GET /api/properties/<id>`
Fetch details and valuation analysis for a specific property.

### `POST /api/properties`
Create a new property listing with automated ML valuation.
- **Body:** `title`, `description`, `property_type`, `city`, `locality`, `area_sqft`, `bedrooms`, `bathrooms`, `property_age`, `has_parking`, `furnishing`, `price`, `seller_name`, `seller_phone`.

### `POST /api/check-duplicates`
Detects potential duplicates based on title similarity and locality.
- **Body:** `{ "title": "...", "property_type": "...", "locality": "...", "city": "..." }`

---

## 🤖 Machine Learning

### `POST /api/predict`
Calculate fair market value and buyer barometer score for arbitrary inputs.

### `GET /api/ml-metrics`
Returns current model diagnostics: `mse`, `mae`, `rmse`, `r2_score`, `training_samples`.

---

## 💬 Integrated Messaging

### `GET /api/properties/<id>/messages`
Fetch conversational thread for a property.

### `POST /api/properties/<id>/messages`
Send message as buyer or seller.
- **Body:** `{ "sender_type": "buyer", "sender_name": "...", "message_text": "..." }`

---

## 📅 Appointments & Payments

### `POST /api/appointments`
Schedule a site visit and record initial inquiry timestamp.

### `POST /api/appointments/<id>/confirm`
Seller confirms site visit; calculates and stores **Time-to-Appointment**.

### `POST /api/payments`
Records visit booking token (₹500 refundable).

### `GET /api/metrics`
Aggregated platform metrics for course evaluation.
